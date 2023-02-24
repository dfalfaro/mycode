#!/usr/bin/env python3

import random

def main():

    num = random.randint(1, 100)

    rounds = 0

    guess = ''

    while rounds < 5 and guess != num:

        guess = input("Guess a number between 1 and 100\n>")

        if not guess.isdigit():
            print("Number input only")
            guess = int(guess)


        else:
            continue

        if guess > num:
            print("Too high!")
            rounds += 1

        elif guess < num:
            print("Too low!")
            rounds += 1

        else:
            print("Correct!")

        

main()
