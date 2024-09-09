'''
Name:           Main.py
Aim:            functionality without re-factoring
Description:    a prototype text adventure game
'''

game_state = "INTRODUCTION_ROOM"

def process_game_state(game_state,key_state):

    while game_state != "EXIT":

        if game_state == "INTRODUCTION_ROOM":

            # print context
            print("You are in a small, dimly lit room.")

            # print menu
            print("1. Look around the room")
            print("2. Check the desk drawer")
            print("3. Try to open the door")
            print("4. Do nothing")

            # grab the menu choice
            menu_choice = input("Your choice: ")

            print("\n")

            # process the menu choice and display the
            # appropiate flavor text
            if (menu_choice == '1'):
                print("Looking around reveals a solid door in front of you and a wooden desk with a draw in the corner.")
            elif (menu_choice == '2'):
                print("Checking the desk drawer reveals a hidden key.")
                game_state = "CHECK_DRAW"
            elif (menu_choice == '3'):
                print("You try to open the door")
                game_state = "CHECK_DOOR"
            elif (menu_choice == '4'):
                print("You do nothing and wonder why you are here.")

        elif game_state == "CHECK_DRAW":

            # print context
            print("There is a golden key in the draw it has an orate design.")

            # print menu
            print("1. Take key")
            print("2. Do nothing")

            # grab the menu choice
            menu_choice = input("Your choice: ")
            print("\n")

            if (menu_choice == '1'):
                print("You take the key and put it in your pocket.")
                print("You step away from the desk draw...")
                key_state = True
                
            elif (menu_choice == '2'):
                print("You step away from the desk draw...")
            
            # return to the introduction room
            game_state = "INTRODUCTION_ROOM"

        elif game_state == "CHECK_DOOR":

            # print context
            print("The door is locked. You need a key to open it.")

            if not key_state:

                print("You step away from the door draw.")
                game_state = "INTRODUCTION_ROOM"
                print("\n")

            else:

                # print menu
                print("1. Use key")
                print("2. Do nothing")

                # grab the menu choice
                menu_choice = input("Your choice: ")
                print("\n")
        
                if (menu_choice == '1'):
                    print("You unlock the door using the golden key")
                    print("You enter the hallway")
                    game_state = "HALLWAY"
                elif (menu_choice == '2'):
                    print("You step away from the door draw.")
                    # return to the introduction room
                    game_state = "INTRODUCTION_ROOM"

        
        elif game_state == "HALLWAY":

            # print context
            print("You step into a long narrow hallway with a treasure chest at the end.")

            # print menu
            print("1. Look around the hallway")
            print("2. Investigate the glint of metal in the brick work")
            print("3. Try to open the chest")
            print("4. Go back to the room")

            # grab the menu choice
            menu_choice = input("Your choice: ")

            print("\n")

            # process the menu choice and display the
            # appropiate flavor text
            if (menu_choice == '1'):
                print("Looking around the hallway reavels a glint of metal in the brick work.")
                game_state = "HALLWAY"
            elif (menu_choice == '2'):
                print("Checking the brick work reveals a hook lockpick and a tension wrench.")
                game_state = "CHECK_BRICK_WORK"
            elif (menu_choice == '3'):
                print("You try to open the treasure check lid but it's locked tight.")
                #game_state = "CHECK_CHEST"
            elif (menu_choice == '4'):
                print("You turn around and walk back into the room.")
                game_state = "INTRODUCTION_ROOM"

        elif game_state == "CHECK_BRICK_WORK":
            print("You find a hook lockpick and a tension wrench hidden behind a loose brick")
            game_state = "HALLWAY"

        elif game_state == "CHECK_CHEST":
            print("You cannot open it")
            game_state = "HALLWAY"
        print("\n")

process_game_state(game_state,True)
print("EXIT")

# end of code

'''
To do later afer basic functionality:
re-factor code into classes and multiple files
add more items and information to the game
write longer descriptions with a typewritter effect
Add menu items as you learn more about your environment
'''
