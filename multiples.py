
import sys

def main():
    args = sys.argv[1:]
    argumentCount = len(args)
    if argumentCount==2:
        inputFileName = args[0]
        outputFileName = args[1]
        read_file_line_by_line(inputFileName, outputFileName)
    else:
        print("Correct amount for parameters is 2. Example command line command: python multiples.py input.txt output.txt")

def read_file_line_by_line(inputFile, outputFile):
    resultsArr = []
    try:
        with open(inputFile, 'r') as file:
             # Clear / Create output file
            f = open(outputFile, "w")
            f.write("")
            f.close()

            for line in file:
                # Poistetaan ylimääräiset välilyönnit rivien aluista ja lopuista
                line = line.strip()

                # String to Array
                array = line.split()

                # Get multiples
                multipleResult = getMultiples(int(array[0]), int(array[1]), int(array[2]))
                resultsArr.append(multipleResult)

        resultsArr.sort(key=sortSecond)

        arrLen = len(resultsArr)
        
        for i in range(arrLen):
            fileLine = str(resultsArr[i][0])
            print(fileLine)
            outputFile = open("output.txt", "a")
            outputFile.write(fileLine)
            if i<arrLen-1:
                outputFile.write("\n")
            outputFile.close()

    except FileNotFoundError:
        print(f"Input tiedostoa: '{inputFile}' ei löydy!")

def getMultiples(A, B, Goal):
    resultArr = []

    for x in range(1, Goal):
        if (A*x<Goal):
            resultArr.append(A*x) if A*x not in resultArr else resultArr

        if (B*x<Goal):
            resultArr.append(B*x) if B*x not in resultArr else resultArr

    resultArr.sort()
    
    arrLen = len(resultArr)
    returnStr = ', '.join([str(elem) for elem in resultArr])
    returnStr = str(Goal)+": "+returnStr

    return [returnStr, arrLen]

def sortSecond(val):
    return val[1]

if __name__ == "__main__":
    main()