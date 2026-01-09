#!/usr/bin/env python3
import os
import subprocess
import sys

def check():
    try:
        subprocess.run(["yt-dlp", "--version"], check=True, stdout=subprocess.DEVNULL)
        subprocess.run(["ffmpeg", "-version"], check=True, stdout=subprocess.DEVNULL)
        import termcolor
        return True
    except:
        return False
if check() == False :
    choice_down = input ("We found some messing packeges would you like to install them automaticly?")
    if choice_down == "yes" :
        subprocess.run(["sudo", "apt" , "install" ,"yt-dlp" ,  "-y"])
        subprocess.run(["sudo", "apt", "install" , "ffmpeg" , "-y"])
        subprocess.run(["python3" , "-m" , "pip" , "install", "-U" , "termcolor"])
    elif choice_down == "no" :
        input ("Ok when you done restart the app \nEnter to continue....")
        sys.exit()

import termcolor
from termcolor import colored

print (colored(f"\n\nAll packeges have been found!\n\n" , "green"))
input (colored(f"Enter to contenue...." , "yellow"))

# python3 -m pip install -U termcolor


def show_logo():
    logo = r'''


/**
 *              __              __                .__   
 *     ___.__._/  |_   ______ _/  |_  ____   ____ |  |  
 *    <   |  |\   __\ /_____/ \   __\/  _ \ /  _ \|  |  
 *     \___  | |  |   /_____/  |  | (  <_> |  <_> )  |__
 *     / ____| |__|            |__|  \____/ \____/|____/
 *     \/                                               
 */
                         /\_/\
                        ((@v@))
                        ():::()
                         VV-VV

                
                >>Youtube Download Tool<<      
    '''
   
   
    print(colored(logo, "cyan"))



# CONFIG_FILE = "config.txt"
# if not os.path.exists(CONFIG_FILE):
#     print(colored(f"\nWelcome !\nThis app will make yt-dlp much easier!", "yellow"))
#     download_path = input("Where do you want videos to be saved?\n")
#     download_path = os.path.expanduser(download_path)
#     os.makedirs(download_path, exist_ok=True)
#     with open(CONFIG_FILE, "w") as f:
#         f.write(download_path)
#         print (colored("The file will be saved is : " , "green") + download_path)
#     input(colored("Press Enter to continue..." , "yellow"))
# else:
#     with open(CONFIG_FILE) as f:
#         download_path = f.read().strip()


def get_filename(url):
    return subprocess.check_output(
        ['yt-dlp', '--get-filename', '-o', '%(title)s.%(ext)s', url],
        text=True
    ).strip()


def after_dow(result):
    if result.returncode == 0:
        print(colored("Success !!!", "green"))
    else:
        print(colored("Download failed ", "red"))


    print ("no")
