# Context.py
# Context for the current part of the game

context_dictionary = {
"START_ROOM":"You begin in a small, dimly lit room.",
"USE_KEY":"Context: After finding the key, it unlocks the door.",
"ENTER_HALLWAY":"The player steps into a hallway with a treasure chest at the end.",
"FIND_LOCKPICK":"The player searches the hallway and finds a lockpick hidden behind some loose bricks.",
"OPEN_CHEST":"After unlocking the chest, the player retrieves the treasure map."
}

def context(context_name):
    print('\n'+context_dictionary[context_name])

# end of code
