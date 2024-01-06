#IF/ELSE Statement
print("Welcome to the rollercoaster!")

#Get the users height and age and save in a variable
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))


if height >= 120:

    #If statement to check age

    #Nesting an if statement
    if age > 18 and age <45:
        bill = 5
        print("Adult ticket is $12")
    elif age >=12 and age <=18:
        print("Youth ticket is $7")
        bill = 7
    elif age >=45 and age <=55:
        bill = 0
        print("Everythings gonna be okay. Have a free ride on")
    else:
        bill = 5
        print("Child ticket is $5")

    wants_photo_taken = input("Do you want a photo taken? Y or N. ")

    #This if statement will still run after the if statement above - Multiple if in succession
    #This allows to have many conditions to check and actions to take
    #If statement to check if they want photo taken 
    if wants_photo_taken == "Y":
        #Add $3 dollars to bill
        bill = bill + 3

    print(f"Your final bill is {bill}.") 
else:
    print("You are too short. You cannot ride the rollercoaster!")


#Modulo to get the remainder
print("Is it ODD or EVEN?")

#Get the number input and save to variable
number = int(input("Which number you want to check? "))

#Determine if its even number
if number % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")


