🕹️ Hacker Recon Mini-Game

Một trò chơi mô phỏng kỹ năng hacker cơ bản theo phong cách CTF (Capture The Flag).
Người chơi sẽ lần lượt vượt qua các level từ quét QR, SSH, phân tích mạng, truy cập server bí ẩn cho đến giải mã tín hiệu.

📌 Giới thiệu

Dự án gồm một game chạy trên terminal với 6 level liên tiếp.
Mỗi level yêu cầu người chơi nhập đúng lệnh hoặc giải mã thông tin để tiếp tục.

Trò chơi giúp luyện tư duy logic, thao tác mô phỏng hacker và tương tác dòng lệnh.

🧬 Cấu trúc Game

Game được chạy từ file game.py và bao gồm các level sau:

🔹 Level 0 — QR Recon

Hiển thị mã QR ASCII.

Người chơi nhập lệnh scan_qr.

Trích xuất từ QR:

username = admin

ip = 10.0.0.55

🔹 Level 1 — SSH Giả Lập

Người chơi dùng thông tin thu được từ QR.

Lệnh đúng:

ssh admin@10.0.0.55

🔹 Level 2 — Mạng Xuất Hiện IP Lạ

Trò chơi mô phỏng lệnh ping.

Một IP bất thường xuất hiện:

10.0.0.7

Đây là IP cần điều tra ở level tiếp theo.

🔹 Level 3 — Hidden Server Access

Người chơi dùng lệnh:

connect 10.0.0.7


Server trả về KEY:

N2QSW-65132875


Người chơi nhập đúng KEY để vượt level.

🔹 Level 4 — Hacker Grid Decode

Nhập lại KEY.

Một bảng tín hiệu mã hóa dạng lưới được hiển thị.

Người chơi phải tìm ra tần số = 21.

🔹 Level 5 — Cú Lừa Hacker

Trò chơi kết thúc bằng một đoạn "nghiệp vụ kiểm tra kỹ năng hacker" và…
❌ Mission Failed
(vì đây chỉ là màn chơi thử, kết thúc giả lập)

▶️ Cách chạy game
Yêu cầu

Python 3.8+

Module tự viết:

qr_system.py (chứa hàm create_qr() và read_qr())

Chạy game
python game.py

📁 Cấu trúc thư mục
project/
│── game.py
│── qr_system.py
│── README.md

🧠 Các kỹ năng mô phỏng trong game
Level	Kỹ năng mô phỏng
0	Recon, đọc dữ liệu từ QR
1	SSH command & remote login
2	Network traffic analysis
3	Hidden service probing
4	Basic signal decoding
5	Social-engineering “twist”
⭐ Ghi chú

Toàn bộ game chạy trong terminal, không yêu cầu Internet.

Đây là trò chơi mô phỏng — không thực sự thực hiện SSH hay ping thật.
