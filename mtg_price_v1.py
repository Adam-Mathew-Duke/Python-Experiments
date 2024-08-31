'''
MTG Card Price
Version 2 - adds the ability to save to a text file
Notes Works well, will do further refining and improving
'''

import scrython
from sf_price_fetcher import fetcher
import os

while True:

    os.system('cls')
    card_prompt = input("\nEnter card name, type random or exit: ")
    card_prompt = card_prompt.upper()
    print ("\n")
    
    if card_prompt == "EXIT":
        break;

    try:
        if card_prompt == "RANDOM":
            card = scrython.cards.Random()
        else:
            card = scrython.cards.Named(fuzzy=card_prompt)
    except:
        print ("Card not found on Scryfall.\n")
        break
    else:
        print ("Name:\t"+card.name())
        print ("Set:\t"+card.set_name())
        print ("Type:\t"+card.type_line())
        print ("Rarity:\t"+card.rarity())
        print ("Number:\t"+ card.collector_number())

        try:
            card_price = fetcher.get(card.name())   
        except: 
            print("Price: Not found on Scryfall.\n")
            break
        else:
            # display the current USD price
            print("USD:\t$"+str(card_price))
            print ("\n")
        finally:
            save_prompt = input("Press any key to continue, type save or type exit: ")
            save_prompt = save_prompt.upper()
            if save_prompt == "SAVE":
                save_card_data = 1
            if save_prompt == "EXIT":
                print ('\n')
                break
            if save_card_data == 1:
                try:
                    with open("Card_Price_Data.txt", "a") as myfile:
                        myfile.write(card.name())
                        myfile.write(',')
                        myfile.write(str(card_price))
                        myfile.write('\n')
                except:
                    print ('There was an error saving to the file.\n')
                    break
os.system('cls')

# end of code
