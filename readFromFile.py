import pyqrcode
import os
import argparse
from PIL import Image

def generateQR():
    try:
        file = open(FILE, "r")
        content = file.readlines()
        i=0
        for x in content:
            print(x)
            text = pyqrcode.QRCode(x, encoding="utf-8")
            text.png(str(i)+".png", scale=50)
            i+=1
    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="Name of the file with the content to generate QRCodes.", default="file.txt")
    args = parser.parse_args()
    FILE = args.file
    generateQR()
