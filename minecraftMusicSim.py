import webbrowser
import time
import random
import pyautogui


def playSong(songs):
    while True:
        song = random.randint(0, 11)
        chosen = songs[song].replace("\n", "")
        url = chosen
        new = 1

        webbrowser.open(url, new)
        time.sleep(25)
        pyautogui.press("k")
        time.sleep(1)
        pyautogui.hotkey('alt', 'tab')
        time.sleep(1)

        time.sleep(300)


def main():
    songList = open("musicList.txt", "r")
    songList = songList.readlines()
    playSong(songList)


main()
