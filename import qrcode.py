import qrcode

# Sabit QR kod için URL'nizi ekleyin
url = "https://abdulhamitinci.github.io/QRmenu/"

# QR kodunu oluştur
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# QR kodu görüntüsü oluştur ve kaydet
img = qr.make_image(fill='black', back_color='white')
img.save("menu_qr_code.png")

print("QR kodu başarıyla oluşturuldu!")
