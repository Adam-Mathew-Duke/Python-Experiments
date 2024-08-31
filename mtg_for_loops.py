# MTG for loop example

# card name and rarity
MTG_Dictionary={'Copy Artifact':'rare','Polluted Delta':'rare','Wheel of Fortune':'rare','Bazaar of Baghdad':'common'}

# only print the rare cards
print('List of rare cards:')
for key,value in MTG_Dictionary.items():
    if (value == 'rare'):
        print(key)

# only print the common cards
print('\nList of common cards:')
for key,value in MTG_Dictionary.items():
    if (value == 'common'):
        print(key)

# end of program
