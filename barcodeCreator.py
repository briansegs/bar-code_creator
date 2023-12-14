"Bar Code Creator Class"
from time import sleep
from random import randint
from barcode import EAN13
from barcode.writer import ImageWriter
from data import data, errorMsg

class BarcodeCreator:
    "Creates barcodes and saves them to a local folder"
    folder = data["output_folder"]
    defaultPrefix = data["prefix"]

    def __init__(self, prefix=defaultPrefix):
        self.prefix = prefix
        self.numStr = ""

    def setRandomNumStr(self):
        "sets the numStr variable with a random 13 digit number"
        self.numStr = str(randint(1000000000000, 9999999999999))

    def setPrefixNumStr(self):
        "sets the numStr variable with a 3 digit prefix plus a random 10 digit number"
        self.numStr = self.prefix + str(randint(1000000000, 9999999999))

    def setCustomNumStr(self, customNum):
        "sets the numStr variable with a parameter"
        self.numStr = customNum

#TODO: add feature to name output file or use barcode number or a combination of both
    def saveBarcode(self):
        "saves the barcode to a local folder"
        barCode = EAN13(self.numStr, writer=ImageWriter())
        while True:
            print("Saving file...")
            sleep(1)
            print("File naming options:")
            sleep(.5)
            print(f'1. Use barcode number "{barCode}"')
            sleep(.5)
            print("2. Use your own custom name")
            sleep(.5)
            print(f'3. Use a custom name combined with the barcode number "{barCode}"')
            saveOption = input(">>> ")
            sleep(1)
            
            if saveOption == "1" or saveOption == "2" or saveOption == "3":
                break
            else:
                errorMsg(saveOption)
                sleep(1)
        
        if saveOption == "1":
            barCode.save(self.folder + "/" + str(barCode))
        if saveOption == "2":
            
            print("Enter your file name.")
            sleep(.5)
            barName = input(">>> ")
            
            
        if saveOption == "3":
            
        print(f'Created bar-code: {barCode} in {self.folder} folder')
