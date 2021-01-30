# bmi.py
# Program that calculates somebody's Body Mass Index (BMI)
# Author: Liam Nutley

# We begin by creating our input prompts.
weight = int(input("Enter your weight in Kilograms (Kg): "))
height = int(input("Enter your height in centimetres: ")) / 100
# Height needs to be in metres squared so we adjust it accordingly. 
height = height**2
# We use .format to output our text and result together 
# BMI is weight/height (Height in metres squared!)
print ('Your BMI is {}' .format (weight/height))