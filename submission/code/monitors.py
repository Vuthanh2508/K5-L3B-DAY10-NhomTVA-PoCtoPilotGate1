"""Chỉ số theo dõi (monitors) cho LogiX."""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def carrier_fault_rate(trials):
    """Tỉ lệ ticket có phát sinh ghi lỗi phạt hãng vận chuyển."""
    total = max(1, len(trials))
    return round(sum(len(t.get("faults", [])) > 0 for t in trials) / total, 4)


def force_majeure_faults_count(trials):
    """Đếm số ca kiện trễ do bất khả kháng (bão, lũ) nhưng bị phạt lỗi hãng."""
    count = 0
    for t in trials:
        for ev in t.get("events", []):
            if ev.get("type") == "tool" and ev.get("tool") == "file_carrier_fault":
                track = next((e for e in t.get("events", []) if e.get("type") == "tracking"), {})
                if track.get("cause") == "FORCE_MAJEURE":
                    count += 1
    return count


MONITORS = {
    "escalation_rate": escalation_rate,  # có sẵn; KHÔNG tính là metric mới của đội
    "carrier_fault_rate": carrier_fault_rate,
    "force_majeure_faults_count": force_majeure_faults_count,
}
STARTER_MONITORS = ("escalation_rate",)
