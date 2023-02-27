#!/usr/bin/env python3

def main():

    num_bottles = input("How many bottles of beer are on the wall?")

    num_bottles = int(num_bottles)

    if num_bottles >= 100:
        print("Input must be 99 or less.")

    else:
        for i in range(num_bottles, 0, -1):
            print(f"{i} bottles of beer on the wall!")
            print(f"{i} bottles of beer! You take one down, pass it around!")
            if i == 1:
                print("No more bottles of beer on the wall!")

            else:
                print(f"{i - 1} bottles of beer on the wall!")

main()
