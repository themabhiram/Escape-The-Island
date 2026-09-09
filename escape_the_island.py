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
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
program_name = "    Escape the Island with a Treasure    "
print("="*len(program_name))
print(program_name)
print("="*len(program_name))
print()
#Game start
print("--> You wake up alone on a mysterious island. Your goal is to find the treasure and escape before nightfall.    \n")
# 1. The First Path (1st question)
print("[0] You see two paths. The left path goes into a dark forest, while the right path follows the beach toward the mountains.")
question_1 = input("Choices --> Left - Enter the forest (or) Right - Follow the beach\nYour Choice : ")
question_1.lower()
print()
# if the answer right
if question_1 == "right":
    #The River (2nd question)
    print("[1] You reach a deep river. The water is moving quickly, but you notice a small wooden boat tied to a tree.")
    question_2 = input("Choices -->  SWIM — Try to swim across (or) BOAT — Use the boat\nYour Choice : ")
    question_2.lower()
    print()
    if question_2 == "boat":
        # The Cave (3rd question)
        print("[2] On the other side, you find a cave. Inside, you hear water dripping, but you also see fresh footprints leading deeper inside.")
        question_3 = input("Choices --> ENTER — Follow the footprints (or) LEAVE — Walk away\nYour Choice : ")
        question_3.lower()
        print()
        if question_3 == "enter":
            # The Two Doors (4th question)
            print("[3] Deep inside the cave, you find two doors. One is covered in old scratches. The other has a golden symbol carved into it.")
            question_4 = input("Choices --> LEFT — Open the scratched door (or) RIGHT — Open the golden door.\nYour Choice : ")
            question_4.lower()
            print()
            if question_4 == "right":
                # The Treasure (5th and last question)
                print("[4] Behind the golden door, you find the treasure! 💰 But the cave begins to collapse.\nYou see a narrow tunnel leading outside and a large tunnel that looks unstable.")
                question_5 = input("Choices --> NARROW TUNNEL — Crawl through it (or) LARGE TUNNEL — Run through it.\nYour Choice : ")
                question_5.lower()
                print()
                if question_5 == "narrow tunnel":
                    winngin_statement = "    You Won The Game    "
                    pattern_deign = len(winngin_statement)
                    pattern = "="*pattern_deign
                    print(f"You crawl through the narrow tunnel, escape the collapsing cave, and reach the beach with the treasure.\n🚁 A rescue helicopter spots you.\nYOU ESCAPED!\n\n{pattern}\n{winngin_statement}\n{pattern}")
                elif question_5 == "large tunnel":
                    game_over_statement_1 = "    Rocks block the tunnel. GAME OVER.    "
                    game_over_statement_1_len = len(game_over_statement_1)
                    print("="*game_over_statement_1_len)
                    print(game_over_statement_1)
                    print("="*game_over_statement_1_len)
                else:
                    print("Choice not valid")
            elif question_4 == "left":
                 game_over_statement_2 = "    A trap activates beneath your feet. GAME OVER.    "
                 game_over_statement_2_len = len(game_over_statement_1)
                 print("="*game_over_statement_2_len)
                 print(game_over_statement_2)
                 print("="*game_over_statement_2_len)
            else:
                print("Choice not valid")
        elif question_3 == "leave":
            game_over_statement_3 = "    You lose the trail and become trapped as night falls. GAME OVER.    "
            game_over_statement_3_len = len(game_over_statement_3)
            print("="*game_over_statement_3_len)
            print(game_over_statement_3)
            print("="*game_over_statement_3_len)
        else:
            print("Choice not valid")
    elif question_2 == "swim":
        game_over_statement_4 = "    The strong current pulls you away. GAME OVER.    "
        game_over_statement_4_len = len(game_over_statement_4)
        print("="*game_over_statement_4_len)
        print(game_over_statement_4)
        print("="*game_over_statement_4_len)
    else:
        print("Choice not valid")
