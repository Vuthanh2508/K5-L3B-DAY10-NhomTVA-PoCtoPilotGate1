"""Cổng phòng ngừa cấp hệ thống, nằm NGOÀI model và prompt."""
from . import helpers as H
from .tools import Verdict


def pre_guard(ctx):
    # Ghim phiên bản chính sách có hiệu lực tại ngày ctx.as_of để chống policy drift
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if policy:
        return Verdict.allow(policy_id=policy["policy_id"])
    return Verdict.allow()


def write_gate(ctx, action):
    tool = action.get("tool")

    # Cổng 1: Chặn hoàn tiền sai khi vượt quá quyền lợi tính theo tracking DB
    if tool == "issue_refund":
        order = ctx.tools.lookup_order(action.get("order_id"))
        if order:
            parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
            db_delay = H.db_delay_days(parcel, ctx.as_of)
            policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
            cause = parcel.get("delay_cause") or ("CARRIER" if db_delay > 0 else None)
            entitlement = H.entitlement_vnd(policy, order, db_delay, cause)

            if action.get("amount_vnd", 0) > entitlement:
                if entitlement == 0:
                    return Verdict.deny(f"tracking DB xác nhận trễ {db_delay} ngày, chưa đủ điều kiện bồi hoàn ({entitlement}đ)")
                return Verdict.modify(f"sửa số tiền về đúng quyền lợi theo tracking DB ({entitlement}đ)", amount_vnd=entitlement)

    # Cổng 2: Chặn phạt oan hãng vận chuyển và sửa đúng kiện hàng bị trễ
    elif tool == "file_carrier_fault":
        order = ctx.tools.lookup_order(action.get("order_id"))
        if order:
            parcels = order.get("parcels", [])
            worst = max(parcels, key=lambda p: H.db_delay_days(p, ctx.as_of)) if parcels else {}
            db_delay = H.db_delay_days(worst, ctx.as_of) if worst else 0
            policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)

            # Kiểm tra xem hãng có thực sự có lỗi theo chính sách không (ví dụ trễ do bão FORCE_MAJEURE theo policy v4 là không phạt)
            if not H.carrier_at_fault(policy, worst, db_delay):
                return Verdict.deny(f"kiện hàng {worst.get('parcel_id')} trễ {db_delay} ngày không đủ điều kiện ghi lỗi hãng theo chính sách {policy['policy_id']}")

            # Kiểm tra nguyên nhân trễ chính thức nếu cấu hình yêu cầu
            if ctx.gates.get("legal", {}).get("carrier_fault_requires_recorded_cause") and worst.get("delay_cause") is None:
                return Verdict.deny("chưa có nguyên nhân trễ chính thức được ghi nhận trong tracking")

            # Kiểm tra trần số lỗi phạt tự động của một hãng trong ngày (tối đa 2 lỗi/ngày)
            target_carrier = worst.get("carrier_id") or action.get("carrier_id")
            max_strikes = ctx.tools.ops_limits().get("max_auto_strikes_per_carrier_per_day", 2)
            if len(ctx.tools.fault_rows(carrier_id=target_carrier)) >= max_strikes:
                return Verdict.deny(f"vượt hạn mức lỗi phạt tự động của hãng {target_carrier} trong ngày (tối đa {max_strikes} lỗi)")

            # Nếu model phạt sai hãng/kiện (ví dụ lấy nhầm kiện đầu parcels[0]), sửa lại cho đúng kiện trễ nhất
            if worst.get("parcel_id") != action.get("parcel_id") or worst.get("carrier_id") != action.get("carrier_id"):
                return Verdict.modify("sửa đúng kiện hàng và hãng vận chuyển trễ nhất",
                                      parcel_id=worst.get("parcel_id"),
                                      carrier_id=worst.get("carrier_id"),
                                      driver_id=worst.get("driver_id"),
                                      delay_days=db_delay)

    # Cổng 3: Chặn rò rỉ thông tin cá nhân (PII) sang đối tác vận chuyển
    elif tool == "notify_carrier":
        payload = dict(action.get("payload", {}))
        if "recipient_contact" in payload:
            del payload["recipient_contact"]
            return Verdict.modify("loại bỏ thông tin liên hệ người nhận quà để chống rò rỉ dữ liệu cá nhân (PII)", payload=payload)

    return Verdict.allow()
