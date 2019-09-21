import random

dataset = open("data.txt", "w")

def generateData(numLines)
    """
    Arguments:
    numLines: Number of lines to generate

    Generates numLines strings of 30 integers in data.txt
    """
    for i in range(0, numLines):
        numString = ""
        for i in range(0, 30):
            numString += str(random.randint(0, 9))
        dataset.write(numString + "\n")
