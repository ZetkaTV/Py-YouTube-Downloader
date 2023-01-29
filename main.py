from pytube import YouTube
from time import sleep
import os

link = input("YouTube video link: ")
yt = YouTube(link)

print("Title of video: ", yt.title)

print("Views: ", yt.views)

ques = input("Do you want to download this video? (Y/N) >>> ")
if ques == "Y" or "y":
    print("downloading yt video at " + os.getcwd() + "\downloads")
    file = yt.streams.get_highest_resolution()
    file.download(os.getcwd() + "/downloads")
    print("Done downloading requested video!")
    sleep(5)
    exit()
else:
    print("Closing app.")
    sleep(2)
    exit()