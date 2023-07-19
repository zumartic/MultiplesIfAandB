import sys

def main():

    # Tallennetaan annetut argumentit taulukkoon
    args = sys.argv[1:]

    # Tarkistetaan annettujen argumenttien määrä
    argumentCount = len(args)
    if argumentCount==2:

        # Ensimmäisenä annettu argumenttin on input-tiedosto
        inputFileName = args[0]

        # Toisena annettu argumentti on output-tiedosto
        outputFileName = args[1]

        # Jos argumentteja on annettu oikea määrä niin etsitään monikerrat
        read_file_line_by_line(inputFileName, outputFileName)
    else:
        print("Correct amount for parameters is 2. Example command line command: python multiples.py input.txt output.txt")


# Monikertojen etsintä
def read_file_line_by_line(inputFileName, outputFileName):
    resultsArr = []

    # Avataan ja luetaan input-tiedosto
    try:
        with open(inputFileName, 'r') as file:
             # Siivotaan / Muodostetaan output-tiedosto
            f = open(outputFileName, "w")
            f.write("")
            f.close()

            # Käydään input-tiedosto läpi rivi kerrallaan
            for line in file:
                # Poistetaan ylimääräiset välilyönnit rivien aluista ja lopuista
                line = line.strip()

                # Muutetaan rivien lukujonot taulukoiksi
                array = line.split()

                # Etsitään lukujen monikerrat erillisellä aliohjelmalla
                multipleResult = getMultiples(int(array[0]), int(array[1]), int(array[2]))

                # Lisätään löydetyt monikerrat ja niiden määrät väliaikaisiin tuloksiin
                resultsArr.append(multipleResult)

        # Lajitellaan tulokset nousevaan järjestykseen löydettyjen määrien mukaisesti
        resultsArr.sort(key=sortSecond)

        # Lasketaan tulostaulukon pituus
        arrLen = len(resultsArr)

        # Tulostetaan tulokset ja kirjoitetaan output-tiedostoon
        # resultsArr taulukko sisältää myös kyseisen tulosrivin pituuden ja
        # pituutta ei tulostetaa tuloksiin
        for i in range(arrLen):

            # Tulostetaan rivi näytölle
            fileLine = str(resultsArr[i][0])
            print(fileLine)

            # Lisätään rivi output-tiedostoon
            outputFile = open(outputFileName, "a")
            outputFile.write(fileLine)

            # Ei rivinvaihtoa viimeiselle riville output-tiedostossa
            if i<arrLen-1:
                outputFile.write("\n")
            outputFile.close()

    # Annetaan virheilmoitus, jos input-tiedostoa ei löydy
    except FileNotFoundError:
        print(f"Input tiedostoa: '{inputFileName}' ei löydy!")


# Aliohjelma monikertojen etsimiseen
def getMultiples(A, B, Goal):
    resultArr = []

    # Käydään lukujen A ja B monikerrat yksitelleen läpi ja 
    # lisätään ne tulostaulukkoon, jos kysäistä monikertaa
    # ei jo ole tulostaulukossa
    for x in range(1, Goal):
        if (A*x<Goal):
            resultArr.append(A*x) if A*x not in resultArr else resultArr

        if (B*x<Goal):
            resultArr.append(B*x) if B*x not in resultArr else resultArr

    # Lajitellaan tulostaulukko nousevaan järjestykseen
    resultArr.sort()
    
    # Lasketaan tulostaulukon pituus, tarvitaan lopullisten tulosten lajitteluun
    arrLen = len(resultArr)

    # Muutetaan tulostaulukko merkkijonoksi
    returnStr = ', '.join([str(elem) for elem in resultArr])
    
    # Muutetaan tulos-merkkijono lopulliseen tulostettavaan muotoon
    returnStr = str(Goal)+": "+returnStr

    # Palautetaan tulokset
    return [returnStr, arrLen]


# Aliohjelma tulosten lajittelua varten
def sortSecond(val):
    return val[1]

if __name__ == "__main__":
    main()
