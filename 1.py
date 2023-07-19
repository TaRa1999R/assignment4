print (" ✨ MAKING YOUR OWN QR CODE ✨ ")

import qrcode 

name = input (" Please enter your full name : ")
phone = input (" Please enter yout phone number : ")
x = name + phone

img = qrcode.make(x)
img.save (" YOUR_QR_CODE.png ")