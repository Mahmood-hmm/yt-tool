#!/usr/bin/env python3
import os
import subprocess
import sys
import platform
import json
import rich
from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from rich.panel import Panel
from rich.align import Align
import time
Console = Console()

def check():
    if platform.system().lower() =="windows" :
        pass
    else:
        try:
            subprocess.run(["yt-dlp", "--version"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return True
        except:
            local_yt = os.path.expanduser("~/.local/bin/yt-dlp")
            if os.path.exists(local_yt):
                return True
            else :
                return False  


def check_ffmpeg() :
    if platform.system().lower() =="windows" :
        pass
    else :
        try :
            subprocess.run(["ffmpeg", "-version"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return True
        except :
            return False



def detect_manager():
    if os.system("command -v apt > /dev/null 2>&1") == 0:
        return "apt"
    elif os.system("command -v pacman > /dev/null 2>&1") == 0:
        return "pacman"
    elif os.system("command -v dnf > /dev/null 2>&1") == 0:
        return "dnf"
    elif os.system("command -v zypper > /dev/null 2>&1") == 0:
        return "zypper"
    else:
        return None


manager = detect_manager() 

if not check() :
    print("You are missing yt-dlp please install befor")
    sys.exit()


if not check_ffmpeg() :
    if platform.system().lower() == "windows" :
        print ("Please put ffmpeg.exe in same file here")
        sys.exit()
    else :
        if manager == "apt" :
            subprocess.run("sudo apt update && sudo apt install ffmpeg -y" , shell=True)
        elif manager == "dnf" :
            subprocess.run(["sudo" ,  "dnf" ,  "install" ,  "ffmpeg" ,  "-y"])
        elif manager == "pacman" :
            subprocess.run(["sudo" , "pacman" ,"-S" ,"ffmpeg" ,"--noconfirm"])
        elif manager == "zypper" :
            subprocess.run(["sudo", "zypper" ,"install" ,"ffmpeg"])


def enter() :
    Console.input("[yellow]Enter to continue[/yellow]")


def logo():
    logo = r'''

            __              __                .__   
    ___.__._/  |_          _/  |_  ____   ____ |  |  
    <   |  |\   __\  ______ \   __\/  _ \ /  _ \|  |  
    \___  | |  |   /_____/  |  | (  <_> |  <_> )  |__
    / ____| |__|            |__|  \____/ \____/|____/
    \/                                               

              >>Youtube Download Tool 3.0<<      
    '''
   
    Console.print(
        Panel(
            logo,
            style="cyan bold",
            title="[white]Welcome[/white]",
            subtitle="[yellow]v4.0[/yellow]",
            expand=False
        )
    )


def owl():
    owl_art = (
r"""
 /\ /\ 
((ovo))
():::()
  VVV  
"""
    )
    centered_owl = Align.center(owl_art, style="cyan bold")

    Console.print(
        Panel(
            centered_owl,
            style="cyan bold",
            title="[white]yt-tool[/white]",
            subtitle="[yellow]v4.0[/yellow]",
            width=30,      
            expand=False,
            padding=(1, 4)  
        )
    )



CONFIG_FILE = "config.txt"
if not os.path.exists(CONFIG_FILE):
    Console.print(f"\nWelcome !\nThis app will make yt-dlp much easier!", style="yellow")
    download_path = Console.input("[cyan]Where do you want videos to be saved?\n[/cyan]")
    download_path = os.path.expanduser(download_path)
    os.makedirs(download_path, exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        f.write(download_path+"\n")
        Console.print ("The file will be saved is : " + download_path)
    Console.input("[yellow]Press Enter to continue...[/yellow]")
else:
    with open(CONFIG_FILE, "r") as f:
        lines = f.readlines()
        download_path = lines[0].strip()



def after_dow(result):
    if platform.system().lower() == "windows" :
        pass
    if result.returncode == 0:
        Console.print("Success !!!", style= "green")
    else:
        Console.print("Download failed ", style="red")



def download(cmd) :
            result = subprocess.run(cmd)
            after_dow(result)



def start_choices () :
    Console.print ("[cyan bold]\nPlease choose one of this :[/cyan bold]")
    Console.print ("[yellow] |1| [/yellow] Video")
    Console.print ("[yellow] |2| [/yellow] Playlist")
    Console.print ("[yellow] |3| [/yellow] Audio")
    Console.print ("[yellow] |4| [/yellow] Download from inestegram or other socioal")
    Console.print ("[yellow] |5| [/yellow] Help")
    Console.print ("[yellow] |6| [/yellow] Exit")



def print_quality() :
        Console.print ("Please choose a quality" , style="cyan bold")
        Console.print ("[yellow] |1| [/yellow] 4k")
        Console.print ("[yellow] |2| [/yellow] 2k")
        Console.print ("[yellow] |3| [/yellow] 1080p")
        Console.print ("[yellow] |4| [/yellow] 720p")
        Console.print ("[yellow] |5| [/yellow] 480p")
        Console.print ("[yellow] |6| [/yellow] back")



def print_audio() :
        Console.print ("[yellow] |1| [/yellow] PlayList as MP3")
        Console.print ("[yellow] |2| [/yellow] Single video as MP3")
        Console.print ("[yellow] |3| [/yellow] back")



def print_social() :
        Console.print ("[yellow] |1| [/yellow] Eny social midea")
        Console.print ("[yellow] |2| [/yellow] back")
 


formats = {
    "1": 'bv*[vcodec^=avc1][height<=2160]+ba[acodec^=mp4a]/b[height<=2160]',  # 4K
    "2": 'bv*[vcodec^=avc1][height<=1440]+ba[acodec^=mp4a]/b[height<=1440]',  # 2K
    "3": 'bv*[vcodec^=avc1][height<=1080]+ba[acodec^=mp4a]/b[height<=1080]',  # 1080p
    "4": 'bv*[vcodec^=avc1][height<=720]+ba[acodec^=mp4a]/b[height<=720]',    # 720p
    "5": 'bv*[vcodec^=avc1][height<=480]+ba[acodec^=mp4a]/b[height<=480]',    # 480p
    }
    


def continuee() :
    Console.input("[yellow]Enter to continue[/yellow]")


def clear () :
        if platform.system().lower() == "windows" :
            pass
        else :
            subprocess.run(["clear"])


def video() :
    while True :
        clear()
        owl()
        print_quality()
        choice = Console.input("[cyan]> [/cyan]")
        if choice in ["1" , "2" , "3" , "4" , "5"] :
            url = Console.input("[yellow]please paste URl:[/yellow] \n[cyan]> [/cyan]")
            cmd = ["yt-dlp" , 
            "-f" , formats[choice] ,
            "--merge-output-format", "mp4",
            "-o", f"{download_path}/%(title)s.mp4",
            url 
                ]
            download(cmd)
            enter()
        elif choice == "6" :
            break
        else :
            Console.print("Please choose one of above")
            time.sleep(2)


def playlist () :
    while True :
        clear()
        owl()
        Console.print("[yellow]Do you want a file for the plalist ?[/yellow] [dim]Details in help[/dim]")
        file_choice = Console.input("[cyan]> [/cyan]")
        print_quality()
        choice = Console.input("[cyan]> [/cyan]")
        if choice in ["1" , "2" , "3" , "4" , "5"] :
            if file_choice.lower() in ["yes" , "y" , ""] :
                url = Console.input("[yellow]Please paste URL :[/yellow]\n[cyan]> [/cyan]")
                cmd = ["yt-dlp" , 
                "-f" , formats[choice] ,
                "--merge-output-format", "mp4",
                "-o", f"{download_path}%(playlist_title)s/%(title)s.mp4" ,
                url 
                    ]
                if choice in ["1" , "2" , "3" , "4" , "5"] :
                    download(cmd)
                    enter()
                else :
                    Console.print("Plese choose one of above" , style="yellow")
            elif file_choice.lower() in ["no" , "n"] :
                url = Console.input("[yellow]Please paste URL :[/yellow]\n[cyan]> [/cyan]")
                cmd = ["yt-dlp" , 
                "-f" , formats[choice] ,
                "--merge-output-format", "mp4",
                "-o", f"{download_path}/%(title)s.mp4",
                url 
                    ]
                if choice in ["1" , "2" , "3" , "4" , "5"] :
                    download(cmd)
                    enter()
                else :
                    Console.print("Plese choose one of above" , style="yellow")
        elif choice == "6" :
            break
        else :
            Console.print("Plese choose one of above" , style="yellow")
            time.sleep(2)


    
def audio() :
    while True :
        clear()
        owl()
        print_audio() 
        choice = Console.input("[cyan]> [/cyan]")
        if choice == "1" :
            Console.print("[yellow]Do you want a file for the plalist ?[/yellow] [dim]Details in help[/dim]")
            file_choice = Console.print("[cyan]> [/cyan]")
            if file_choice.lower() in ["yes" , "y" , ""] :
                url = Console.input("[yellow]Please paste URL :[/yellow][cyan]> [/cyan]")
                cmd = [
                    'yt-dlp',
                    '-x',
                    '--audio-format', 'mp3',
                    '--audio-quality', '0',
                    '-o', f"{download_path}/%(playlist_index)s - %(title)s.%(ext)s",
                    url
                ]
                download(cmd)
                enter()
            elif file_choice.lower() in ["no" , "n"] :
                url = Console.input("[yellow]Please paste URL :[/yellow][cyan]> [/cyan]")
                cmd = [
                    'yt-dlp',
                    '-x',
                    '--audio-format', 'mp3',
                    '--audio-quality', '0',
                    '-o', f"{download_path}/%(title)s.mp3",
                    url
                ]
                download(cmd)
                enter()
        elif choice == "2" :
            url = Console.input("[yellow]Please paste URL :[/yellow][cyan]> [/cyan]")
            cmd = [
                'yt-dlp',
                '-x',
                '--audio-format', 'mp3',
                '--audio-quality', '0',
                '-o', f"{download_path}/%(title)s.mp3",
                url
            ]
            download(cmd)
            enter()
        elif choice == "3" :
            break
        else :
            Console.print("Please choose one of above" , style="yellow")
            time.sleep(2)




def social() :
    while True :
        clear() 
        owl()
        print_social() 
        choice = Console.input("[cyan]> [/cyan]")
        if choice == "1" :
            url = Console.input("[yellow]Please paste URL :[/yellow][cyan]> [/cyan]")
            cmd = [
                "yt-dlp" , 
                url
            ]
            download(cmd)
            enter()
        elif choice == "2" : 
            break



def help() :
    while True :
        subprocess.run(["clear"])
        table = Table(title="Help" , show_lines=True)
        table.add_column("Question" , style="yellow")
        table.add_column("Description" , style="cyan")
        table.add_row("What is this app?" , "yt-tool is a tool to help you download videos or playlists for : free / no ads / eny quality")
        table.add_row("What does it do?" , "Download eny video or playlist")
        table.add_row("What lint project goal?" , "To make it as much as possible")
        table.add_row("Why the app dosent work?" , "There are a lot of common errors like :\n1) Old version of yt-dlp or ffmpeg\n2) You download a privet video/playlist\n3) Quality video/playlist dont have") 
        table.add_row("I didn't like the app style" , "You can easy change style/logo or even add futures this app have clearly to view functions")
        Console.print(table)
        continuee()
        break



def main() :
    while True :
        if platform.system().lower() == "windows" :
            pass
        else :
            subprocess.run(["clear"])
        logo()
        start_choices()
        choice = Console.input("[cyan]> [/cyan]")
        if choice == "1" :
            video()
        elif choice == "2" :
            playlist()
        elif choice == "3" :
            audio()
        elif choice == "4" :
            social()
        elif choice == "5" :
            help() 
        elif choice == "6" :
            break

if __name__== "__main__":

    main()

