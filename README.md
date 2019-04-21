# QRCode

A simple tool to generate QRCodes in python.

## Setup
You should set a virtual enviromment:
```shell
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
You can also run without the virtual enviromment:
```shell
$ pip install Image
$ pip install pyqrcode
```
## Run
### Without files
You can run the QRCode generator by typing into your shell:
``` shell
$ python3 qrcode.py 
``` 
There is multiple options to run:
```console
--c Content to generate QRCode.
--o Name of the outpufile
--i Image name
--logo 0 if you don't want to add a logo, 1 otherwise. (default 0)
```

### Read from files
You can run the QRCode generator by typing into your shell:
``` shell
$ python3 raedFromFile.py --file "Path to the file"
```

### Output

#### Simple QRCode / QRCode with logo
<img src="https://github.com/user-cube/QRCode/blob/master/qrcode.png?raw=true" alt="simple qrcode" width="200" height="200"/><img src="https://github.com/user-cube/QRCode/blob/master/QRCodeLogo.png?raw=true" alt="simple qrcode" width="200" height="200"/>

