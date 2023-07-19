# Multiples of A and B
## Theory
Let’s assume that A is 4 and B is 7, so if we list all the natural numbers below 20 that are multiples of A or B, we get 4, 7, 8, 12, 14 and 16.

## Program
MultiplesOfAandB takes a file as the first command line argument. The file need to consits a list of numbers, with 3 numbers per row separated by space and number of rows can be undefined (i.e. it can be something between 1 - infinite). 

First number in a row is A and the second is B, third one is the goal number (as in theorem 20). The program searches all multiples of A and B which are below the third number, prints it out to screen and also write results to file which needs to be given as the second command line argument. Program sorts out the results to ascending order based on multiples count on certain row.

**MultiplesOfAndB can be run by using Python**
```
python multiples.py input.txt output.txt
```

## Example
Example input file content:
```
5 8 31
4 7 20
```

Example screen output and output file content:
```
20:4 7 8 12 14 16 
31:5 8 10 15 16 20 24 25 30
```
