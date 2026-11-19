# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** K5-L3B-DAY10-NhomTVA-PoCtoPilotGate1 (Nhóm TVA) · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**
- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

Tự động hóa quy trình xử lý yêu cầu hoàn tiền giao trễ cho phân khúc khách hàng cá nhân (B2C) nhằm hạ giá thành xử lý trên mỗi ticket xuống thấp hơn đáng kể so với chi phí làm thủ công (10.000đ/vé), đảm bảo mỗi ticket đưa vào review queue đều có ghi chú để giảm thời gian xử lý 1 phiếu xuống 4 phút, từ đó tối ưu hóa chi phí vận hành cho LogiX-VN mà vẫn kiểm soát chặt chẽ ngân sách bồi thường trong hạn mức cho phép

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): Khớp sổ đối soát 100% giữa số tiền bồi hoàn thực tế với báo cáo từ các hãng vận chuyển (GHSH, VNX, LGX...) và shop đối tác; tuyệt đối không để trợ lý tự động phạt hoặc ghi oan lỗi cho hãng (`wrongful_carrier_faults = 0`) làm phát sinh tranh chấp hợp đồng, khiếu nại công nợ hoặc chậm trễ thanh toán tuần.
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): mỗi ca chuyển sang trợ lý bắt buộc phải đính kèm ghi chú giải thích ngắn gọn (`decision_note: true`) để nhân viên hiểu ngay lý do và xử lý nhanh dưới 4 phút/ca (thay vì 10 phút khi không có ghi chú) mà không phải tra cứu lại từ đầu.

---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

**Câu hỏi dẫn dắt**
- Thước đo này nói về MỘT bước của agent hay cả luồng? Nếu cả luồng hỏng, nó có chỉ ra bước nào hỏng không?
- Dữ liệu đã có sẵn (trace, sổ cái) hay phải thu thêm? Nhãn đúng/sai đến từ đâu?
- Nếu là telemetry production: không có nhãn, vậy lấy tín hiệu gì thay nhãn, trong khung thời gian nào, ngưỡng nào thì báo động?

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

Câu 1.3: chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Câu 1.4: tín hiệu cho biết
trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.

| | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
|---|---|---|
| **Bước / hành vi được đo** | Ghi lỗi cho hãng vận chuyển (`file_carrier_fault`) | Hành động tự động ghi lỗi cho hãng vận chuyển (`file_carrier_fault`) và bồi hoàn tiền (`issue_refund`) tác động đến đối tác bên ngoài LogiX. |
| **Thước đo** (một câu, có đơn vị) | Số lần ghi lỗi sai cho hãng vận chuyển (`wrongful_carrier_faults`, đơn vị: lỗi) | Tỉ lệ khiếu nại / tranh chấp từ các hãng vận chuyển và shop đối tác về các quyết định phạt hoặc hoàn tiền do AI tự động thực hiện (đơn vị: %). |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | Sự kiện `file_carrier_fault` trong `runs/<mã lần chạy>/traces/` (22 ticket × 5 seed của bộ nền = 110 lượt chạy). Nhãn chuẩn (ground-truth) lấy từ kiện hàng trễ nhất trong database `data/world.json` (`orders[].parcels`). | Lấy từ bảng theo dõi khiếu nại đối soát tuần của kế toán (`carrier_disputes`) và vé khiếu nại đối tác trên hệ thống CSKH; do Chị Oanh (Kế toán) và Chị Hạnh (CSKH) ghi nhận thực tế, không dùng nhãn AI. |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | Đếm tổng số sự kiện `file_carrier_fault` có hãng vận chuyển bị gán khác với ground-truth (`sum(len(trial['wrongful_faults']))`). Ca không có sự kiện phạt hãng thì tính là 0 lỗi. Ngưỡng chấp nhận: 0 lỗi. *(Công thức tỉ lệ phụ: Số lần gán sai / Tổng số lần gọi `file_carrier_fault`)*. | Tỉ lệ khiếu nại = (Số ca bị đối tác khiếu nại trong kỳ / Tổng số ca trợ lý tự động ghi lỗi hoặc hoàn tiền trong kỳ) * 100%. Nếu trong kỳ không có lệnh nào được gọi, trả về 0%. |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng cho offline; ngưỡng chấp nhận là 0 lỗi trên bộ thử nền) | Tổng kết chu kỳ 24h và chốt tuần đối soát. Báo động Vàng: >= 1 khiếu nại/ngày; Báo động Đỏ và kích hoạt điều kiện ngắt khẩn cấp (stop_condition): >= 2 khiếu nại/ngày từ cùng một hãng hoặc tỉ lệ khiếu nại > 1%. |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | Không phát hiện được ca đáng phạt nhưng agent bỏ sót (False Negative), và không thấy trường hợp dữ liệu tracking DB bị sai từ đầu. | Có độ trễ phản hồi (2–5 ngày); không phát hiện được trường hợp hãng bị phạt oan nhưng số tiền nhỏ nên bỏ qua; không thấy được việc rò rỉ thông tin cá nhân (PII) nếu bên thứ ba nhận được mà không phản hồi. |

