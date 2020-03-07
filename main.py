from pygame import mixer as player
from mutagen.mp3 import MP3 as mp3
from time import sleep
import os

# variables begin
curTrack = ""
curList = ""

player.init(frequency=44000)
music_dir = "musics/"
TrackLists = []
help_message = """
    Commands:
        play xxx : Plays the track xxx
            ex: play oldies/Pixies Where is my mind.mp3
        
        volume x.x : Sets volume to entered float, ex:0.3 - the max is 1.0
        
        list x : Plays the detected list x
            it will automaticly cycle the list and stops.
        
        show_lists : Shows detected lists. 
            This command will shows all lists that detected at the start.
            Note that you must put your mp3 files in music folder.
            The program will add the same list, if the files are in same folder  
            
        help : Shows help
        
        about : Shows the program details
        
        exit : Exits the program
"""
enterance_msg = " - PyPlayer 1.0.0          type help for available commands... \n"
# variables end

def create_lists():
    # list creator
    # Input: NONE, OUTPUT: Tracklists[]
    for s, f, d in os.walk(music_dir):
        for folder in f:
            list = []
            folder = "musics/" + str(folder)
            for file in os.listdir(folder):
                if file.endswith(".mp3"):
                    list.append(folder+"/"+str(file))
            TrackLists.append(list)
    for e in TrackLists:
        print(e)

def playTrack(track):
    # track player
    # Input: sound file, Output: Sound
    global curTrack
    trackPath = music_dir + track
    print(" - Playing:" + str(track))
    curTrack = track
    player.music.load(trackPath)
    player.music.play()

def playList(number):
    # list player
    # Input: List ID in TrackLists[], Output: Sound
    global curList
    id = int(number) - 1
    cur_list = TrackLists[id]
    print(" - Playing the list:"+str(cur_list))
    curList = cur_list
    for track in cur_list:
        audio = mp3(track)
        length = audio.info.length + 3.0
        player.music.load(track)
        player.music.play(1)
        minutes = int(length) / 60
        print(" - Playing: " + track + "  Lenght:"+str(minutes)+ " minutes.")
        sleep(length)

############################################################################################################################################################################################################################################

def cmd():
    print(enterance_msg)
    create_lists()
    while True:
        global player
        cmd = input(">")
        player.music.set_volume(0.5)
        if cmd == "help":
            print(help_message)
        if cmd[0:4] == "play":
            track = cmd[5:]
            playTrack(track)
        if cmd[0:4] == "list":
            number = cmd[5:]
            playList(number)
        if cmd == "about":
            print(" PyPlayer, command line mp3 player. Created by Kubilay Gezer.     07.03.2020 : 19.06")
        if cmd[0:3] == "vol":
            volume = cmd[4:]
            volume = float(volume)
            try:
                player.music.set_volume(volume)
            except ValueError:
                print(" - This must be a float.")
                pass
        if cmd == "exit":
            break

cmd()