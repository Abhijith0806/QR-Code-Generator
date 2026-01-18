import qrcode
print("QR CODE GENERATOR")
website_link = input("Enter your URL : ")
q1 = int(input("Do you want to modify the QR code size ?\n"
             "1 for YES\n"
             "0 for NO\n"))
if q1 == 1:
    ver = int(input("Version(1-40) =  "))
    box = int(input("Box_size =  "))
    bor = int(input("Border = "))
    qr = qrcode.QRCode(version = ver,box_size = box,border = bor)
    qr.add_data(website_link)
    qr.make()
    img = qr.make_image(fill_color = 'black',back_color='white')
else:
    qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
    qr.add_data(website_link)
    qr.make()
    img = qr.make_image(fill_color = 'black',back_color='white')
name = input("Enter file name with extension ( .png /.jpg ) =  ")
img.save(name)
print("GENERATING.........")  
print("GENERATED SUCCESSFULLY !") 