#!/usr/bin/env python3
import os
import subprocess
import sys

def check():
    try:
        subprocess.run(["yt-dlp", "--version"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(["ffmpeg", "-version"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        import termcolor
        return True
    except:
        local_yt = os.path.expanduser("~/.local/bin/yt-dlp")
        if os.path.exists(local_yt):
            return True
        return False

def detect_manager():
    if os.system("command -v apt > /dev/null 2>&1") == 0:
        return "apt"
    elif os.system("command -v pacman > /dev/null 2>&1") == 0:
        return "pacman"
    elif os.system("command -v dnf > /dev/null 2>&1") == 0:
        return "dnf"
    else:
        return None

if check () :
    print ("every thing is ready !")
    pass
else:
    auto = input ("you missing some packeges would you like to download it automaticly ?\nyes//no\n")   

    if auto == "yes" :
        manager = detect_manager()
        if manager == "apt" : 
            subprocess.run ([sys.executable , "-m" , "pip" , "install", "yt-dlp", "--break-system-packages"])  
            subprocess.run (["sudo", "apt", "install", "ffmpeg", "-y"])
            subprocess.run ([sys.executable , "-m" , "pip" , "install" , "termcolor" , "--break-system-packages"])
        elif manager == "pacman" :
            subprocess.run (["sudo" , "pacman" , "-S" , "yt-dlp"])
            subprocess.run (["sudo" , "pacman" , "-S" , "ffmpeg"])
            subprocess.run ([sys.executable , "-m" , "pip" , "install" , "termcolor"])
        elif manager == "dnf" :
            subprocess.run (["sudo" , "dnf" , "install" , "yt-dlp"])
            subprocess.run (["sudo" , "dnf" , "install" , "ffmpeg"])
            subprocess.run([sys.executable , "-m" , "pip" , "install" , "termcolor"])
        else :
            print (colored("Sorry the download faild" , "red"))
    elif auto == "no" :
        print ("ok download pkgs and then restart the app")
    if not check :
        print ("somthing went wrong try again")

import termcolor
from termcolor import colored

if not check() :
    sys.exit()

input (colored(f"Enter to contenue...." , "yellow"))

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

                
              >>Youtube Download Tool 2.0<<      
    '''
   
   
    print(colored(logo, "cyan"))



CONFIG_FILE = "config.txt"
if not os.path.exists(CONFIG_FILE):
    print(colored(f"\nWelcome !\nThis app will make yt-dlp much easier!", "yellow"))
    download_path = input("Where do you want videos to be saved?\n")
    download_path = os.path.expanduser(download_path)
    os.makedirs(download_path, exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        f.write(download_path)
        print (colored("The file will be saved is : " , "green") + download_path)
    input(colored("Press Enter to continue..." , "yellow"))
else:
    with open(CONFIG_FILE) as f:
        download_path = f.read().strip()


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

while True :
    formats_1 = {
    "1": 'bv*[vcodec^=avc1][height<=2160]+ba[acodec^=mp4a]/b[height<=2160]',  # 4K
    "2": 'bv*[vcodec^=avc1][height<=1440]+ba[acodec^=mp4a]/b[height<=1440]',  # 2K
    "3": 'bv*[vcodec^=avc1][height<=1080]+ba[acodec^=mp4a]/b[height<=1080]',  # 1080p
    "4": 'bv*[vcodec^=avc1][height<=720]+ba[acodec^=mp4a]/b[height<=720]',    # 720p
    "5": 'bv*[vcodec^=avc1][height<=480]+ba[acodec^=mp4a]/b[height<=480]',    # 480p
    }

    
    subprocess.run(["clear"])
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

        #cmd code to download video
        cmd = ["yt-dlp" , 
        "-f" , formats_1[quality] ,
        "--merge-output-format", "mp4",
        "-o", f"{download_path}/%(title)s.mp4",
        url 
            ]


        name = get_filename(url)
        if os.path.exists(name):
            print(colored("The file exists already !", "green"))
        if quality == "1" :
            result = subprocess.run(cmd)
            after_dow(result)
            input (colored("Enter to continue" , "red"))
        elif quality == "2" :
            result = subprocess.run(cmd)
            after_dow(result)
            input (colored("Enter to continue" , "red"))
        elif quality == "3" :
            result = subprocess.run(cmd)
            after_dow(result)
            input (colored("Enter to continue" , "red"))
        elif quality == "4" :
            result = subprocess.run(cmd)
            after_dow(result)
            input (colored("Enter to continue" , "red"))
        elif quality == "5" : 
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
            "-o", f"{download_path}%(playlist_title)s/%(title)s.mp4" ,
            url 
                ]
            if os.path.exists(name):
                print(colored("The file exists already !", "green"))
            if quality == "1" :
                result = subprocess.run(cmd)
                after_dow(result)
                input (colored("Enter to continue" , "red"))
            elif quality == "2" :
                result = subprocess.run(cmd)
                after_dow(result)
                input (colored("Enter to continue" , "red"))
            elif quality == "3" :
                result = subprocess.run(cmd)
                after_dow(result)
                input (colored("Enter to continue" , "red"))
            elif quality == "4" :
                result = subprocess.run(cmd)
                after_dow(result)
                input (colored("Enter to continue" , "red"))
            elif quality == "5" : 
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
            "-o", f"{download_path}/%(title)s.mp4",
            url 
                ]

            if quality == "1" :
                result = subprocess.run(cmd)
                after_dow(result)
                input (colored("Enter to continue" , "red"))
            elif quality == "2" :
                result = subprocess.run(cmd)
                after_dow(result)
                input (colored("Enter to continue" , "red"))
            elif quality == "3" :
                result = subprocess.run(cmd)
                after_dow(result)
                input (colored("Enter to continue" , "red"))
            elif quality == "4" :
                result = subprocess.run(cmd)
                after_dow(result)
                input (colored("Enter to continue" , "red"))
            elif quality == "5" : 
                result = subprocess.run(cmd)
                after_dow(result)
                input (colored("Enter to continue" , "red"))
    elif choice == "3" :
        file_choice = input(colored(f"Do you want a file for a play list ?  \n yes // no \n>  " , "yellow"))
        url = input ("Please enter URL: \n")
        if file_choice.lower() == "yes" :
            resault = subprocess.run([
                'yt-dlp',
                '-x',
                '--audio-format', 'mp3',
                '--audio-quality', '0',
                '-o', f"{download_path}/%(playlist_index)s - %(title)s.%(ext)s",
             url
            ])
            after_dow(result)                
            input (colored("Enter to continue" , "red"))
        elif file_choice.lower() == "no" :
            resault = subprocess.run([
                'yt-dlp',
                '-x',
                '--audio-format', 'mp3',
                '--audio-quality', '0',
                '-o', f"{download_path}/%(title)s.mp3",
                url
            ])
            after_dow(result)                
            input (colored("Enter to continue" , "red"))
    elif choice == "4" :
        break
    elif choice == "5" :
            os.system("nano errors.txt")
    elif choice == "6" :
        os.system("nano help.txt")

