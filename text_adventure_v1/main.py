'''
Name:           Main.py
Description:    Classic text adventure game
Volume:         1
'''

game_state = "INTRODUCTION_ROOM"

def process_game_state(game_state,key_state,pick_state):

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
                print("You try to force open the check but the lid is locked")
                game_state = "CHECK_CHEST"
            elif (menu_choice == '4'):
                print("You turn around and walk back into the room.")
                game_state = "INTRODUCTION_ROOM"

        elif game_state == "CHECK_BRICK_WORK":

            # print context
            print("Stepping closer to the bricks you spot some lockpick tools hidden in the wall.")

            # print menu
            print("1. Examine Lockpick tools")
            print("2. Take Lockpick tools")
            print("3. Do nothing")

            # grab the menu choice
            menu_choice = input("Your choice: ")

            print("\n")

            # process the menu choice and display the
            # appropiate flavor text
            if (menu_choice == '1'):
                print("There is a hook pick and a tension wrench")
                game_state = "CHECK_BRICK_WORK"
            elif (menu_choice == '2'):
                print("You put the lockpick and tension wrench into your breast pocket")
                pick_state = True
                game_state = "HALLWAY"
            elif (menu_choice == '3'):
                print("You step away from the brick work")   
                game_state = "HALLWAY"

        elif game_state == "CHECK_CHEST":

            # print menu

            if not pick_state:

                print("1. Examine Chest")
                print("2. Use Golden Key")
                print("3. Do nothing")

                # grab the menu choice
                menu_choice = input("Your choice: ")

                print("\n")

                # process the menu choice and display the
                # appropiate flavor text
                if (menu_choice == '1'):
                    print("The large chest has an orate design")
                    game_state = "CHECK_CHEST"
                elif (menu_choice == '2'):
                    print("You try to open the check using the Golden Key")
                    print("The key does not fit in the lock")
                    game_state = "HALLWAY"
                elif (menu_choice == '3'):
                    print("You step away from the chest")   
                    game_state = "HALLWAY"

            else:

                print("1. Examine Chest")
                print("2. Use Golden Key")
                print("3. Use lockpick")
                print("4. Do nothing")

                # grab the menu choice
                menu_choice = input("Your choice: ")

                print("\n")

                # process the menu choice and display the
                # appropiate flavor text
                if (menu_choice == '1'):
                    print("The large chest has an orate design")
                    game_state = "CHECK_CHEST"
                elif (menu_choice == '2'):
                    print("You try to open the check using the Golden Key")
                    print("The key does not fit in the lock")
                    game_state = "HALLWAY"
                elif (menu_choice == '3'):
                    print("You use the lockpick to open the chest")
                    print("There is a treasure map inside")
                    print("You take the map and put it in your backpack")
                    print("To be continued! .....")   
                    game_state = "EXIT"
                elif (menu_choice == '4'):
                    print("You step away from the chest")   
                    game_state = "HALLWAY"

        print("\n")

'''
Test:
Start in HALLWAY
Has Golden Key
Has Lockpick
'''
process_game_state("HALLWAY",True,True)
print("EXIT")

# end of code

'''
Ideas:
    Test and add to basic functionality
    Re-factor the code into classes, data types and multiple files
    Add more items and information to the text adventure game
    Add a type writer effect to help with reading
    Add menu items as you explore the environment
    Lockpick can be made up of different seperate items
    Including hook, ball, diamond, tension wrench, rake and lube
    Add a carpet and some pictures and a window on the wall.
    Once everything is working how the game works with random item
    placement. Maybe not every item is in every run of the game?
    Or maybe there are different items on each playthrough?
    Or maybe you get a hard run or an easy run?
'''
