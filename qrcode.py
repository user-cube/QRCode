import pyqrcode
from PIL import Image

"""
Function that generates the simple QRCode.

Parameters
-----
linkToWebsite - Link to the Webiste that will be
                stored at QRCode.
"""
def generateQR(linkToWebsite):
    url = pyqrcode.QRCode(linkToWebsite,error = 'H')
    url.png('qrcode.png',scale=50)

"""
Add logo to the center of a pre-generated QRCode.

Parameters
-----
imageName - The image name to add to the QRCode.

"""
def addImage(imageName):
    img = Image.open('qrcode.png')
    img = img.convert("RGBA")
    logo = Image.open(imageName)

    width, height = img.size
    logo_size = 500
    
    xmin = ymin = int((width / 2) - (logo_size / 2))
    xmax = ymax = int((width / 2) + (logo_size / 2))

    # resize the logo as calculated
    logo = logo.resize((xmax - xmin, ymax - ymin))

    #put the logo in the qr code
    img.paste(logo, (xmin, ymin, xmax, ymax))
    img.save("QRCodeLogo.png") 

"""
Menu function with options validation.

"""
def menu():
    print(" [2] - Generate QRCode with logo\n [1] - Generate QRCode without logo\n [0] - Exit")
    
    while True:
        try:
            selector = int(input("Option: "))
            if ( selector > 2 or selector < 0 ):
                print("Option should be between 0 and 2")
            else:
                break
        except:
            print("Invalid option")
    
    if ( selector == 0 ):
        exit()
    elif ( selector == 1 ):
        linkToWebsite = input("Link: ")
        generateQR(linkToWebsite)
    else:
        linkToWebsite = input("Link: ")
        imageName = input("Logo: ")
        generateQR(linkToWebsite)
        addImage(imageName)

"""Main"""
menu()
