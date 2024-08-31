'''
Name: Card Suits
Version: 2 - add GUI support
Description: Aphasia exercise using the four playing card suits
'''

import os
import random
import tkinter

card_suit = ['♥','♦','♣','♠']
card_name = ['Hearts','Diamonds','Clubs','Spades']
card_color = ['red','red','black','black']

def card_display():

	answer_text.set('') # clear the answer
	card_text.set(card_suit[random.randint(0,3)]) # new random suit
	button_text.set('Check') # update the button

	# update the card suit
	if card_text.get() == card_suit[0]:
		card_label.config(fg=card_color[0])
	elif card_text.get() == card_suit[1]:
		card_label.config(fg=card_color[1])
	elif card_text.get() == card_suit[2]:
		card_label.config(fg=card_color[2])
	elif card_text.get() == card_suit[3]:
		card_label.config(fg=card_color[3])
	
def answer_display():	

	# update the answer text
	if card_text.get()==card_suit[0]:
		answer_text.set(card_name[0])
	elif card_text.get()==card_suit[1]:
		answer_text.set(card_name[1])
	elif card_text.get()==card_suit[2]:
		answer_text.set(card_name[2])
	elif card_text.get()==card_suit[3]:
		answer_text.set(card_name[3])

	button_text.set('Next') # update the button

def change():

	if button_text.get() == 'Check':
		answer_display()
	elif button_text.get() == 'Next':
		card_display()

window = tkinter.Tk()

button_text = tkinter.StringVar()
button_text.set('Check')

answer_text = tkinter.StringVar()
answer_text.set('')

card_text = tkinter.StringVar()
card_text.set(card_suit[random.randint(0,3)])

answer_label = tkinter.Label(window,bg='white',fg='black',textvariable=answer_text)
answer_label.config(font=("Arial", 25))
answer_label.pack(pady = (50, 0))

card_label = tkinter.Label(window,bg='white',width=2,height=1,textvariable=card_text)
card_label.config(font=("Arial", 150))
card_label.pack(pady = (25, 50))

card_display()

button = tkinter.Button(window, textvariable=button_text, width=15, command = change)
button.config(font=("Arial", 20))
button.pack()

window.title('Card Suits')
window.geometry("550x500")
window.config(background = 'white')
window.mainloop()

# end of program
