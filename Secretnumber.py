# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:34:48 2023

@author: ddebaggis
"""
#game setup
print("Please think of a number between 0 and 100!")
# set variables highest possible number is 100 & lowest is 0
hi = 100
lo = 0

guessed = False

#Loop until correct
while not guessed:
    #Bisection search: guess the midpoint between our current high and low guesses
    guess = (hi+lo)//2
    print("Is your secret number " + str(guess))
    user_inp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indcate I guessed Correctly.")
    
    if user_inp == 'c':
        #correct answer
        guessed = True
    elif user_inp == 'h':
        #guess was too high. So make the current guess the highest possible guess
        hi = guess
    elif user_inp == 'l':
        #guess was too high. So make the current guess the lowest possible guess
        lo = guess
    else:
        print("Sorry, I did not understand your input.")

print("Game over. Your secret number was: " +str(guess))

    
