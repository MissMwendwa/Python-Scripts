#This python program will prompt the user to input their date of birth
#And this information will be used to determine their zodiac sign.

#Prompt the user to enter the date of birth and month

month = input("Please input your birth month:  ")
month.lower
date = int(input("Enter your date of birth:  "))

#create a list of all year round months and signs
months = ["january", "february", "march", "april", "may", "june", "july", "august", "spetember", "october", "november", "december"]

#this block will determine the zodiac sign
if month in months:
	if month == "march":
		sign = "Pisces" if (date<21) else "Aries"
	elif month == "april":
		sign = "Aries" if (date<20) else "Taurus"
	elif month == "may":
		sign = "Taurus" if (date<21) else "Gemini"
	elif month == "june":
		sign = "Gemini" if (date<21) else "Cancer"
	elif month == "july":
		sign = "Cancer" if (date<23) else "Leo"
	elif month == "august":
		sign = "Leo" if (date<23) else "Virgo"
	elif month == "september":
		sign = "Virgo" if (date<23) else "Libra"
	elif month == "october":
		sign = "Libra" if (date<23) else "Scorpio"
	elif month == "november":
		sign = "Scorpio" if (date<22) else "Sagittarius"
	elif month == "december":
		sign = "Sagittarius" if (date<22) else "Capricorn"
	elif month == "january":
		sign = "Capricorn" if (date<20) else "Acquarius"
	elif month == "february" :
		sign = "Acquarius" if (date<19) else "Pisces"

print("Your Zodiac Sign is: " + sign)  