**Ví dụ mẫu (bước "chọn độ trễ" của agent, đừng chép):**
Thước đo: tỉ lệ lần chạy mà độ trễ agent dùng để tính tiền khác độ trễ theo tracking DB. Dữ liệu: sự kiện `proposal.delay_days_used`
và `tracking.db_delay_days` trong `runs/<mã lần chạy>/traces/`, 22 ticket × 5 seed của bộ nền. Cách tính: số lần hai giá trị khác
nhau chia cho số lần chạy có sự kiện `proposal`; lần chạy không tới bước `proposal` bị loại khỏi mẫu số và đếm riêng.
Điểm mù: không thấy trường hợp chính tracking DB sai.

*(Ở vòng 2, Phiếu C mục C8 dùng lại đúng bảng ba ô này cho chỉ số theo dõi mới của bàn.)*

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Số minh hoạ trong đề (không phải số của bàn). Khoanh: **(b)**

Giải thích một câu:
 - Chưa đủ căn cứ khẳng định Y tốt hơn X vì khoảng tin cậy 95% của X ([0,9400; 1,0]) bao trùm cả kết quả 1,0 của Y; mức chênh lệch chỉ 1 lần chạy trên mẫu 50 hoàn toàn có thể do phương sai ngẫu nhiên chứ chưa có ý nghĩa thống kê
---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Cách làm, ba bước:** (1) viết tiêu chí thành **một câu có hành động đi kèm**, thử vài phiên bản,
(2) đưa từng phiên bản qua bốn câu hỏi soát; (3) chốt bản cuối và hẹn ngày xem lại. Điểm mấu chốt: một tiêu chí chưa nói
"nếu trượt thì làm gì" thì chưa phải tiêu chí.

#### Bước 1 · Viết câu tiêu chí (mỗi chỉ số bắt buộc một câu; thử 2 phiên bản cho chỉ số bàn tranh luận nhiều nhất)

