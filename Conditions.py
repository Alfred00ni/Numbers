# Method to evaluate data
# if then else

import random
from turtle import hideturtle

HighRange = 100
MiddleNumber = int(HighRange / 2)
MyGuess = MiddleNumber 
NumberOfGuesses = 0

MyRandomNumber = random.randrange(1,HighRange)
#MyRandomNumber = 42
print(MyRandomNumber)

while True:
    NumberOfGuesses += 1

    if MyRandomNumber == MyGuess:
        print ("You win!!! The number was ",MyRandomNumber)
        print ("Number of Guesses", NumberOfGuesses)
        break
    # --------less than--------
    elif MyRandomNumber < MyGuess:
         # if TURE
        # Modify the guess to be in the middle of the range
        HighRange = MyGuess # high range = 50
        MyGuess = int(MiddleNumber / 2)
        MiddleNumber = MyGuess
    #---------greater than----------
    else :
         # if FLASE
        # Modify the guess to be in the middle of the range
        # greater than middle number -- less than high range
        # high range 50 - middle number 25 / 2 + 25 = 37
        range = (HighRange - MiddleNumber) / 2 + MiddleNumber
        MyGuess = int(range)
        MiddleNumber = MyGuess