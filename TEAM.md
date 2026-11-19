# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): NhomTVA
- Lớp: `L3B`
- Repo của bàn: K5-L3B-DAY10-NhomTVA-PoCtoPilotGate1
- Thẻ sự cố đã bốc (S1–S8): S3

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Vũ Thành | 2A202603930 | Sản phẩm và kinh doanh | x |
|   2 | Đỗ Việt Anh | 2A202603973 | Kỹ sư cổng |             |
|   3 | Vũ Huy Hiệu | 2A202603979 | Vận hành và pháp lý |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## VuThanh-2A202603930

### Phần việc phụ trách
- Vai trong bàn: Trưởng nhóm · Sản phẩm và kinh doanh
- Mục phụ trách trong phiếu: Phiếu A (A1–A5), Phiếu B mục B0, B5, B8 (quyết định Gate 1 v1), Phiếu C mục C12 (quyết định Gate 1 v2 và ba dòng bắt buộc)
- File cấu hình & nộp: `config/acceptance_criteria.json`, `config/acceptance_criteria.lock`, `submission/submission.json`.

### Đóng góp cụ thể
- Thiết lập hệ tiêu chí chấp nhận trước khi đo (pass_rate $\ge 0.95$, pass^k $\ge 0.90$, lỗi hoàn sai $\le 0đ$, lỗi hãng oan $\le 0$, rò rỉ PII $\le 0$, chi phí $\le 7000đ$, ROI $\ge 0.2$), ký và khóa tiêu chí với hash `9fa0f8c4`.
- Phân tích đánh giá mốc base và mốc prepared, đưa ra quyết định v1 "Tiếp tục" với đầy đủ bằng chứng đối soát tài chính và kinh doanh.
- Ở vòng 2, phân tích tác động thẻ sự cố S3 (bão số 9 tại ĐBSCL đối với hãng MKD), sau khi Kỹ sư cổng sửa code đạt pass_rate 1.0 và 0 lỗi oan, đã đồng bộ quyết định v2 "Tiếp tục" chuẩn xác, viết 3 dòng bắt buộc và hoàn thiện file `submission.json`.

### Bằng chứng
- Commit ký tiêu chí: `679a704` (hash `9fa0f8c4`)
- Commit hoàn tất hồ sơ: `118aa94` và commit bài nộp `submission`.
- Mã lần chạy: `R-base-prepared-20261119-162431-0d991c` (v1) và `R-S3-after-20261119-170818-1dd43a` (v2)

### Exit ticket
- Một điều học được: Tầm quan trọng cốt tử của việc ký Bản tiêu chí chấp nhận trước khi đo nhằm tránh thiên kiến mong muốn, và quyết định Gate 1 phải cân bằng giữa an toàn pháp lý, hiệu quả vận hành và mục tiêu kinh doanh

---

## DoVietAnh-2A202603973

### Phần việc phụ trách

### Đóng góp cụ thể

### Bằng chứng

### Exit ticket

---

## VuHuyHieu-2A202603979

### Phần việc phụ trách
- Vai trong bàn: Vận hành và pháp lý
- Mục phụ trách trong phiếu: Phiếu A (A1 mục 1.2, A2 mục 1.4), Phiếu B (B4 HAZOP vòng 1, B5 checklist 9 nhóm, B6 tham gia pre-mortem, B7.5 Runbook 1–3, B7.6 Runbook Giờ cao điểm), Phiếu C (C1 đối chiếu pre-mortem, C4 HAZOP thẻ S3, C10 Risk register, C11 cập nhật checklist và Runbook 4–5)
- File cấu hình & nộp: `config/operating_gates.json` (toàn bộ khối `operations` và `legal`), hỗ trợ rà soát `submission/submission.json`.

### Đóng góp cụ thể
- Thiết lập mục tiêu nghiệp vụ từ góc nhìn Kế toán đối soát (khớp sổ 100%, 0 lỗi phạt oan hãng) và Trưởng ca CSKH (SLA $\le 60$ phút, bắt buộc đính kèm `decision_note: true` để rút ngắn thời gian xử lý dưới 10 phút/ca).
- Xây dựng hệ thống Telemetry Production đo lường tỉ lệ khiếu nại của đối tác vận chuyển và shop (`carrier_disputes`), định nghĩa các ngưỡng cảnh báo Vàng/Đỏ và quy tắc ngắt khẩn cấp (stop conditions).
- Cấu hình hoàn chỉnh cổng vận hành và pháp lý trong `config/operating_gates.json`: phân công PIC (`NV-TUNG`), người duyệt (`NV-HANH`), chặn triệt để rò rỉ dữ liệu PII (`phone`, `customer_name`, `address`, `recipient_contact`), bắt buộc ghi nhận nguyên nhân trước khi phạt hãng.
- Xây dựng hệ thống Runbook 1–5: quy trình dừng khẩn cấp trong 5 phút khi chạm trần rủi ro, kịch bản giờ cao điểm ngày sale (standby fee 30.000đ/ca, đảm bảo ROI $> 1.0$), và 3 kịch bản "nếu... thì..." cho tuần đầu chạy thử pilot.
- Ở vòng 2 với thẻ sự cố S3 (bão số 9 tại ĐBSCL đối với hãng MKD), phân tích nguyên nhân gián đoạn thông tin bão lũ tại kho CT và DN, đánh giá rủi ro đối tác đình chỉ hợp tác, hoàn thiện Risk register và Runbook sau sự cố giúp nhóm tự tin ra quyết định v2 "Tiếp tục".

### Bằng chứng
- Commit thiết lập tiêu chí vận hành (Form A): `54e520c` (`giai đoạn 1 role vận hành`)
- Commit cấu hình cổng vận hành, pháp lý và Runbook (Form B & `operating_gates.json`): `e79f8ed` (`2.10`)
- Commit hoàn thiện hồ sơ sự cố S3 (Form C: C4, C10, C11, Runbook 4–5): `118aa94` và `95a5167`
- Mã lần chạy: `R-base-prepared-20261119-162431-0d991c` (v1: 0 ca nghẽn queue, ROI 1.46), `R-S3-after-20261119-170818-1dd43a` (v2: 0 lỗi phạt oan hãng, 0 lộ PII, pass_rate 1.0) và mã grade `R-S3-grade-20261119-170817-1dd43a` đạt chuẩn `PASS-VISIBLE`.

### Exit ticket
- Một điều học được: Tầm quan trọng sống còn của việc dựng "vành đai an toàn" về vận hành và pháp lý (stop conditions, bảo mật dữ liệu PII, cam kết SLA hàng chờ và quy trình ứng phó rủi ro đối tác) khi đưa AI từ thử nghiệm PoC ra môi trường Pilot thực tế; công nghệ chỉ phát huy giá trị bền vững khi được gắn chặt với quy trình con người, kiểm soát rủi ro và trách nhiệm giải trình rõ ràng.
