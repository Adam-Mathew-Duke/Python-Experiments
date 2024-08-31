# Card Suits
# Aphasia exercise with playing card suits
# Version 1

import os
import random

# Print color text in the terminal
from colorama import Fore, Back, Style

# Setup the card suits
card_suit = ['♥','♦','♣','♠']
card_color = [Fore.RED,Fore.RED,Fore.BLACK,Fore.BLACK]
card_name = ['Hearts','Diamonds','Clubs','Spades']

# Press any key to continue
def user_prompt():
	prompt = input ('')
	prompt = prompt.upper()
	return prompt

while True:

	# Clear the terminal on Windows
	os.system('cls')
	print ('\n')

	# Choose a random card and display it
	card_index = random.randrange(4)
	print (card_color[card_index]+Back.WHITE+card_suit[card_index])
	
	# Reset the terminal colors
	print(Style.RESET_ALL)

	# Press any key or type exit to end
	prompt = user_prompt()
	if prompt == 'EXIT':
		break

	# Display the card suit name
	print (card_name[card_index])

	# Press any key or type exit to end
	prompt = user_prompt()	
	if prompt == 'EXIT':
		break

# Clear the terminal on Windows
os.system('cls')

# end of program
