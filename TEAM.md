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
- Vai trong bàn: Kỹ sư cổng (Gate Engineer)
- Mục phụ trách trong phiếu: Phiếu A (A2 mục 1.3 Offline metric), Phiếu B (B0 mốc base, B2 soát lỗi T-002@55, B6 pre-mortem kỹ thuật, B7.1–B7.3 code cổng guards và chống data leakage), Phiếu C (C0 nhật ký chạy, C1 mốc prepared, C2 soát lỗi S3, C4 HAZOP S3, C6 Fault tree trước sửa, C7 Bảng sửa, C8 chỉ số theo dõi mới, C9 Fault tree sau sửa)
- File code & cấu hình phụ trách: `lab10/guards.py` (toàn bộ hàm `pre_guard`, `write_gate`), `lab10/monitors.py` (định nghĩa và đăng ký các monitor theo dõi), kiểm thử với `lab10.eval` và `lab10.grade`.

### Đóng góp cụ thể
- Thiết kế Offline Metric (Câu 1.3): Xây dựng bộ đo lường độc lập cho bước `file_carrier_fault` với công thức tính F1-Score/Accuracy, nguồn nhãn đối soát từ tracking DB để đánh giá khả năng nhận diện lỗi hãng trước khi triển khai.
- Phát triển Cổng bảo vệ Vòng 1 (`lab10/guards.py`):
  - Chặn đứng 100% tiền hoàn sai và hoàn thiếu (`issue_refund`): Bắt buộc đối chiếu `db_delay_days` và `entitlement_vnd` từ tracking DB, triệt tiêu lỗi khách khai gian ngày trễ (sửa triệt để ca `T-002@55`).
  - Bảo vệ dữ liệu cá nhân (PII): Tự động lọc bỏ số điện thoại, địa chỉ nhà (`recipient.phone`, `recipient.street`) trước khi gọi `notify_carrier`.
  - Ghim chính sách hiệu lực (`effective_policy`): Ngăn ngừa trôi dạt chính sách (policy drift) theo ngày `as_of`.
  - Giúp hệ thống ở mốc prepared đạt pass rate từ 0.25 lên 0.8333, hoàn sai về 0đ, lộ PII về 0.
- Xử lý sự cố Thẻ S3 (Hãng Mekong Delta Ship bị phạt oan do bão số 9):
  - Dò trace các ticket lỗi (`S3-01`, `S3-04`, `S3-40`..`S3-43`), phát hiện 2 nguyên nhân gốc: (1) Chính sách `REFUND-v4` miễn trừ bão lũ `FORCE_MAJEURE` nhưng DB chưa cập nhật cờ; (2) Thiếu kiểm soát trần số lần phạt tích lũy trong ngày của đối tác.
  - Cập nhật `write_gate`: Bổ sung kiểm tra `len(ctx.tools.fault_rows(carrier_id=carrier_id)) >= 2` (khóa cứng trần tối đa 2 lỗi/ngày) và loại trừ mọi lệnh phạt do thiên tai; chọn đúng kiện hàng trễ nhất (`H.worst_parcel`).
  - Viết 2 monitors trong `lab10/monitors.py`: `carrier_fault_rate` (tỉ lệ ticket phát sinh phạt hãng) và `force_majeure_faults_count` (đếm lỗi phạt trong ngày thiên tai).
  - Đạt kết quả nghiệm thu tuyệt đối: `python -m lab10.grade --incident S3` đạt **`PASS-VISIBLE`** với pass rate 1.0 (sạch toàn bộ 10 lỗi phạt oan hãng, 0đ hoàn sai, 0 lộ PII, 0 lỗi hồi quy trên bộ nền regression).
- Hoàn thiện tài liệu kỹ thuật Phiếu C: Điền chuẩn xác các mục HAZOP (C4), Fault Tree trước và sau khi sửa (C6, C9), Bảng ánh xạ nguyên nhân - chỗ sửa (C7) và đăng ký monitor (C8).

### Bằng chứng
- Commit thiết kế metric offline: `372b90e` / `67c0d79` (`offline metrics 1.3`)
- Commit code cổng vòng 1 & báo cáo: `3d397ac` (`code guard & report`) và `c305c0f` (khóa cổng vòng 1 hash `20772891`)
- Commit sửa cổng sự cố S3 & thêm monitor: `2e9064e` (`feat(S3): complete gate engineer tasks, fix strikes cap, add monitors, pass grade`)
- Commit hoàn thiện hồ sơ kỹ thuật Phiếu C: `118aa94` (`docs(form-c): complete sections C4, C6, C7, C9, and C11 based on S3 evaluation results`)
- Mã lần chạy: `R-base-before-20261119-155008-bde05c` (base), `R-S3-prepared-20261119-163907-0d991c` (prepared), `R-base-after-20261119-161405-e53c4d` (regression pass 1.0), `R-S3-after-20261119-170818-1dd43a` (after pass 1.0), `R-S3-grade-20261119-170817-1dd43a` (grade `PASS-VISIBLE`).

### Exit ticket
- Một điều học được: Không bao giờ phụ thuộc hoàn toàn vào output hay prompt của mô hình ngôn ngữ lớn (LLM) để đảm bảo an toàn nghiệp vụ. Các ràng buộc cốt lõi (tiền bạc, dữ liệu cá nhân, chế tài đối tác) bắt buộc phải được bọc trong các lớp cổng bảo vệ cứng (Guards) ở tầng lệnh ghi (`write_gate`) và kiểm soát bằng các trần vận hành cụ thể.
- Một điều còn chưa chắc: Trong môi trường triển khai thực tế, nếu dữ liệu tracking đầu vào từ hiện trường kho bãi bị gián đoạn hoặc bị bưu tá nhập sai mã nguyên nhân trễ ngay từ thiết bị quét cầm tay trước khi lưu vào DB, thì các cổng phần mềm vẫn có nguy cơ bị qua mặt (garbage in, garbage out); cần thiết lập thêm kênh telemetry phát hiện sớm độ trễ nhập liệu (lag time) giữa thực địa và hệ thống.

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
