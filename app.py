"Creates a EAN13 bar code"
from time import sleep
from barcodeCreator import BarcodeCreator
from data import data, errorMsg

print("Let's create an EAN13 barcode")
sleep(1)

options = data["options"]
barcodeOption = ""

while barcodeOption not in options:

    # Prints out barcode creation options
    print("Options:")
    sleep(1)
    for num, option in options.items():
        print(f'{num}. {option}')
        sleep(1)
    barcodeOption = input(">>> ")

    # Handles when option 1 is selected
    if barcodeOption == "1":
        while True:
            print("Enter your 13 digit number.")
            sleep(.5)
            customNum = input(">>> ")
            if len(customNum) == 13 and customNum.isnumeric():
                break
            else:
                errorMsg(customNum)
                sleep(1)

        print("Creating barcode...")
        sleep(1)
        barcodeBot = BarcodeCreator()
        barcodeBot.setCustomNumStr(customNum)
        barcodeBot.saveBarcode()

    # Handles when option 2 is selected
    elif barcodeOption == "2":
        print("Creating a random 13 digit barcode...")
        sleep(1)
        barcodeBot = BarcodeCreator()
        barcodeBot.setRandomNumStr()
        barcodeBot.saveBarcode()

    # Handles when option 3 is selected
    elif barcodeOption == "3":
        barcodeBot = BarcodeCreator()
        while True:
            print("Options:")
            sleep(1)
            print(f'1. Use default prefix ({barcodeBot.prefix})')
            sleep(1)
            print("2. Input a custom 3 digit prefix")
            sleep(1)
            prefixOption = input(">>> ")

            if prefixOption == "1" or prefixOption == "2":
                break
            else:
                errorMsg(prefixOption)
                sleep(1)

        if prefixOption == "1":
            print(f'Creating a barcode with prefix "{barcodeBot.prefix}"...')
            sleep(1)
            barcodeBot.setPrefixNumStr()
            barcodeBot.saveBarcode()

        elif prefixOption == "2":
            while True:
                print("Enter 3 digit prefix number.")
                sleep(1)
                prefixNum = input(">>> ")
                if len(prefixNum) == 3 and prefixNum.isnumeric():
                    break
                else:
                    errorMsg(prefixNum)
                    sleep(1)

            barcodeBot = BarcodeCreator(prefix=prefixNum)
            print(f'Creating a barcode with prefix "{barcodeBot.prefix}"...')
            sleep(1)
            barcodeBot.setPrefixNumStr()
            barcodeBot.saveBarcode()

    else:
        errorMsg(barcodeOption)
        sleep(1)
