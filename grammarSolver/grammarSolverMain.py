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
        text = text + symbol;
        return text;
    else:
        print(symbol)
        values = grammar[symbol];
        values = values.split()
        for symbol in values:
            generateGrammar(grammar, symbol, text);
            #r = random.randint(0, len(values) - 1);
            #newSymbol = values[r];

    return text;




def main():
    fileLocation = getFileName();
    grammar = buildGrammar(fileLocation);


    symbol = input("Symbol to generate (Enter to quit)? ");
    numSymbols = input("How many to generate? ");

    text = "";
    output = generateGrammar(grammar, symbol, text)
    print(output)



if __name__ == "__main__": main()