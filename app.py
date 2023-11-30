"Creates a unique EAN13 bar code"
from random import randint
from barcode import EAN13
from barcode.writer import ImageWriter

folder = "/home/b-man/Documents/Programming/create_bar-code/bar_codes"

prefix = "101"

numStr = prefix + str(randint(1000000000, 9999999999))

barCode = EAN13(numStr, writer=ImageWriter())

barCode.save(folder + "/" + str(barCode))

print(f'Created bar-code: {barCode} in {folder}')
