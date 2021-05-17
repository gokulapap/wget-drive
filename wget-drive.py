#/usr/bin/python3
#script to download drive file links by wget

from os import system

link = input("Enter the drive link : ")
out = input("Enter the output file name: ")
size = input("whether the file size is less than 100MB ? (Y/N) : ")

parts = link.split('/')
fileid = parts[5]

# if the size is less than 100MB - Y from input
if size == 'Y' or size == 'y':
  system("wget --no-check-certificate 'https://docs.google.com/uc?export=download&id={}' -O {}".format(fileid, out))

else:
  system("wget --load-cookies \/tmp\/cookies.txt \"https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id={}' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id={}\" -O {} && rm -rf /tmp/cookies.txt".format(fileid, fileid, out))
