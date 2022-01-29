myList = ["area", "book", "code", "data", "east", "audio", "build", "cable", "delay", "enjoy"]
myFile = open('words.txt', 'w')

for ch in myList:
    myFile.write(ch)
    myFile.write('\n')
myFile.close()
