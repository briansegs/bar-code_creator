"Creates a EAN13 bar code"
from barcodeCreator import BarcodeCreator
from data import data

# TODO: Add print statments to promt steps
# TODO: Make a version of the app and class that will work without the json
# and saves the barcode to the root dir (default for EAN13().save())
# This version will be for the public. More user friendly

print("Let's create an EAN13 barcode.")

options = data["options"]
barcodeOption = ""

while barcodeOption not in options:
    print("Options:")
    for num, option in options.items():
        print(f'{num}. {option}')
    barcodeOption = input(">>> ")

    if barcodeOption == "1":
        while True:
            print("Enter your 13 digit number.")
            customNum = input(">>> ")
            if len(customNum) == 13 and customNum.isnumeric():
                break
            print(f'Error: "{customNum}" is not a 13 digit number.')
        print("Creating barcode...")
        barcodeBot = BarcodeCreator()
        barcodeBot.setCustomNumStr(customNum)
        barcodeBot.saveBarcode()

    elif barcodeOption == "2":
        print("Creating a random 13 digit barcode...")
        barcodeBot = BarcodeCreator()
        barcodeBot.setRandomNumStr()
        barcodeBot.saveBarcode()

    # TODO: add option 3
    # TODO: Add option to edit prefix or use default (expose default)
    else:
        print(f'Error: "{barcodeOption}" is not an option.')
