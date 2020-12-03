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
        pyautogui.hotkey('alt', 'tab')
        pyautogui.click()

        time.sleep(300)


def main():
    songList = open("musicList.txt", "r")
    songList = songList.readlines()
    playSong(songList)


main()
