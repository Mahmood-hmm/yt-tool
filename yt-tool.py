#!/usr/bin/env python3
import os
import subprocess
import sys

pbar = None



def check_termcolor():
    try:
        import termcolor
        return True
    except ImportError:
        return False



if check_termcolor() == False :
    print ("\n\n\nplease wail installing some items to program \n\n\n\n")
    os.system("python3 -m pip install -U termcolor")

import termcolor
from termcolor import colored

def check_items() : 
    try :
        os.system ("yt-dlp --version")
        return True
    except version :
        return False
if check_items() == False :
    down_choice = input (colored("yt-dlp have not foind do you want to install it? \n" , "yellow"))
    if down_choice() == "yes" :
        os.system("python3 -m pip install -U yt-dlp")
    elif down_choice() == "no" : 
        exit



def show_logo():
    logo = r'''



                                                   
           ,--.           ,--.                ,--. 
,--. ,--.,-'  '-.,-----.,-'  '-. ,---.  ,---. |  | 
 \  '  / '-.  .-''-----''-.  .-'| .-. || .-. ||  | 
  \   '    |  |           |  |  ' '-' '' '-' '|  | 
.-'  /     `--'           `--'   `---'  `---' `--' 
`---'                                              
                     /\_/\
                    ( o.o )
                     > ^ <

       >> Youtube Downloader Tool v1.0 <<      
    '''
   
   
    print(colored(logo, "cyan"))



