import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

qr = pyqrcode.create("www.google.com")
qr.png("google.png",scale=8)

d = decode(Image.open("google.png"))
print(d[0].data.decode("ascii"))