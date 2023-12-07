# Barcode Creator
### I need bar codes to scan!

And that is the truth. I'm working on a different project where I realized that I needed unique barcodes. I found 
python-barcode and decided to make my own barcode creator. 

It was fun to make and has all the features I need for my other project. If you need EAN13 barcodes or a base to build
your own barcode creator, feel free to clone and have fun. 

## Dependencies
### Local Development

Make sure you have Python3 and pip installed.

#### Python 3.7

[python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

Instructions for setting up your virual enviornment:\
[Virtual Enviornment docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup 
```bash
python3 -m venv .venv
```

and running 
```bash
source .venv/bin/activate
```

install dependencies by running:
```bash
pip install -r requirements.txt
```

This will install all of the required packages listed in the `requirements.txt` file.

#### Key Dependencies

[python-barcode](https://python-barcode.readthedocs.io/en/stable/) is a pure-python library for generating barcodes in various formats. It’s 100% pure python.

[Pillow](https://python-pillow.org/) is required for generating images (e.g.: PNGs).

## Using the Application

#### Running app
```bash
python3 app.py
```
