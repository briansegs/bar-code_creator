"App data"
from time import sleep

data = {
    "output_folder" : "barcodes",
    "options" : {
        "1" : "Use your own 13 digit number",
        "2" : "Generate a random 13 digit number",
        "3" : "Input a 3 digit prefix followed by a random 10 digit number"
    },
    "prefix" : "101"
}

def errorMsg(error):
    "returns a generic input error"
    errorStr = print(f'Input error: "{error}" is an invalid input.')
    return errorStr

def getFileName():
    "returns fileName"
    while True:
        print("Enter your file name.")
        sleep(.5)
        fileName = input(">>> ")
        sleep(1)
        isCorrect = ""
        while isCorrect.lower() != "y" and isCorrect.lower() != "n":
            print(f'If name "{fileName}" is correct enter "Y" else enter "N".')
            sleep(.5)
            isCorrect = input(">>> ")
            sleep(1)
            if isCorrect.lower() != "y" and isCorrect.lower() != "n":
                errorMsg(isCorrect)
                sleep(1)
        if isCorrect.lower() == "y":
            break
        elif isCorrect.lower() == "n":
            pass
    return fileName
