print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure")



#First task: Ask if he's going to the left or right. Save the answer to a variable
where_to_go = input("You're at a crossroad. Where are you going? Type \"left\" or \"right\". \n").lower()

if where_to_go == "left":
    #Second task: Ask if user going to swim or wait.
    swim_or_wait = input("You came to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for the boat. Type \"swim\" to swim across. \n").lower()
    if swim_or_wait == "wait":
        #Third task: Choose a door
        color = input("You arrive at the island unharmed. There is a house with three doors. one red, one yellow, and one blue. Which color do you choose? \n").lower()
        if color == "yellow":
            print("You Win!")
        else:
            print("Game Over")  
    else:
        print("Game Over")
else:
    print("Game Over")