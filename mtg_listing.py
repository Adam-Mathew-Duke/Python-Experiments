# MTG Card List - Version 1

import os
import time
import scrython

totalCards=0
cardIndex=[]
cards={}

os.system('cls')
prompt = input('How many MTG cards?: ')

try:
	totalCards=int(prompt)
except ValueError:
	print('Value is not an integer - using default value.')
	totalCards=5
	time.sleep(2)

if (totalCards<1 or totalCards>20):
	print('Value is out of range - using default value.')
	totalCards=5
	time.sleep(2)

os.system('cls')
print('Please wait - Loading ' + str(totalCards) + ' cards...\n')

for index in range(totalCards):
	cardIndex.append(scrython.cards.Random())
	cards.update({cardIndex[index].name():cardIndex[index].rarity()})
	print(index+1,''+list(cards.keys())[index]+' - '+list(cards.values())[index])

print ('\nList is complete!\n')
# end of program
