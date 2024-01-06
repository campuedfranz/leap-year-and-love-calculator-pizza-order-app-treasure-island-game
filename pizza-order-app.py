print("Thank you for choosing Big Papa's Pizza Deliveries")

#Ask pizza size and save it to a variable

pizza_size = input("What size of pizza do you want? S, M, or L ")

bill = 0

if pizza_size == "S":
    bill = 15
elif pizza_size == "M":
    bill = 20
else:
    bill = 25
#Ask if they want pepperoni 
add_pepperoni = input("Do you want pepperoni? Y or N ")
if add_pepperoni == "Y":
    #Check size as basis for additional bill from cheese
    if  pizza_size == "MS":
        bill = bill + 2
    else:
        bill = bill + 3
#Ask if they want extra cheese
add_extra_cheese = input("Do you want extra cheese? Y or N ")
if add_extra_cheese == "Y":
    bill = bill + 1

print(f"Your final bill is ${bill}.")