CONFIG_FILE = "config.txt"
if not os.path.exists(CONFIG_FILE):
    print(colored("Welcome !\nThis app will make yt-dlp much easier!", "yellow"))
    download_path = input("Where do you want videos to be saved?\n")
    download_path = os.path.expanduser(download_path)
    os.makedirs(download_path, exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        f.write(download_path)
        print (colored("The file will be saved is : ") + download_path)
    input("Press Enter to continue...")
else:
    with open(CONFIG_FILE) as f:
        download_path = f.read().strip()



def check():
    try:
        subprocess.run(["yt-dlp", "--version"], check=True, stdout=subprocess.DEVNULL)
        subprocess.run(["ffmpeg", "-version"], check=True, stdout=subprocess.DEVNULL)
        return True
    except:
        return False
if check() == False :
    os.system("sudo apt install yt-dlp -y")
    os.system("sudo apt install ffmpeg -y")


def get_filename(url):
    return subprocess.check_output(
        ['yt-dlp', '--get-filename', '-o', '%(title)s.mp4', url],
        text=True
    ).strip()


def after_dow(url) : 
    name = get_filename(url)
    if os.path.exists(name):
        print (colored("Success !!!" , "green"))
    else :
        print (colored("Sorry download failed or file not found"  , "red"))




while True :
    os.system("clear")
    show_logo()
    print ("\nPlease choose one of this :")
    print (colored("1) " , "yellow") + ("Download a vedio"))
    print (colored("2) " , "yellow") + ("Download a playlist"))
    print (colored("3) " , "yellow") + ("Download sound from vedio"))
    print (colored("4) " , "yellow") + ("Exit"))
    print (colored("5) " , "yellow") + ("Common errors"))
    print (colored("6) " , "yellow") + ("Help"))
    choice = input ()
    if choice == "1" : 
        print (colored("Please choose a quality" , "yellow"))
        print (colored("1) " , "yellow") + ("4k"))
        print (colored("2) " , "yellow") + ("2k"))
        print (colored("3) " , "yellow") + ("1080p"))
        print (colored("4) " , "yellow") + ("720p"))
        print (colored("5) " , "yellow") + ("420p"))
        quality = input (colored("What quality you want?\n" , "yellow"))
        url = input ("Please paste a URL: \n")
        name = get_filename(url)
        if os.path.exists(name):
            print(colored("The file exists already !", "green"))
        if quality == "1" :
            os.system('yt-dlp -f "bv*[vcodec^=avc1][height<=2160]+[acodec^=mp4a]/b [haight<=2160]" --merge-output-format mp4 -o "%(title)s.mp4" ' + url)
            after_dow(url)
            input (colored("Enter to continue" , "red"))
        elif quality == "2" :
            os.system('yt-dlp -f "bv*[vcodec^=avc1][height<=1440]+[acodec^=mp4a]/b [haight<=1440]" --merge-output-format mp4 -o "%(title)s.mp4" ' + url)
            after_dow(url)
            input (colored("Enter to continue" , "red"))
        elif quality == "3" :
            os.system('yt-dlp -f "bv*[vcodec^=avc1][height<=1080]+[acodec^=mp4a]/b [haight<=1080]" --merge-output-format mp4 -o "%(title)s.mp4" ' + url)
            after_dow(url)
            input (colored("Enter to continue" , "red"))
        elif quality == "4" :
            os.system('yt-dlp -f "bv*[vcodec^=avc1][height<=720]+[acodec^=mp4a]/b [haight<=720]" --merge-output-format mp4 -o "%(title)s.mp4" ' + url)
            after_dow(url)
            input (colored("Enter to continue" , "red"))
        elif quality == "5" : 
            os.system('yt-dlp -f "bv*[vcodec^=avc1][height<=480]+[acodec^=mp4a]/b [haight<=480]" --merge-output-format mp4 -o "%(title)s.mp4" ' + url)
            after_dow(url)
            input (colored("Enter to continue" , "red"))
    elif choice == "2" :
        file_choice = input("Do you want a file for a play list ?  **answear with yes or no**\n")
        if file_choice.lower() == "yes" :
            print (colored("Please choose a quality" , "yellow"))
            print (colored("1) " , "yellow") + ("4k"))
            print (colored("2) " , "yellow") + ("2k"))
            print (colored("3) " , "yellow") + ("1080p"))
            print (colored("4) " , "yellow") + ("720p"))
            print (colored("5) " , "yellow") + ("420p"))
            quality = input (": ")
            url = input (colored("Please paste a URL: \n" , "yellow"))
            name = get_filename(url)
            if os.path.exists(name):
                print(colored("The file exists already !", "green"))
            if quality == "1" :
                os.system('yt-dlp -f "bv*[vcodec^=avc1][height<=2160]+[acodec^=mp4a]/b [haight<=2160]" --merge-output-format mp4 -o "%(playlist_title)s/%(title)s.mp4" ' + url)
                after_dow(url)
                input (colored("Enter to continue" , "red"))
            elif quality == "2" :
                os.system('yt-dlp -f "bv*[vcodec^=avc1][height<=1440]+[acodec^=mp4a]/b [haight<=1440]" -o "%(playlist_title)s/%(title)s.mp4" ' + url)
                after_dow(url)
                input (colored("Enter to continue" , "red"))
            elif quality == "3" :
                os.system('yt-dlp -f "bv*[vcodec^=avc1][height<=1080]+[acodec^=mp4a]/b [haight<=1080]" -o "%(playlist_title)s/%(title)s.mp4" ' + url )
                after_dow(url)
                input (colored("Enter to continue" , "red"))
            elif quality == "4" :
                os.system('yt-dlp -f "bv*[vcodec^=avc1][height<=720]+[acodec^=mp4a]/b [haight<=720]" -o "%(playlist_title)s/%(title)s.mp4" ' + url)
                after_dow(url)
                input (colored("Enter to continue" , "red"))
            elif quality == "5" : 
                os.system('yt-dlp -f "bv*[vcodec^=avc1][height<=480]+[acodec^=mp4a]/b [haight<=480]" -o "%(playlist_title)s/%(title)s.mp4" ' + url)
                after_dow(url)
                input (colored("Enter to continue" , "red"))
        elif file_choice.lower() == "no" :
            print (colored("Please choose a quality" , "yellow"))
            print (colored("1) " , "yellow") + ("4k"))
            print (colored("2) " , "yellow") + ("2k"))
            print (colored("3) " , "yellow") + ("1080p"))
            print (colored("4) " , "yellow") + ("720p"))
            print (colored("5) " , "yellow") + ("420p"))
            quality = input ("What quality you want?\n")
            url = input ("Please paste a URL: \n")
            if quality == "1" :
                os.system('yt-dlp -f "bv*[vcodec^=avc1][height<=2160]+[acodec^=mp4a]/b [haight<=2160]" --merge-output-format mp4 -o "%(title)s.mp4" ' + url)
                after_dow(url)
                input (colored("Enter to continue" , "red"))
            elif quality == "2" :
                os.system('yt-dlp -f "bv*[vcodec^=avc1][height<=1440]+[acodec^=mp4a]/b [haight<=1440]"  --merge-output-format mp4 -o "%(title)s.mp4" ' + url)
                after_dow(url)
                input (colored("Enter to continue" , "red"))
            elif quality == "3" :
                os.system('yt-dlp -f "bv*[vcodec^=avc1][height<=1080]+[acodec^=mp4a]/b [haight<=1080]" --merge-output-format mp4  -o "%(title)s.mp4" ' + url )
                after_dow(url)
                input (colored("Enter to continue" , "red"))
            elif quality == "4" :
                os.system('yt-dlp -f "bv*[vcodec^=avc1][height<=720]+[acodec^=mp4a]/b [haight<=720]" --merge-output-format mp4 -o "%(title)s.mp4" ' + url)
                after_dow(url)
                input (colored("Enter to continue" , "red"))
            elif quality == "5" : 
                os.system('yt-dlp -f "bv*[vcodec^=avc1][height<=480]+[acodec^=mp4a]/b [haight<=480]" --merge-output-format mp4 -o "%(title)s.mp4" ' + url)
                after_dow(url)
                input (colored("Enter to continue" , "red"))
    elif choice == "3" :
        file_choice = input("Do you want a file for a play list ?  **answear with yes or no**\n")
        url = input ("Please enter URL: \n")
        if file_choice.lower() == "yes" :
            os.system('yt-dlp -x --audio-format mp3 --audio-quality 0 -o "%(playlist_index)s - %(title)s.%(ext)s" ' + url)
        elif file_choice.lower() == "no" :
            os.system('yt-dlp -x --audio-format mp3 --audio-quality 0 -o - "%(title)s.%(ext)s" ' + url)
    elif choice == "4" :
        break
    elif choice == "5" :
            os.system("nano errors.txt")
    elif choice == "6" :
        os.system("nano help.txt")