while True :
    if check() == False :
        print("you have some packeges messing")
        sys.exit()


    formats_1 = {
    "1": 'bv*[vcodec^=avc1][height<=2160]+ba[acodec^=mp4a]/b[height<=2160]',  # 4K
    "2": 'bv*[vcodec^=avc1][height<=1440]+ba[acodec^=mp4a]/b[height<=1440]',  # 2K
    "3": 'bv*[vcodec^=avc1][height<=1080]+ba[acodec^=mp4a]/b[height<=1080]',  # 1080p
    "4": 'bv*[vcodec^=avc1][height<=720]+ba[acodec^=mp4a]/b[height<=720]',    # 720p
    "5": 'bv*[vcodec^=avc1][height<=480]+ba[acodec^=mp4a]/b[height<=480]',    # 480p
    }


    os.system("clear")
    show_logo()
    print (colored("\nPlease choose one of this :" , "cyan"))
    print (colored("1) " , "yellow") + ("Download a vedio"))
    print (colored("2) " , "yellow") + ("Download a playlist"))
    print (colored("3) " , "yellow") + ("Download sound from vedio"))
    print (colored("4) " , "yellow") + ("Exit"))
    print (colored("5) " , "yellow") + ("Common errors"))
    print (colored("6) " , "yellow") + ("Help"))
    choice = input (colored("> " , "cyan"))
    if choice == "1" : 
        print (colored("Please choose a quality" , "yellow"))
        print (colored("1) " , "yellow") + ("4k"))
        print (colored("2) " , "yellow") + ("2k"))
        print (colored("3) " , "yellow") + ("1080p"))
        print (colored("4) " , "yellow") + ("720p"))
        print (colored("5) " , "yellow") + ("420p"))
        quality = input (colored("What quality you want?\n >  " , "yellow"))
        url = input (colored("Please paste URL: \n>  " , "yellow"))

        cmd = ["yt-dlp" , 
        "-f" , formats_1[quality] ,
        "--merge-output-format", "mp4",
        "-o", "%(title)s.mp4",
        url 
            ]

        name = get_filename(url)
        if os.path.exists(name):
            print(colored("The file exists already !", "green"))
        if quality == "1" :
            subprocess.run(cmd)
            result = subprocess.run(cmd)
            after_dow(result)
            input (colored("Enter to continue" , "red"))
        elif quality == "2" :
            subprocess.run(cmd)
            result = subprocess.run(cmd)
            after_dow(result)     
            input (colored("Enter to continue" , "red"))
        elif quality == "3" :
            subprocess.run(cmd)
            result = subprocess.run(cmd)
            after_dow(result)
            input (colored("Enter to continue" , "red"))
        elif quality == "4" :
            subprocess.run(cmd)
            result = subprocess.run(cmd)
            after_dow(result)            
            input (colored("Enter to continue" , "red"))
        elif quality == "5" : 
            subprocess.run(cmd)
            result = subprocess.run(cmd)
            after_dow(result)            
            input (colored("Enter to continue" , "red"))
        else :
            print (colored("please try again" , "cyan"))


    elif choice == "2" :
        file_choice = input(colored("Do you want a file for a play list ? \n yes // no \n>   " , "yellow"))
        if file_choice.lower() == "yes" :
            print (colored("Please choose a quality" , "yellow"))
            print (colored("1) " , "yellow") + ("4k"))
            print (colored("2) " , "yellow") + ("2k"))
            print (colored("3) " , "yellow") + ("1080p"))
            print (colored("4) " , "yellow") + ("720p"))
            print (colored("5) " , "yellow") + ("420p"))
            quality = input (colored("> " , "cyan"))
            url = input (colored("Please paste a URL: \n>  " , "yellow"))
            name = get_filename(url)
            cmd = ["yt-dlp" , 
            "-f" , formats_1[quality] ,
            "--merge-output-format", "mp4",
            "-o", '"%(playlist_title)s/%(title)s.mp4"',
            url 
                ]
            if os.path.exists(name):
                print(colored("The file exists already !", "green"))
            if quality == "1" :
                subprocess.run(cmd)
                result = subprocess.run(cmd)
                after_dow(result)                
                input (colored("Enter to continue" , "red"))
            elif quality == "2" :
                subprocess.run(cmd)
                result = subprocess.run(cmd)
                after_dow(result)                
                input (colored("Enter to continue" , "red"))
            elif quality == "3" :
                subprocess.run(cmd)
                result = subprocess.run(cmd)
                after_dow(result)                
                input (colored("Enter to continue" , "red"))
            elif quality == "4" :
                subprocess.run(cmd)
                result = subprocess.run(cmd)
                after_dow(result)                
                input (colored("Enter to continue" , "red"))
            elif quality == "5" : 
                subprocess.run(cmd)
                result = subprocess.run(cmd)
                after_dow(result)                
                input (colored("Enter to continue" , "red"))
        elif file_choice.lower() == "no" :
            print (colored("Please choose a quality" , "yellow"))
            print (colored("1) " , "yellow") + ("4k"))
            print (colored("2) " , "yellow") + ("2k"))
            print (colored("3) " , "yellow") + ("1080p"))
            print (colored("4) " , "yellow") + ("720p"))
            print (colored("5) " , "yellow") + ("420p"))
            quality = input (colored("What quality you want?\n>  " , "yellow"))
            url = input ("Please paste a URL: \n")
            cmd = ["yt-dlp" , 
            "-f" , formats_1[quality] ,
            "--merge-output-format", "mp4",
            "-o", "%(title)s.mp4",
            url 
                ]
            if quality == "1" :
                subprocess.run(cmd)
                result = subprocess.run(cmd)
                after_dow(result)                
                input (colored("Enter to continue" , "red"))
            elif quality == "2" :
                subprocess.run(cmd)
                result = subprocess.run(cmd)
                after_dow(result)                
                input (colored("Enter to continue" , "red"))
            elif quality == "3" :
                subprocess.run(cmd)
                result = subprocess.run(cmd)
                after_dow(result)                
                input (colored("Enter to continue" , "red"))
            elif quality == "4" :
                subprocess.run(cmd)
                result = subprocess.run(cmd)
                after_dow(result)                
                input (colored("Enter to continue" , "red"))
            elif quality == "5" : 
                subprocess.run(cmd)
                result = subprocess.run(cmd)
                after_dow(result)                
                input (colored("Enter to continue" , "red"))
    elif choice == "3" :
        file_choice = input(colored(f"Do you want a file for a play list ?  \n yes // no \n>  " , "yellow"))
        url = input ("Please enter URL: \n")
        if file_choice.lower() == "yes" :
            subprocess.run([
                'yt-dlp',
                '-x',
                '--audio-format', 'mp3',
                '--audio-quality', '0',
                '-o', '%(playlist_index)s - %(title)s.%(ext)s',
             url
            ])
            result = subprocess.run(cmd)
            after_dow(result)                
            input (colored("Enter to continue" , "red"))
        elif file_choice.lower() == "no" :
            subprocess.run([
                'yt-dlp',
                '-x',
                '--audio-format', 'mp3',
                '--audio-quality', '0',
                '-o', '%(title)s.%(ext)s',
                url
            ])
            result = subprocess.run(cmd)
            after_dow(result)                
            input (colored("Enter to continue" , "red"))
    elif choice == "4" :
        break
    elif choice == "5" :
            os.system("nano errors.txt")
    elif choice == "6" :
        os.system("nano help.txt")

