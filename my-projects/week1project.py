#!/usr/bin/env python3

#Ask user to input birthdate

def main():
    while True:
        try:
            birth_date = input("Enter your birth date (in the format MM/DD/YYYY): ")
#Convert string input into int        
            month, day, year = map(int, birth_date.split('/'))
#Input validation
            if year <= 0:
                raise ValueError("Invalid year.")
            if year > 2023:
                raise ValueError("Are you from the future?")
            if day > 31 or day <= 0:
                raise ValueError("Invalid day.")
            if month > 12 or month <= 0:
                raise ValueError("Invalid month.")
            if month in [4, 6, 9, 11] and day > 30:
                raise ValueError("Invalid day for this month.")
            if month == 2 and ((day > 29) or (day == 29 and not (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)))):
                raise ValueError("Invalid day for February.")
            break
        except (ValueError, TypeError) as e:
            if e:
                print(e)

#Set zodiac sign to calander date
    zodiac_sign = ''
    if (month == 12 and day >= 22) or (month == 1 and day <= 19):
        zodiac_sign = 'Capricorn'
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        zodiac_sign = 'Aquarius'
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        zodiac_sign = 'Pisces'
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        zodiac_sign = 'Aries'
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        zodiac_sign = 'Taurus'
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        zodiac_sign = 'Gemini'
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        zodiac_sign = 'Cancer'
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        zodiac_sign = 'Leo'
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        zodiac_sign = 'Virgo'
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        zodiac_sign = 'Libra'
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        zodiac_sign = 'Scorpio'
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        zodiac_sign = 'Sagittarius'

#Print zodiac sign
    if zodiac_sign:
        print(f"I had a feeling you were a {zodiac_sign}...")

main()
