import time
import random
import os
from playsound import playsound
from mutagen.mp3 import MP3
from tqdm import tqdm
from threading import Timer


def songTimer(songLen):
    for _ in tqdm(range(songLen)):
        time.sleep(1)


def playSong(songs):
    count = 0
    songRepeat = ""
    while True:
        # picks song at random, sets up name so that bot can process it
        # also checks and makes sure it doesn't repeat the previous song
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
        # print(directory + ("\\" + chosen))
        print("Now Playing: ", chosen.replace(".mp3", ""))

        # sets how long the program will sleep for
        # when song is finished
        audio = MP3(chosen)
        sleepTime = 300 - round(audio.info.length)
        songLength = round(audio.info.length)
        print("Song Length: ", songLength, " seconds")

        songerTimer = Timer(0.0, songTimer, [songLength])
        songerTimer.start()

        # plays the chosen song, then goes to sleep
        chosenSong = directory + ("\\" + chosen)
        playsound(chosenSong)

        count += 1
        os.system('cls')
        print("Songs Played: ", count)
        print("Time to Next: ", sleepTime, " seconds")
        for _ in tqdm(range(sleepTime)):
            time.sleep(1)
        os.system('cls')


def main():
    # opens list of songs, then sends it to the playSong() method
    songList = open("musicList.txt", "r")
    songList = songList.readlines()
    playSong(songList)


if __name__ == '__main__':
    main()
