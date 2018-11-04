import os.path



def welcome():
    print("This program generates random text based on a document.\nGive me an input file and an 'N' value for groups\nof words, and I'll create random text for you.\n\n")


def getInput():
    fileName = input("Input file? ")
    fileLocation = 'G:/My Drive/personal/cs_projects/python_projects/madlibs/textFiles/' + fileName

    while os.path.exists(fileLocation) == False:
        print("That file does not exist. Please try again.\n")
        fileName = input("Input file? ")
        fileLocation = 'G:/My Drive/personal/cs_projects/python_projects/ngrams/textFiles/' + fileName

    textFile = open(fileLocation, "r");


def readFile(input, n):
    textFile = open(input, "r");


def main():

    welcome();
    fileLocation = getInput();
    readFile(fileLocation);


if __name__ == "__main__": main()
