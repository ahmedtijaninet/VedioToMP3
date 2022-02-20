import os
from config import *
from convert import convert

for filename in path:           
    audioname=str(filename[:-4])
    mp4_file =(foldername+filename)
    mp3_file =(r"audio/"+audioname+".mp3")
    try:
        convert(mp4_file, mp3_file)
    except:
        print("bad file!")
