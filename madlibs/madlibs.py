#print("Hello World!")

fileLocation = 'C:/Users/djole/PycharmProjects/madlibs/textFiles/tarzan.txt';

textFile = open(fileLocation, "r");

lines = textFile.readlines();

#print(lines)
print(len(lines))

for i in lines:
    print(i)

