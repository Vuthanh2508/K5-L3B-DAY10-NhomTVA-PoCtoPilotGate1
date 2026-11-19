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

### Đóng góp cụ thể

### Bằng chứng

### Exit ticket
