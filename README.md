# minecraftMusicSim
Simulates Mincreaft music playing as you work

`````````````````````````````````````````````````````````````````````````````````````````````
Update 13/13/2020:

-No longer uses webbrowser with youtube links
  When using webbrowser, youd have to stop what youre doing and wait for the program to alt+tab
  you back to what you were doing. Also, there would be a chance it never played the video as it
  wouldn't load fast enough. Relied on no ads as well on youtube
  
-User must provide their own copies of the music
  The user must provide .mp3 files that are listed in the musicList.txt, with matching file names.
  I will not provide the .mp3 files for the users so that they have to acquire the files 
  legally/themselves

`````````````````````````````````````````````````````````````````````````````````````````````
`````````````````````````````````````````````````````````````````````````````````````````````
Update 01/07/2021:

-No longer sleeps for 5 minutes between songs
  Previously, the program would always sleep for 5 minutes, instead of just a few minutes depending on 
  song lengthes. When using webbrowser, the program would sleep 5 minutes between the start of each song, 
  making it sound natural. With playsound, it would sleep 5 minutes between the end of the previous song
  and start of next song. This has been fixed to sound natural to Minecraft
  
`````````````````````````````````````````````````````````````````````````````````````````````
