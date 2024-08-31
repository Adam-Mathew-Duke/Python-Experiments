# Binaural Beats - Terminal Version

'''
To do:
> Revise code and see what can be imporved.
> Make code as clear and efficient as possible.
> Add comments where useful.
> Done.
'''

import os
from AccelBrainBeat.brainbeat.binaural_beat import BinauralBeat

class create_binural_beat:

    def __init__(self):

        self.left_channel = 130
        self.right_channel = self.left_channel + 10
        self.preview_duration = 5 # plays for x seconds
        self.save_duration = 60 # saves a file x second long
        self.volume = 0.5
        self.beat = BinauralBeat()

    def display_audio_info(self,state):
        
        if state == "play":
            print ("\nNow Playing:")
        elif state == "save":
            print ("\nNow Saving:")
        
        print("Left frequency: "+str(self.left_channel)+"Hz")
        print("Right frequency: "+str(self.right_channel)+"Hz")
        print("Phantom frequency: "+str(self.right_channel-self.left_channel)+"Hz")
        print("Duration: "+str(self.preview_duration))
        print("Volume: "+str(self.volume))

    def create_beat(self,frequency):
        self.left_channel = frequency
        self.right_channel = self.left_channel + 10
        self.display_audio_info("play") 
        self.beat.play_beat(
        	frequencys=(self.left_channel,self.right_channel),
        	play_time=self.preview_duration,
        	volume=self.volume)

    def save_beat(self,frequency):
        self.display_audio_info("save")
        self.left_channel = frequency
        self.right_channel = self.left_channel + 10
        filename = str(self.left_channel) + "Hz - Binural Beat Audio.wav"
        self.beat.save_beat(
            output_file_name=filename,
            frequencys=(self.left_channel,self.right_channel),
        	play_time=self.save_duration,
        	volume=self.volume
        )

def error_message(error_type):

    if error_type == "main_menu_error":
        print("Please enter a choice between 1 and 4")
        input("Press anykey to continue.")

    if error_type == "frequency_menu_error":
        print("130Hz selected as your choice was outside the frequency range.")
        input("Press anykey to continue.")

def main_menu():

    os.system("cls")
    print("\nBinural Beats\n")
    print("1. Set Frequency")
    print("2. Play Beat Preview (5 seconds)")
    print("3. Save Beat (1 minute)")
    print("4. Exit Program\n")
    choice = input("Your choice: ")
    
    try:
        choice = int(choice)
    except:
        error_message("main_menu_error")
        choice = main_menu()
    if choice < 1 or choice > 4:
        error_message("main_menu_error")
        choice = main_menu()
    return choice

choice = main_menu()
choice2 = create_binural_beat().left_channel

while True:

    if choice == 1:
        choice2 = input("Choose frequency (between 130 and 180): ")
        
        try:
            choice2 = int(choice2)
        except:
            error_message("frequency_menu_error")
            choice2 = 130
            choice2 = int(choice2)
        if choice2 < 130 or choice2 > 180:
            error_message("frequency_menu_error")
            choice2 = 130
            choice2 = int(choice2)

        choice = main_menu()

    elif choice == 2:
        beat = create_binural_beat()
        beat.create_beat(choice2)
        choice = main_menu()

    elif choice == 3:
        beat = create_binural_beat()
        beat.save_beat(choice2)
        choice = main_menu()

    elif choice == 4:
        break

# end of code
