import qrcode

# Menü sayfasının URL'si
menu_url = 'https://abdulhamitinci.github.io/cafe-menuu/'  # URL'yi buraya ekle

# QR kodu oluştur
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(menu_url)
qr.make(fit=True)

# QR kodu resmi oluştur ve kaydet
img = qr.make_image(fill='black', back_color='white')
img.save('cafe_menu_qr_code.png')
