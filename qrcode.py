import pyqrcode
import argparse
import os
from PIL import Image

"""
Function that generates the simple QRCode.
"""
def generateQR():
    url = pyqrcode.QRCode(CONTENT,error = 'H')
    url.png("int.png",scale=100)

"""
Add logo to the center of a pre-generated QRCode.
"""
def addImage():
    img = Image.open("int.png")
    img = img.convert("RGBA")

    try:
        logo = Image.open(IMAGE)
    except:
        print(IMAGE + " not found")
        
    width, height = img.size
    logo_size = 700
    
    xmin = ymin = int((width / 2) - (logo_size / 2))
    xmax = ymax = int((width / 2) + (logo_size / 2))

    # resize the logo as calculated
    logo = logo.resize((xmax - xmin, ymax - ymin))

    #put the logo in the qr code
    img.paste(logo, (xmin, ymin, xmax, ymax))
    img.save(OUTPUT) 
    os.remove("int.png")

"""
Menu function with options validation.
"""
def menu():        
    if ( LOGO == 0 ):
        generateQR()
    else:
        generateQR()
        addImage()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--c", help="Content to generate QRCode.", default="404")
    parser.add_argument("--o", help="Name of the outpufile", default="qrcode.png")
    parser.add_argument("--i", help="Image name", default="image.png")
    parser.add_argument("--logo", help="0 if you don't want to add a logo, 1 otherwise.", default=0)
    args = parser.parse_args()
    CONTENT = args.c
    LOGO = args.logo
    OUTPUT = args.o
    IMAGE = args.i
    menu()

