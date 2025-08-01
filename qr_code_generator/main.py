import qrcode

data = input('Enter The Website URL: ')
file_name = input('Enter the file name: ')
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
img = qr.make_image(fill_color="black", back_color="white")
img.save(file_name)
print(f'QR Code save as file name {file_name}')

