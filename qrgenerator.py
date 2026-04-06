import qrcode
data = input("enter the text or url:").strip()
file_name = input("enter the file name: ").strip()
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_colour='black', back_colour='white')
image.save(f"{file_name}.png")
print(f'QR code saved as {file_name})')
