"Creates a unique EAN13 bar code"
import json
from random import randint
from barcode import EAN13
from barcode.writer import ImageWriter
# TODO: turn into class and then import
# TODO: Add print statments to edit prefix or use default
# TODO: Add welcome print statment 
# TODO: Add option to give a barcode number or generate a random one
with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    file.close()

folder = data["folder_path"]

prefix = "101"

numStr = prefix + str(randint(1000000000, 9999999999))

barCode = EAN13(numStr, writer=ImageWriter())

barCode.save(folder + "/" + str(barCode))

print(f'Created bar-code: {barCode} in {folder}')
