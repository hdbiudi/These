import sqlite3
import time

def hien_thi_dong_tu_tu(dong, toc_do):
    for char in dong:
        print(char, end='', flush=True)
        time.sleep(toc_do)
    print()

def hien_thi_info_tu_tu(info, toc_do):
    dong_info = info.split('\n')
    for dong in dong_info:
        hien_thi_dong_tu_tu(dong, toc_do)

# Kết nối với cơ sở dữ liệu SQLite
conn = sqlite3.connect('Data.db')
cursor = conn.cursor()

# Truy vấn dữ liệu từ cơ sở dữ liệu
cursor.execute("SELECT * FROM thong_tin WHERE id = 1")
# Fetchall để lấy tất cả các dòng kết quả từ câu truy vấn

row = cursor.fetchone()

# Lấy thông tin từ kết quả truy vấn
Name_ = row[1]
Another_Name = row[2]
Science_Name = row[3]
Surname = row[4]
Parts_used = row[5]
Function_Dominion = row[6]
Dosage_and_usage = row[7]

# Đóng kết nối với cơ sở dữ liệu
cursor.close()
conn.close()

# Tạo thông tin cây thuốc
info = f"Tên khác: {Name_}\nTên Khác: {Another_Name}\nTên khoa học: {Science_Name}\nHọ: {Surname}\nBộ phận dùng: {Parts_used}\nCông năng, chủ trị: {Function_Dominion}\nLiều lượng, cách dùng: {Dosage_and_usage}\n"

# Gọi hàm để hiển thị thông tin từng dòng
hien_thi_info_tu_tu(info, 0.05)  # Tốc độ là 0.1 giây mỗi ký tự