elif question_1 == "left":
    # question 2 if player select left
    print("[1] You enter the dark forest. After a few minutes, you find a small cabin. \nThe door is open, but you hear strange noises inside. \nBehind the cabin, you also see a narrow path leading deeper into the forest.")
    question_2_wrong_side = input("Choices --> A — Enter the cabin (or) B — Follow the forest path.\nYour Choice : ")
    question_2_wrong_side.lower()
    print()
    if question_2_wrong_side == "a":
        game_over_statement_5 = "    You trigger a trap. GAME OVER.    "
        game_over_statement_5_len = len(game_over_statement_5)
        print("="*game_over_statement_5_len)
        print(game_over_statement_5)
        print("="*game_over_statement_5_len)
    elif question_2_wrong_side == "b":
        print("[2] You reach a deep river. The water is moving quickly, but you notice a small wooden boat tied to a tree.")
        question_2 = input("Choices -->  SWIM — Try to swim across (or) BOAT — Use the boat\nYour Choice : ")
        question_2.lower()
        print()
        if question_2 == "boat":
        # The Cave (3rd question)
            print("[3] On the other side, you find a cave. Inside, you hear water dripping, but you also see fresh footprints leading deeper inside.")
            question_3 = input("Choices --> ENTER — Follow the footprints (or) LEAVE — Walk away\nYour Choice : ")
            question_3.lower()
            print()
            if question_3 == "enter":
                    # The Two Doors (4th question)
                    print("[4] Deep inside the cave, you find two doors. One is covered in old scratches. The other has a golden symbol carved into it.")
                    question_4 = input("Choices --> LEFT — Open the scratched door (or) RIGHT — Open the golden door.\nYour Choice : ")
                    question_4.lower()
                    print()
                    if question_4 == "right":
                        # The Treasure (5th and last question)
                        print("[5] Behind the golden door, you find the treasure! 💰 But the cave begins to collapse.\nYou see a narrow tunnel leading outside and a large tunnel that looks unstable.")
                        question_5 = input("Choices --> NARROW TUNNEL — Crawl through it (or) LARGE TUNNEL — Run through it.\nYour Choice : ")
                        question_5.lower()
                        print()
                        if question_5 == "narrow tunnel":
                            winngin_statement = "    You Won The Game    "
                            pattern_deign = len(winngin_statement)
                            pattern = "="*pattern_deign
                            print(f"You crawl through the narrow tunnel, escape the collapsing cave, and reach the beach with the treasure.\n🚁 A rescue helicopter spots you.\nYOU ESCAPED!\n\n{pattern}\n{winngin_statement}\n{pattern}")
                        elif question_5 == "large tunnel":
                            game_over_statement_6 = "    Rocks block the tunnel. GAME OVER.    "
                            game_over_statement_6_len = len(game_over_statement_6)
                            print("="*game_over_statement_6_len)
                            print(game_over_statement_6)
                            print("="*game_over_statement_6_len)
                        else:
                            print("Choice not valid")
                    elif question_4 == "left":
                                    game_over_statement_7 = "    A trap activates beneath your feet. GAME OVER.    "
                                    game_over_statement_7_len = len(game_over_statement_7)
                                    print("="*game_over_statement_7_len)
                                    print(game_over_statement_7)
                                    print("="*game_over_statement_7_len)
                    else:
                        print("Choice not valid")
            elif question_3 == "leave":
                        game_over_statement_8 = "    You lose the trail and become trapped as night falls. GAME OVER.    "
                        game_over_statement_8_len = len(game_over_statement_8)
                        print("="*game_over_statement_8_len)
                        print(game_over_statement_8)
                        print("="*game_over_statement_8_len)

            else:
                 print("Choice not valid") 
        elif question_2 == "swim":
                print("The strong current pulls you away. GAME OVER.")
                game_over_statement_8 = "    You lose the trail and become trapped as night falls. GAME OVER.    "
                game_over_statement_8_len = len(game_over_statement_8)
                print("="*game_over_statement_8_len)
                print(game_over_statement_8)
                print("="*game_over_statement_8_len)

        else:
            print("Choice not valid")   
else:
    print("Choice not valid")