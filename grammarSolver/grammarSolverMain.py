import os.path
import random



def getFileName():
    fileName = input("Grammar file name? ");
    fileLocation = 'G:/My Drive/personal/cs_projects/python_projects/grammarSolver/res/' + fileName

    while os.path.exists(fileLocation) == False:
        print("That file does not exist. Please try again.\n")
        fileName = input("Grammar file name? ");
        fileLocation = 'G:/My Drive/personal/cs_projects/python_projects/grammarSolver/res/' + fileName

    return fileLocation;


def buildGrammar(input):
    textFile = open(input, "r");
    myDict = {};
    for line in textFile:
        key = line.split("::=")[0];
        values = line.split("::=")[1];
        values = values.split("|");
        myDict[key] = values;
    return myDict;



def generateGrammar(grammar, symbol, text):
    if symbol not in grammar:
        text = text.append(symbol);
        return;
    else:
        grammarValues = grammar[symbol];
        randInd = random.randint(0, len(grammarValues) - 1);
        randValue = str(grammarValues[randInd]).split()
        for symbol in randValue:
            generateGrammar(grammar, symbol, text);

    return;




def main():
    fileLocation = getFileName();
    grammar = buildGrammar(fileLocation);

    symbol = 1;

    while(symbol != ""):

        symbol = input("Symbol to generate (Enter to quit)? ");
        if symbol not in grammar.keys():
            print("That symbol is not valid.\n")
            symbol = input("Symbol to generate (Enter to quit)? ");

        numSymbols = input("How many to generate? ");

        while (numSymbols.isdigit() == False):
            print("That input was not a number.\n");
            numSymbols = input("How many to generate? ");

        for i in range(int(numSymbols)):
            text = [];
            generateGrammar(grammar, symbol, text);
            grammarStory = ' '.join(text);
            print(str(i) + '. ' + grammarStory + '\n');



if __name__ == "__main__": main()