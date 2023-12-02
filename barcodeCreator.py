"Bar Code Creator Class"
import json
from random import randint
from barcode import EAN13
from barcode.writer import ImageWriter

class BarcodeCreator:
    "Creates barcodes and saves them to a local folder"
    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        file.close()
    folder = data["folder_path"]

    def __init__(self, prefix="101"):
        self.prefix = prefix
        self.numStr = ""
        self.barCode = ""

    def setPrefix(self, prefixNum):
        "sets the prefix variable"
        self.prefix = prefixNum

    def setRandomNumStr(self):
        "sets the NumStr variable with a random 13 digit number"
        self.numStr = str(randint(1000000000000, 9999999999999))

    def setPrefixNumStr(self):
        "sets the NumStr variable with a 3 digit prefix plus a random 10 digit number"
        self.numStr = self.prefix + str(randint(1000000000, 9999999999))

    def setCustomNumStr(self, customNum):
        "sets the NumStr variable with a custom number"
        self.numStr = customNum

    def createBarcodeNum(self):
        "creates a barcode number"
        self.barCode = EAN13(self.numStr, writer=ImageWriter())

    def saveBarcode(self):
        "saves the barcode to a local folder"
        self.barCode.save(self.folder + "/" + str(self.barCode))
        print(f'Created bar-code: {self.barCode} in {self.folder}')
