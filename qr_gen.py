import qrcode
# first we take input from the user in form of url
# and we also use strip method to correct any space mistake from user end
'''
data = input("enter the text or URL:\n").strip()
filename = input("enter filename:\n").strip()
img = qrcode.make(data)
img.save(f"{filename}.png")           # this is a quick way to create qr code
print("qr code generate and saved")
'''
# this is a detailed way to generae qr code :

data = input("enter the text or URL:\n").strip()
filename = input("enter filename:\n").strip()
# qrcode.QRCode() creates a qr code object
qr = qrcode.QRCode(version = 1, #1-40 controls size of qr code
                    #version 1 means 21*21 boxes
                   box_size = 10, #pixels per box
                   border = 4,#border width(min is 4)
)
qr.add_data(data) #this adds actual info like text,phone no. ,urls
img = qr.make_image(fill_color = "black", back_color="white")#Converts the QR code into an image (PIL Image object).
qr.make(fit=True)# Finalizes the QR code after adding data.
# fit=True automatically chooses the smallest version that fits the data.
img.save(f"{filename}.png")
print("qr code saved!!")