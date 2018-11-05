import os.path



def welcome():
    print("This program generates random text based on a document.\nGive me an input file and an 'N' value for groups\nof words, and I'll create random text for you.\n\n")


def getInput():
    fileName = input("Input file? ")
    fileLocation = 'G:/My Drive/personal/cs_projects/python_projects/ngrams/textFiles/' + fileName

    while os.path.exists(fileLocation) == False:
        print("That file does not exist. Please try again.\n")
        fileName = input("Input file? ")
        fileLocation = 'G:/My Drive/personal/cs_projects/python_projects/ngrams/textFiles/' + fileName

    return fileLocation

def readFile(input, n):
    textFile = open(input, "r");
    myList = [];
    myDict = {};

    #make list of all words
    for line in textFile:
        for word in line.split():
            myList.append(word);

    #build ngrams map
    for i in range(len(myList)):
        dictValue = "";
        for j in range(1, n + 1):
            dictValue = dictValue + " " + myList[(i + j) % len(myList)];
        myDict[myList[i]] = dictValue;

    return myDict;





def main():

    welcome();
    fileLocation = getInput();
    n = input("How many grams? ")
    ngramDict = readFile(fileLocation, int(n));


if __name__ == "__main__": main()
