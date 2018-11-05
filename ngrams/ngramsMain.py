import os.path
import random


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
        dictKey = myList[i];
        for j in range(1, n - 1):
            dictKey = dictKey + " " + myList[(i + j) % len(myList)];
        newValue = myList[(i + n - 1) % len(myList)];
        if dictKey in myDict:
            curValue = myDict[dictKey];
            if newValue not in curValue:
                curValue.append(newValue);
                myDict[dictKey] = curValue;
        else:
            newKey = [];
            newKey.append(newValue);
            myDict[dictKey] = newKey;

    return myDict;

def generateStory(nGramDict, numWords):
    myStory = [];
    keys = list(nGramDict.keys());
    randStartIndex = random.randint(1, len(keys));
    randStart = keys[randStartIndex];
    myStory.append(randStart)
    currentGram = randStart;
    print(currentGram)
    for i in range(0, numWords - 1 - len(randStart)):
       currentValue = nGramDict[currentGram]
       newWordIndex = random.randint(0, len(currentValue));

       newWord = currentValue[newWordIndex];
       newWindow = currentGram[1:] + " " + newWord;
       myStory.append(newWindow);



    return myStory;




def main():

    welcome();
    fileLocation = getInput();
    nGrams = input("How many grams? ");
    numWords = input("Number of words to generate (0 to quit)? ");
    #if numWords = 0, quit
    nGramDict = readFile(fileLocation, int(nGrams));
    nGramStory = generateStory(nGramDict, int(numWords))
    print(nGramStory)

if __name__ == "__main__": main()
