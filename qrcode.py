import pyqrcode
from PIL import Image

def generateQR(linkToWebsite):
    url = pyqrcode.QRCode(linkToWebsite,error = 'H')
    url.png('qrcode.png',scale=10)

def addImage():
    im = Image.open('qrcode.png')
    im = im.convert("RGBA")
    logo = Image.open('NEI.png')
    box = (135,135,235,235)
    im.crop(box)
    region = logo
    region = region.resize((box[2] - box[0], box[3] - box[1]))
    im.paste(region,box)
    im.save("QRCodeLogo.png") 

def menu():
    print(" [2] - Generate code with logo\n [1] - Generate code without logo\n [0] - Exit")
    
    while True:
        try:
            selector = int(input("Option: "))
            if ( selector > 2 or selector <= 0 ):
                print("Option should be between 0 and 2")
            else:
                break
        except:
            print("Invalid option")
    
    if ( selector == "0" ):
        exit()
    elif ( selector == "1" ):
        linkToWebsite = input("Link: ")
        generateQR(linkToWebsite)
    else:
        linkToWebsite = input("Link: ")
        generateQR(linkToWebsite)
        addImage()

menu()