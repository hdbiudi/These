import qrcode
from PIL import Image

# Tạo QR code
data = "https://19009165.com/"
color = "#66A646"  # 'cyan' "#1e8f45"
background = "white"
# Đường dẫn tới file logo
logo_path = "CreateQRcode/20230609-101714.png"

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=40,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Tạo hình ảnh QR code
qr_image = qr.make_image(fill_color=color, back_color=background)
qr_image = qr_image.convert("RGBA")

# Đọc file logo
logo_image = Image.open(logo_path)

# Kích thước của QR code
qr_size = qr_image.size

# Kích thước của logo (giảm kích thước logo nếu quá lớn)
logo_size = (qr_size[0] // 6, qr_size[1] // 6)
logo_image = logo_image.resize(logo_size, resample=Image.LANCZOS)

# Tính toán vị trí trung tâm để chèn logo vào
logo_position = ((qr_size[0] - logo_size[0]) // 2, (qr_size[1] - logo_size[1]) // 2)

# Chèn logo vào hình ảnh QR code
qr_image.paste(logo_image, logo_position, logo_image)

# Lưu hình ảnh QR code với logo
qr_image.save("CreateQRcode/qrcode_with_logo.png")
