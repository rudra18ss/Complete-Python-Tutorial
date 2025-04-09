#This is QR code Generator using python

import qrcode as qr
img = qr.make('https://www.instagram.com/rudra18s/')
img.save('instagram.png')
