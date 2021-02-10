import time
import random
import os
from playsound import playsound
from mutagen.mp3 import MP3


def playSong(songs):
    count = 0
    songRepeat = ""
    while True:
        # picks song at random, sets up name so that bot can process it
        # also checks and makes sure it doesnt repeat the previous song
        while True:
            song = random.randint(0, 11)
            chosen = songs[song].replace("\n", "")

            if songRepeat == "":
                songRepeat = chosen
                break
            elif chosen == songRepeat:
                continue
            else:
                songRepeat = chosen
                break

        # sets the directory for playsound()
        directory = os.path.dirname(os.path.abspath(__file__))
        print("Now Playing: ", chosen.replace(".mp3", ""))

        # sets how long the program will sleep for
        # when song is finished
        audio = MP3(chosen)
        sleepTime = 300 - round(audio.info.length)
        songLength = round(audio.info.length)
        print("Song Length: ", songLength, " seconds")

        # plays the chosen song, then goes to sleep
        chosenSong = directory + ("\\" + chosen)
        playsound(chosenSong)
        count += 1
        print("Songs Played: ", count)
        print("Time to Next: ", sleepTime, " seconds")
        print()

        time.sleep(sleepTime)


def main():
    # opens list of songs, then sends it to the playSong() method
    songList = open("musicList.txt", "r")
    songList = songList.readlines()
    playSong(songList)


main()
