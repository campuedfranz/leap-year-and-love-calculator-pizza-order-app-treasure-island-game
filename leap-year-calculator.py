print("IS IT LEAP YEAR?")

#Get the year you want to check then save to a variable
year_to_check = int(input("What year you want to check? "))

if (year_to_check % 4) == 0:
    if (year_to_check % 100) == 0:
        if (year_to_check % 400) == 0:
            print(f"{year_to_check} is a leap year!")
        else:
            print(f"{year_to_check} is not a leap year!")
    else:
        print(f"{year_to_check} is a leap year!")
else:
    print(f"{year_to_check} is not a leap year!")