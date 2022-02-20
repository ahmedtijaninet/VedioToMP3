import os
import sys

#get directory
try:
    foldername = str(sys.argv[1])
except:
    foldername = input("folder name :")
#create audio folder
if not os.path.exists('audio'):
    os.makedirs('audio')
#get list files
path = os.listdir(foldername)

