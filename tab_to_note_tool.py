'''
Name:           Guitar tab to note tool
Description:    Converts guitar tab to note
Version:        1
'''

'''
1. Get the range of notes a guitar can play
2. Gather all the data for TAB and Note Names
3. Make the program as a terminal version
4. Refine the code and add useful comments
'''

guitar_string = 0
guitar_fret = 0

input_guitar_string = input("TAB String Number: ");
input_guitar_fret = input("TAB Fret Number: ");

input_guitar_string = int(input_guitar_string)
input_guitar_fret = int(input_guitar_fret)

if input_guitar_string == 0 and input_guitar_fret == 0:
    print ("Low E - Open String")

# end of code
