# Barcode-Creator
### I need barcodes to scan!

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

Setup virtual environment: 
```bash
python3 -m venv .venv
```

Run virtual environment:
```bash
source .venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

This will install all of the required packages listed in the `requirements.txt` file.

#### Key Dependencies

[python-barcode](https://python-barcode.readthedocs.io/en/stable/) is a pure-python library for generating barcodes in various formats. It’s 100% pure python.

[Pillow](https://python-pillow.org/) is required for generating images (e.g.: PNGs).

## Using the Application

#### Running the app
```bash
python3 app.py
```

The app will walk you through everything you need to do. You get three options to pick from that all output a EAN13 barcode as a .png file.
1. Use your own 13 digit number
2. Generate a random 13 digit number
3. Input a 3 digit prefix followed by a random 10 digit number
    - Or use default a prefix number which can be set in the [data.py](https://github.com/briansegs/bar-code_creator/blob/8a575a86742b33e41bd73b3fc8277bdb0048f23a/data.py#L9) file

#### Outputting .png files
Steps to setup your output folder:
1. Create a folder at the root of this project (named what ever you want) 
2. Edit the "[folder_path](https://github.com/briansegs/bar-code_creator/blob/854f2c50eb913443102b9414fd08ae1e17972a37/data.py#L3)" key in the "[data](https://github.com/briansegs/bar-code_creator/blob/854f2c50eb913443102b9414fd08ae1e17972a37/data.py#L2)" dictionary that lives in the "[data.py](https://github.com/briansegs/bar-code_creator/blob/main/data.py)" file.
    - e.g.: /home/(your-system)/Documents/Programming/bar-code_creator/(png-output-file-name)
    - This is an examle from my system. The path you use has to lead to the project folder on your system.
