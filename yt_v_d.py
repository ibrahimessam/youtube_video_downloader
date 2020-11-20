# THIS CODE FOR DOWNLOAD VIDEO FROM YOUTUBE IT'S VERY EASY CODE

import pytube

url = input("Enter here Youtube Video URL :> ")

youtube = pytube.Youtube(url)

video = youtube.streams.first()

video.dewnload()
