def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    fileSelected = "Files\day2.txt"
    openMode = "r"
    myFile = open(fileSelected, openMode)
    fileContents = myFile.read().split("\n")
    for i in range(len(fileContents)):
        fileContents[i]= fileContents[i].split(" ")
        for j in range(len(fileContents[i])):
            if j == 0:
                fileContents[i][j] = fileContents[i][j].split("-")
            elif j == 1:
                fileContents[i][j] = fileContents[i][j].replace(":", "")


    validCount = 0
    #for i in range(len(fileContents)):
        #letCount = fileContents[i][2].count(fileContents[i][1])
        #if letCount in range(int(fileContents[i][0][0]), int(fileContents[i][0][1])+1):
         #   validCount += 1
    #print(validCount)

    for i in range(len(fileContents)):
        targetLet = fileContents[i][1]
        spot1 = int(fileContents[i][0][0])
        spot2 = int(fileContents[i][0][1])
        targetPassword = fileContents[i][2]
        if (targetPassword[int(fileContents[i][0][0])-1] == targetLet or targetPassword[int(fileContents[i][0][1])-1] == targetLet) and not (targetPassword[int(fileContents[i][0][0])-1] == targetLet and targetPassword[int(fileContents[i][0][1])-1] == targetLet):
            validCount += 1

    print(validCount)
if __name__ == "__main__":
    main()