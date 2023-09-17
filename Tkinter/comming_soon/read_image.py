import cv2
import sqlite3
# Đọc dữ liệu từ file nhị phân và gán vào biến
with open('image001.jpg', 'rb') as file:
    blob_data = file.read()
# Lưu dữ liệu vào cơ sở dữ liệu SQLite
conn = sqlite3.connect('Data.db')
cursor = conn.cursor()
# Tạo bảng để lưu trữ dữ liệu blob
cursor.execute('''CREATE TABLE IF NOT EXISTS images
                  (id INTEGER PRIMARY KEY,
                  image BLOB)''')

# Chèn dữ liệu blob vào bảng
cursor.execute("INSERT INTO images (image) VALUES (?)", (blob_data,))

# Lưu thay đổi và đóng kết nối
conn.commit()
conn.close()
