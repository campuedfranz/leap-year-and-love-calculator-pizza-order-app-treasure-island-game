#Get the name of lovers names
name1 = input("What's the name of the male? ").lower()
name2 = input("What's the name of the female? ").lower()
combined_names = name1 + name2

#Count the occurence

#Count letter of T-R-U-E
counting_t = combined_names.count("t")
counting_r = combined_names.count("r")
counting_u = combined_names.count("u")
counting_e = combined_names.count("e")

first_number = str(counting_t + counting_r + counting_u + counting_e)


#Count letter of L-O-V-E

counting_l = combined_names.count("l")
counting_o = combined_names.count("o")
counting_v = combined_names.count("v")
counting_e = combined_names.count("e")

second_number = str(counting_l + counting_o + counting_v + counting_e)

#Calculate and print the score and finding

score = int(first_number + second_number)

if score <10 or score >90:
    compatibility = ", you go together like coke and mentos."
elif score >40 and score <50:
    compatibility = ", you are alright together."
else:
    compatibility = "."

print("The love calculator is calculating your score...")
print(f"Your score is {score}{compatibility}")

