def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    fileSelected = "Files\day1.txt"
    openMode = "r"
    myFile = open(fileSelected, openMode)
    fileContents = myFile.read().split("\n")
    for i in range(len(fileContents)):
        for j in range(len(fileContents)):
            for k in range(len(fileContents)):
                if int(fileContents[i]) + int(fileContents[j]) + int(fileContents[k]) == int(2020):
                    multiple1 = int(fileContents[i])
                    multiple2 = int(fileContents[j])
                    multiple3 = int(fileContents[k])
                    product = multiple1 * multiple2 * multiple3
                    print(int(multiple1))
                    print(int(multiple2))
                    print(int(multiple3))
                    print(int(product))

if __name__ == "__main__":
    main()