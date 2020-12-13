import time
import random
import os
from playsound import playsound


def playSong(songs):
    while True:
        song = random.randint(0, 11)
        chosen = songs[song].replace("\n", "")

        directory = os.path.dirname(os.path.abspath(__file__))
        print(directory + ("\\" + chosen))
        playsound(directory + ("\\" + chosen))
        time.sleep(300)


def main():
    songList = open("musicList.txt", "r")
    songList = songList.readlines()
    playSong(songList)


main()
