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
print("You've come to a crossroads on a dark and stormy night. There is a chill in the air and a thick fog covering "
      "the area. Where do you want to go?")
direction = input('       Type "left" or "right"\n       Your Choice: ')
if direction.lower() == "left":
    print("You've come to a mysterious lake. As you struggle to see through the fog, you notice an island off in the "
          "middle of the lake. You find an empty dock - do you wait for a boat or try to swim across?")
    wait = input('       Type "wait" to see if a boat comes along. Type "swim" to brave the waters to swin across.\n'
                 '       Your Choice: ')
    if wait.lower() == "wait":
        print("After a long wait, an old wooden boat arrives at the dock. As the boat comes closer and closer, "
              "you realize that there is no one steering the boat! Against your better judgement, you board the boat\n"
              "and depart for the mysterious island.\n\nThe voyage is long and turbulent, but you finally arrive at the "
              "island unharmed. There, you find a massive house with 3 doors.")
        door = input("One door is red, one is yellow and the last door is blue. Which color do you chose?\n       Your Choice: ")
        if door.lower() == "red":
            print("As you approach the red door, you start to notice the temperature rising. You foolishly open the door and are immediately burned alive by an intense backdraft! Game Over!")
        elif door.lower() == "blue":
            print("As you approach the blue door, you hear the feint sound of animals. You open the door and are trampled by a stampede of beasts! You attempt to pick yourself up but find yourself face-to-face with\nbeady eyes and sharp teeth. Game Over!")
        else:
            print("As you approach the yellow door, you hear a loud hum coming from the other side of the door. You open the door and are blinded by an intense light! You have found the treasure! You Win!")

    else:
        print("You decide to brave the frigid waters and swim to the island. Little did you know, this lake was "
              "infested with hungry alligators! You are torn to shreds in a matter of seconds! Game Over!")
else:
    print("Drats! Its so dark and foggy out that you didn't see that hole! You've fallen to your death! Game Over!")

