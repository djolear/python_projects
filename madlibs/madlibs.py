#print("Hello World!")

fileLocation = 'G:/My Drive/personal/cs_projects/python_projects/madlibs/textFiles/tarzan.txt';

textFile = open(fileLocation, "r");

lines = textFile.readlines();

#print(lines)
print(len(lines))

for i in lines:
    print(i)

