"Creates a EAN13 bar code"
from barcodeCreator import BarcodeCreator
from data import data, errorMsg

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
            else:
                errorMsg(customNum)
        print("Creating barcode...")
        barcodeBot = BarcodeCreator()
        barcodeBot.setCustomNumStr(customNum)
        barcodeBot.saveBarcode()

    elif barcodeOption == "2":
        print("Creating a random 13 digit barcode...")
        barcodeBot = BarcodeCreator()
        barcodeBot.setRandomNumStr()
        barcodeBot.saveBarcode()

    elif barcodeOption == "3":
        barcodeBot = BarcodeCreator()
        while True:
            print("Options:")
            print(f'1. Use default prefix ({barcodeBot.prefix})')
            print("2. Input a custom 3 digit prefix")
            prefixOption = input(">>> ")
            if prefixOption == "1" or prefixOption == "2":
                break
            else:
                errorMsg(prefixOption)

        if prefixOption == "1":
            print(f'Creating a barcode with prefix "{barcodeBot.prefix}"...')
            barcodeBot.setPrefixNumStr()
            barcodeBot.saveBarcode()

        elif prefixOption == "2":
            while True:
                print("Enter 3 digit prefix number.")
                prefixNum = input(">>> ")
                if len(prefixNum) == 3 and prefixNum.isnumeric():
                    break
                else:
                    errorMsg(prefixNum)

            barcodeBot = BarcodeCreator(prefix=prefixNum)
            print(f'Creating a barcode with prefix "{barcodeBot.prefix}"...')
            barcodeBot.setPrefixNumStr()
            barcodeBot.saveBarcode()

    else:
        errorMsg(barcodeOption)
