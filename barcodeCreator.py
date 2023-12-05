"Bar Code Creator Class"
from random import randint
from barcode import EAN13
from barcode.writer import ImageWriter
from data import data

class BarcodeCreator:
    "Creates barcodes and saves them to a local folder"
    folder = data["folder_path"]
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

    def saveBarcode(self):
        "saves the barcode to a local folder"
        barCode = EAN13(self.numStr, writer=ImageWriter())
        barCode.save(self.folder + "/" + str(barCode))
        print(f'Created bar-code: {barCode} in {self.folder}')
