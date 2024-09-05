# A program using list, dicts and tuples.

# tuple - immutable keys
key=('1','2','3','4','5')

# list - editable
value=['Apple','Orange','Pear','Grapes','Pineapple']

# dictionary
dictionary={key[0]:value[0],key[1]:value[1],
key[2]:value[2],key[3]:value[3],key[4]:value[4]}

# display results
for key,value in dictionary.items():
    print(key,value)

# end of code
