import sqlite3

# Kết nối đến cơ sở dữ liệu SQLite
conn = sqlite3.connect('Data.db')

# Tạo một đối tượng cursor để thao tác với cơ sở dữ liệu
cursor = conn.cursor()

# Thực hiện các câu truy vấn và tương tác với cơ sở dữ liệu
# Ví dụ: Tạo bảng
cursor.execute('''CREATE TABLE IF NOT EXISTS thong_tin
                  (ID INTEGER PRIMARY KEY,
                  Name_ TEXT,
                  Another_Name TEXT,
                  Science_Name TEXT,
                  Surname TEXT,
                  Parts_used TEXT,
                  Function_Dominion TEXT,
                  Dosage_and_usage TEXT)''')

# Thêm dữ liệu vào bảng
cursor.execute("INSERT INTO thong_tin VALUES (1, 'Ké Đầu Ngựa', 'Thương nhĩ', 'Xanthium strumarium L.', 'Cúc (Asteraceae)', 'Quả già', 'Tiêu độc, sát trùng, tán phong thông khiếu, trừ thấp. Chữa phong hàn, đau đầu, chân tay co rút, đau khớp, mũi chảy nước hôi, mày đay, lở ngứa, tràng nhạc, mụn nhọt, mẩn ngứa', 'Ngày dùng 6 - 12g, sắc uống')")

# Lưu thay đổi và đóng kết nối với cơ sở dữ liệu
conn.commit()
conn.close()
