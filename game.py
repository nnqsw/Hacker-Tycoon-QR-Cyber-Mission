# ===============================================
# game.py
# ===============================================
from qr_system import create_qr, read_qr
import time


# ================================
# LEVEL 0 — Quét QR để lấy username + IP
# ================================
def level0():
    print("\n=== LEVEL 0: QR Recon ===")

    qr_data = "user=admin;ip=10.0.0.55"

    # Hiển thị QR lên terminal
    create_qr(qr_data)

    # Người chơi nhập lệnh
    cmd = input("Nhập lệnh (scan_qr): ").strip()

    if cmd != "scan_qr":
        print("❌ Sai lệnh!")
        return None

    # Quét QR (trả thẳng text)
    data = read_qr(qr_data)

    # Tách IP + username
    parts = dict(pair.split("=") for pair in data.split(";"))
    user = parts["user"]
    ip = parts["ip"]

    print(f"✔ Username: {user}\n✔ IP: {ip}\n")
    return {"user": user, "ip": ip}


# ================================
# LEVEL 1 — SSH Giả Lập
# ================================
def level1(info):
    print("\n=== LEVEL 1: SSH vào server ===")
    print("Dùng thông tin tìm được từ mã QR để SSH.")

    correct_cmd = f"ssh {info['user']}@{info['ip']}"
    cmd = input("Nhập lệnh SSH: ").strip()

    if cmd == correct_cmd:
        print("Đang kết nối...\n✔ Kết nối thành công!\n")
        return True

    print("❌ Sai lệnh. Gợi ý:", correct_cmd)
    return False


# ================================
# LEVEL 2 — Ping xuất hiện IP lạ
# ================================
def level2():
    print("=== LEVEL 2: Kiểm tra kết nối mạng ===")

    main_ip = "192.168.56.10"
    secret_ip = "10.0.0.7"

    print(f"Đang ping {main_ip}...\n")
    time.sleep(1)

    for _ in range(3):
        print(f"Reply from {main_ip}: bytes=32 time=2ms TTL=64")
        time.sleep(0.3)

    print(f"⚠ Reply from {secret_ip}: bytes=32 time=3ms TTL=64  (gói tin bất thường!)")
    time.sleep(0.4)

    for _ in range(2):
        print(f"Reply from {main_ip}: bytes=32 time=2ms TTL=64")
        time.sleep(0.3)

    print("\nCó vẻ có **gói tin từ IP lạ**…")
    print("Chuyển sang Level 3 để điều tra.\n")
    time.sleep(1)

    return secret_ip


# ================================
# LEVEL 3 — Connect <IP lạ> & KEY
# ================================
def level3(secret_ip):
    print("=== LEVEL 3: Truy cập server bí ẩn ===")
    print("Bạn đã phát hiện một IP lạ ở Level 2.")
    print("Hãy thử kết nối vào nó để xem chứa gì.\n")

    cmd = input(f"Nhập lệnh (connect {secret_ip}): ").strip()

    if cmd != f"connect {secret_ip}":
        print("❌ Không thể kết nối. Sai lệnh.")
        return False

    print("\nĐang kết nối tới server...")
    time.sleep(1)

    print("\n--- SERVER BANNER ---")
    print("HIDDEN SERVICE v1.07")
    print("KEY: N2QSW-65132875")
    print("----------------------\n")

    key = input("Nhập KEY để xác thực: ").strip()
    if key == "N2QSW-65132875":
        print("✔ Xác thực thành công! Qua Level 3.\n")
        return True

    print("❌ KEY sai!")
    return False


# ================================
# LEVEL 4 — Hacker Grid Decode
# ================================
def level4():
    print("=== LEVEL 4: Hacker Grid Decode ===")

    key_input = input("Nhập KEY: ").strip()
    if key_input != "N2QSW-65132875":
        print("❌ KEY sai.")
        return False

    print("\nHacker Grid (tín hiệu mã hóa):")
    print(
        """
█ ░ █ ░ █
░ █ ░ █ ░
█ ░ █ ░ █
░ █ ░ █ ░
█ ░ █ ░ █
"""
    )

    freq = input("Giải ra tần số (ví dụ: 21): ").strip()
    if freq == "21":
        print("✔ Giải mã thành công! Chuyển sang Level 5...\n")
        return True

    print("❌ Sai tần số.")
    return False


# ================================
# LEVEL 5 — Cú Lừa Hacker
# ================================
def level5():
    print("=== LEVEL 5: FINAL ACCESS ===")
    print("Đang mở khóa hệ thống tối mật...\n")
    time.sleep(1)
    print(">>> Kiểm tra kỹ năng hacker…")
    time.sleep(1)
    print(">>> Phân tích năng lực khai thác…")
    time.sleep(1)
    print(">>> Xác minh trình độ chuyên môn…")
    time.sleep(1)
    print("\nKẾT QUẢ: ❌ THẤT BẠI\n")
    print("Bạn còn non và xanh lắm…")
    print("Hãy luyện thêm kỹ năng rồi quay lại phá đảo hệ thống thật.")
    print("Mission Failed – nhưng đó chỉ là khởi đầu.\n")
    return True


# ================================
# START GAME
# ================================
def start_game():
    input("Nhấn Enter để bắt đầu game...")

    banner = r"""
 /$$   /$$                     /$$                                 /$$$$$$$$                                                     
| $$  | $$                    | $$                                |__  $$__/                                                     
| $$  | $$  /$$$$$$   /$$$$$$$| $$   /$$  /$$$$$$   /$$$$$$          | $$ /$$   /$$  /$$$$$$$  /$$$$$$   /$$$$$$  /$$$$$$$       
| $$$$$$$$ |____  $$ /$$_____/| $$  /$$/ /$$__  $$ /$$__  $$         | $$| $$  | $$ /$$_____/ /$$__  $$ /$$__  $$| $$__  $$      
| $$__  $$  /$$$$$$$| $$      | $$$$$$/ | $$$$$$$$| $$  \__/         | $$| $$  | $$| $$      | $$  \ $$| $$  \ $$| $$  \ $$      
| $$  | $$ /$$__  $$| $$      | $$_  $$ | $$_____/| $$               | $$| $$  | $$| $$      | $$  | $$| $$  | $$| $$  | $$      
| $$  | $$|  $$$$$$$|  $$$$$$$| $$ \  $$|  $$$$$$$| $$               | $$|  $$$$$$$|  $$$$$$$|  $$$$$$/|  $$$$$$/| $$  | $$      
|__/  |__/ \_______/ \_______/|__/  \__/ \_______/|__/               |__/ \____  $$ \_______/ \______/  \______/ |__/  |__/      
                                                                          /$$  | $$                                              
                                                                         |  $$$$$$/                                              
                                                                          \______/                                               

        SWN2Q
    """
    print(banner)
    time.sleep(1)

    info = level0()
    if not info:
        return

    if not level1(info):
        return

    secret_ip = level2()
    if not secret_ip:
        return

    if not level3(secret_ip):
        return

    if not level4():
        return

    if not level5():
        return

    print("\n🎉 CHÚC MỪNG — BẠN ĐÃ PHÁ ĐẢO GAME 🎉")


# ================================
# CHẠY GAME CHỈ KHI RUN FILE TRỰC TIẾP
# ================================
if __name__ == "__main__":
    start_game()