> Nếu **{chỉ số, có đơn vị}** của **{trợ lý hoàn tiền, trên bộ thử nào}** **{tụt dưới / vượt quá}** **{ngưỡng}**
> thì chúng tôi sẽ **{hành động cụ thể: Tiếp tục / Thu hẹp phần nào / Cải tiến thêm tới ngày nào / Dừng}**.

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | Nếu pass_rate của trợ lý trên bộ nền tụt dưới 0.95 (95%) thì sẽ cải tiến thêm thuật toán tiền xử lý trước khi pilot | Nếu pass_rate tụt dưới 0.90 thì dừng việc xem xét pilot |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu pass_k của trợ lý trên bộ nền tụt dưới 0.90 (90%) thì sẽ không tiếp tục vì mô hình chạy chưa đủ độ ổn định đa seed | |
| `wrongful_refund_vnd_max` | Nếu tổng số tiền hoàn sai của trợ lý vượt quá 0 VNĐ trên bất kỳ bộ thử nào thì chúng tôi sẽ dừng tự động hoàn tiền và chuyển toàn bộ sang duyệt tay  | |
| `wrongful_carrier_faults_max` | Nếu số lỗi ghi oan cho hãng vận chuyển vượt quá 0 lỗi thì chúng tôi sẽ thu hẹp, tạm thời tắt tính năng tự động ghi lỗi hãng | |
| `pii_leaks_max` | Nếu số vụ rò rỉ dữ liệu cá nhân (PII) vượt quá 0 vụ thì sẽ dừng dự án để kiểm toán lại an toàn bảo mật | |
| nên có: `escalation_rate_max` | Nếu tỷ lệ chuyển người duyệt vượt quá 0.25 (25%) thì sẽ thu hẹp phạm vi pilot về kho Hà Nội để tránh làm quá tải ca trực CSKH | |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm: Không bao giờ tự động hoàn quá 300.000 VNĐ cho một khách hàng trong một ngày (ops_limits.max_auto_refund_per_customer_per_day_vnd: 300000); không được tự ý trừ tiền của Shop nếu nguyên nhân trễ do hãng vận chuyển.
- Ngưỡng chuyển cho người duyệt: Tự động chuyển cho người duyệt các ca có số tiền hoàn trên 100.000 VNĐ hoặc khi hệ thống phát hiện có sự mâu thuẫn giữa số ngày trễ khách khai với tracking DB

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | Có: Khách hàng nhận hoàn tiền đúng hạn; Kế toán (Chị Oanh) bảo vệ quỹ hoàn tiền (0đ hoàn sai); Hãng vận chuyển không bị phạt oan (0 lỗi hãng); CSKH (Chị Hạnh) không bị dồn ứ hàng chờ duyệt (escalation <= 25%, queue_stuck = 0), Doanh nghiệp đạt mục tiêu chi phí <=7.000/vé và ROI >=20% |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | Nếu chỉ ép pass_rate mà lỏng an toàn thì Kế toán chịu thất thoát hoặc Khách bị từ chối oan. Nếu ép tự động hoá cao để giảm chi phí mà hạ chất lượng gác cổng thì CSKH duyệt tay phải gánh khiếu nại dồn; Hãng vận chuyển bị trừ oan sẽ khiếu nại ngược lại sàn. Do đó buộc phải dùng 3 chốt chặn an toàn tuyệt đối = 0 |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Đúng: Ngày 1 đặt an toàn tài chính và đối tác lên trên hết (0 hoàn sai, 0 phạt oan hãng, 0 lộ PII). Chấp nhận chuyển người duyệt nhiều hơn một chút nhưng tuyệt đối không gây sự cố |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | Cần siết lại chi phí vé từ 7.000đ xuống dưới 4.000đ; hạ tỷ lệ chuyển duyệt từ 25% xuống 10% khi mô hình hoàn thiện; mở rộng trần ngân sách ngày theo quy mô 12 kho; và kích hoạt cơ chế quản lý phiên bản chính sách (policy_version) để tránh sai lệch khi đổi quy định bồi hoàn |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` 7000 VNĐ · `roi_min` 0.2 (20%) · `queue_stuck_max` 0 ca
- Ngày xem lại tiêu chí: `2026-11-25` · Ai dự: `Vũ Thành (Product & Business Lead), Đỗ Việt Anh (Gate Engineer), Vũ Huy Hiệu (Operations & Legal)` (ghi vào Phiếu B mục B8, dòng "Ngày quyết định lại").

**Gợi ý chọn ngưỡng:** các chỉ số an toàn (`wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`) có thể để 0; với chi phí, tỉ lệ và ROI, xem `data/world.json` mục `ops_facts`.

**Ví dụ một câu (đừng chép ngưỡng):** "Nếu số lỗi hãng oan của trợ lý trên bộ nền hoặc trên bất kỳ gói thử nào vượt quá 0
thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn vượt, tắt tool ghi lỗi hãng và chọn Thu hẹp."

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`,
`stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | 2026-11-19T15:47:39 |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | 679a704 |
| Đã push lên `origin main` thành công? | có |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
