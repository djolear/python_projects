import os.path

def createMadlib(filename);

print("Welcome to Madlibs!\nI will ask you to provide various words\nand phrases to fill in a story.\nAt the end, I will display your story to you.\n")


fileName = input("Mad Lib input file? ")
fileLocation = 'G:/My Drive/personal/cs_projects/python_projects/madlibs/textFiles/' + fileName


while os.path.exists(fileLocation) == False:
    print("That file does not exist. Please try again.\n")
    fileName = input("Mad Lib input file? ")
    fileLocation = 'G:/My Drive/personal/cs_projects/python_projects/madlibs/textFiles/' + fileName

textFile = open(fileLocation, "r");


lines = textFile.readlines();

#print(lines)
print(len(lines))

for i in lines:
    print(i)

# starting code again here



