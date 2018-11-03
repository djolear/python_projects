import os.path

def readMadlibFile():
    fileName = input("Mad Lib input file? ")
    fileLocation = 'G:/My Drive/personal/cs_projects/python_projects/madlibs/textFiles/' + fileName

    while os.path.exists(fileLocation) == False:
        print("That file does not exist. Please try again.\n")
        fileName = input("Mad Lib input file? ")
        fileLocation = 'G:/My Drive/personal/cs_projects/python_projects/madlibs/textFiles/' + fileName

    textFile = open(fileLocation, "r");
    return textFile.readlines();



def createMadlib(lines):
    newLib =[]
    for line in lines:
        for j in range(len(line)):
            if j < len(line):
                if line[j] == '<':
                    endInd = line.index('>')
                    lib = input("Please type a " + line[j + 1: endInd] + ": ")
                    line = line[:j] + lib + line[endInd + 1:]

        newLib.append(line)
    return newLib




def main():
    print("Welcome to Madlibs!\nI will ask you to provide various words\nand phrases to fill in a story.\nAt the end, I will display your story to you.\n")
    emptyMadlib = readMadlibFile()
    newLib = createMadlib(emptyMadlib)


    for i in newLib:
        print(i)



if __name__ == "__main__":main()




