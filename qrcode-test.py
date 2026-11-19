import qrcode

def generate_qrcode(text):
    qr = qrcode.QRCode(
        version = 1,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="yellow",back_color="red")
    img.save("qrcode.png")

generate_qrcode("https://varzesh3.ir")
