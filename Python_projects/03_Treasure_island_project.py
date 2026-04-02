print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
print("Your mission is to find the treasure.")
direction = input('you are at a cross road, where do you want to go? \ntype: "left" or "right".' ).lower()
if direction == "left":
    lake = input('You have come to the lake, there is island in the middle of the lake: \ntype "wait" to wait for a boat or type "swim" to swim across.').lower()
    if lake == "wait":
        color = input('You arrive at a island unharmed.\nthere is house with 3 doors.\n one red, one yellow ,one blue. which color do you choose?').lower()
        if color == "blue":
            print("Eaten by beats.\nGame Over")
        elif color == "yellow":
            print("You Won!")
        elif color == "red":
            print("Game Over!")
        else:
            print("You chose a door that doesn't exist.\nGame Over")
    else:
        print("Attacked by Trout.\nGame Over")
else:
    print("Fall into Hole.\nGame Over")
