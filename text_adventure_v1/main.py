'''
Name:           Main.py
Description:    Classic text adventure game
Volume:         1
'''

'''

Next:

Expand on the lock pick mini game to make it more fun
and interesting.

Add some more items and descriptions to my game.

Re-factor the code

Ideas
Re-factor the code.    
Build on the foundation
Add more items and information to the game
Add a type writer effect to the text
Add new menu items as you explore
Lockpick multiple items: hook, ball, diamond, tension
wrench, rake, lube
Add a carpet and some pictures and a window on the wall
Explore random item placement for each run of the game
Explore different items during each playthrough
'''

import os
import random

pick_chance = 80

# hook, snowman, rake
pick_type = "HOOK" # hook, snowman, rake
lock_lube = False
open_lock = False


def process_game_state(game_state,key_state,pick_state):

    while game_state != "EXIT":

        if game_state == "INTRODUCTION_ROOM":

            os.system('cls')

            # print context
            print("\nYou are in a small, dimly lit room.\n")

            # print menu
            print("1. Look around the room")
            print("2. Check the desk drawer")
            print("3. Check the door")
            print("4. Do nothing")

            # grab the menu choice
            menu_choice = input("\nYour choice: ")

            print('\n')

            # process the menu choice and display the
            # appropiate flavor text
            if (menu_choice == '1'):
                print("There is a solid door in front of you.")
                print("A writing table next to the wall on the right of you.")
                print("The desk has a single draw.")
            elif (menu_choice == '2'):
                print("You approach the writing desk.")
                game_state = "CHECK_DRAW"
            elif (menu_choice == '3'):
                print("You approach the door.")
                game_state = "CHECK_DOOR"
            elif (menu_choice == '4'):
                print("You do nothing and wonder why you are here.")

            print('\n')
            input("Press Any Key...")
            os.system('cls')

        elif game_state == "CHECK_DRAW":

            # print context
            print("Checking the desk drawer reveals a hidden key.")
            print("The key is golden with an orate design.")
            print("It's designed for Doors.")

            print('\n')

            # print menu
            print("1. Take key")
            print("2. Return to the room")

            print('\n')

            # grab the menu choice
            menu_choice = input("Your choice: ")

            print('\n')

            if (menu_choice == '1'):
                print("You take the key and put it in your pocket.")
                print("You step away from the desk draw...")
                key_state = True
                
            elif (menu_choice == '2'):
                print("You step away from the desk draw...")

            # return to the introduction room
            game_state = "INTRODUCTION_ROOM"

            print('\n')
            input("Press Any Key...")
            os.system('cls')

        elif game_state == "CHECK_DOOR":

            # print context
            print("The door has an ornate design there is a key hole just below the handle.")
            print('\n')

            if not key_state:

                # print menu
                print("1. Try handle")
                print("2. Return to the room")

                # grab the menu choice
                print('\n')
                menu_choice = input("Your choice: ")
                print("\n")
        
                if (menu_choice == '1'):
                    print("You try the handle but the door does not budge. Maybe you need a key.")
                    game_state = "CHECK_DOOR"
                elif (menu_choice == '2'):
                    print("You step away from the door.")
                    game_state = "INTRODUCTION_ROOM"

                print('\n')
                input("Press Any Key...")
                os.system('cls')

            else:

                # print menu
                print("1. Use key")
                print("2. Do nothing")

                # grab the menu choice
                print('\n')
                menu_choice = input("Your choice: ")
                print("\n")
        
                if (menu_choice == '1'):
                    print("You unlock the door using the golden Door key")
                    print("You enter the hallway")
                    game_state = "HALLWAY"
                elif (menu_choice == '2'):
                    print("You step away from the door draw.")
                    # return to the introduction room
                    game_state = "INTRODUCTION_ROOM"

                print('\n')
                input("Press Any Key...")
                os.system('cls')

        elif game_state == "HALLWAY":

            os.system('cls')

            print("\n")

            # print context
            print("You step into a long narrow hallway with a treasure chest at the end.")

            print('\n')

            # print menu
            print("1. Look around the hallway")
            print("2. Investigate the glint of metal in the brick work")
            print("3. Examine Treasure Chest")
            print("4. Go back to the room")

            print('\n')

            # grab the menu choice
            menu_choice = input("Your choice: ")

            print("\n")

            # process the menu choice and display the
            # appropiate flavor text
            if (menu_choice == '1'):
                print("Looking around the hallway reavels a glint of metal in the brick work.")
                print("There is a large ornate treasure check at the very end of the hallway.")
                
                print('\n')
                input("Press Any Key...")
                os.system('cls')

                game_state = "HALLWAY"
            elif (menu_choice == '2'):
                print("Checking the brick work reveals a hook lockpick and a tension wrench.")

                print('\n')
                input("Press Any Key...")
                os.system('cls')

                game_state = "CHECK_BRICK_WORK"
            elif (menu_choice == '3'):
                print("You step closer to the treasure chest.")
     
                print('\n')
                input("Press Any Key...")
                os.system('cls')

                game_state = "CHECK_CHEST"
            elif (menu_choice == '4'):
                print("You turn around and walk back into the room.")

                print('\n')
                input("Press Any Key...")
                os.system('cls')

                game_state = "INTRODUCTION_ROOM"

        elif game_state == "CHECK_BRICK_WORK":

            print('\n')

            # print context
            print("Stepping closer to the bricks you spot some lockpick tools hidden in the wall.")

            print('\n')

            # print menu
            print("1. Examine Lockpick tools")
            print("2. Take Lockpick tools")
            print("3. Do nothing")

            print('\n')

            # grab the menu choice
            menu_choice = input("Your choice: ")

            print("\n")

            # process the menu choice and display the
            # appropiate flavor text
            if (menu_choice == '1'):
                print("There is a hook pick and a tension wrench")
                print("Maybe I can open the treasure chest with this!")
                print("With these basic tools I'll need to be lucky!")

                print('\n')
                input("Press Any Key...")
                os.system('cls')

                game_state = "CHECK_BRICK_WORK"
            elif (menu_choice == '2'):
  
                print("You put the lockpick and tension wrench into your breast pocket")
                print("I have some lock picking experience I feel like I have a chance")

                print('\n')
                input("Press Any Key...")
                os.system('cls')

                pick_state = True
                game_state = "HALLWAY"

            elif (menu_choice == '3'):

                print("You step away from the brick work")   

                print('\n')
                input("Press Any Key...")
                os.system('cls')

                game_state = "HALLWAY"

        elif game_state == "CHECK_CHEST":

            # print menu
            print("You crouch down in front of the treasure chest.")
            print('\n')

            if not pick_state:

                print("1. Examine Chest")
                print("2. Use Golden Door Key")
                print("3. Do nothing")

                print('\n')

                # grab the menu choice
                menu_choice = input("Your choice: ")

                print("\n")

                # process the menu choice and display the
                # appropiate flavor text
                if (menu_choice == '1'):
                    print("The large chest has an orate design")
                    print("The is a keyhole but no sign of the key anywhere")
                    print("Maybe there is a way to open the chest without using the original key")

                    print('\n')
                    input("Press Any Key...")
                    os.system('cls')


                    game_state = "CHECK_CHEST"
                elif (menu_choice == '2'):
                    print("You try to open the check using the Golden Door Key")
                    print("The key does not fit in the lock")
                    print("The key is designed to use in doors not chests.")

                    print('\n')
                    input("Press Any Key...")
                    os.system('cls')


                    game_state = "HALLWAY"
                elif (menu_choice == '3'):
                    print("You step away from the chest")

                    print('\n')
                    input("Press Any Key...")
                    os.system('cls')

                    game_state = "HALLWAY"

            else:

                print("1. Examine Chest")
                print("2. Use Golden Door Key")
                print("3. Use lockpick (hook type and tension wrench)")
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
                    print("You try to open the check using the Golden Door Key")
                    print("The key does not fit in the lock")
                    game_state = "HALLWAY"
                elif (menu_choice == '3'):

                    '''
                    let's make a little mini game of chance here...
                    '''

                    if (pick_type == "HOOK"):
                        pick_chance = 1

                    # 50% chance of picking the lock
                    pick_attempt = random.randint(1, 2)

                    if (pick_attempt == pick_chance):
                        open_lock = True
                    else:
                        open_lock = False

                    if open_lock == True:
                        print("You use the lockpick to open the chest")
                        print("There is a treasure map inside")
                        print("You take the map and put it in your backpack")
                        print("To be continued! .....")   
                        game_state = "EXIT"
                    elif open_lock == False:
                        print("You did not pick the lock but you are close")
                        print("You adjust your grip and get ready to try again")

                        print('\n')
                        input("Press Any Key...")
                        os.system('cls')

                        game_state = "CHECK_CHEST"


                elif (menu_choice == '4'):
                    print("You step away from the chest")   
                    
                    print('\n')
                    input("Press Any Key...")
                    os.system('cls')

                    game_state = "HALLWAY"

        print("\n")

process_game_state("HALLWAY",True,False)
print("EXIT")

# end of code
