# Context.py
# Menu items for the current part of the game

start_room_menu = [
"Look around the room",
"Check the drawer",
"Try to open the door",
"Do nothing"
]

menu_dictionary = {
    "START_ROOM":start_room_menu
}

def menu(menu_name):
    print('\n')
    menu_item_count=0
    for menu_items in menu_dictionary[menu_name]:
        menu_item_count+=1
        print(str(menu_item_count)+". "+menu_items)
    print('\n')

# end of code
