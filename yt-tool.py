#!/usr/bin/env python3
import os
import subprocess
import sys
import platform
import json


def check():
    if platform.system().lower() =="windows" :
        pass
    else:
        try:
            subprocess.run(["yt-dlp", "--version"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.run(["ffmpeg", "-version"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            import rich
            return True
        except:
            local_yt = os.path.expanduser("~/.local/bin/yt-dlp")
            if os.path.exists(local_yt):
                return True
            else :
                return False  


def detect_manager():
    if platform.system().lower() == "windows" :
        pass
    elif os.system("command -v apt > /dev/null 2>&1") == 0:
        return "apt"
    elif os.system("command -v pacman > /dev/null 2>&1") == 0:
        return "pacman"
    elif os.system("command -v dnf > /dev/null 2>&1") == 0:
        return "dnf"
    else:
        return None
if check () :
    print ("every thing is ready !" )
else:
    auto = input ("you missing some packeges would you like to download it automaticly ?")   

    if auto.lower() in ["yes" , "y" , ""] :
        manager = detect_manager()
        if manager == "apt" : 
            subprocess.run ([sys.executable , "-m" , "pip" , "install", "yt-dlp", "--break-system-packages"])  
            subprocess.run (["sudo", "apt", "install", "ffmpeg", "-y"])
            subprocess.run ([sys.executable , "-m" , "pip" , "install" , "rich" , "--break-system-packages"])
        elif manager == "pacman" :
            subprocess.run (["sudo" , "pacman" , "-S" , "yt-dlp"])
            subprocess.run (["sudo" , "pacman" , "-S" , "ffmpeg"])
            subprocess.run ([sys.executable , "-m" , "pip" , "install" , "rich"])
        elif manager == "dnf" :
            subprocess.run (["sudo" , "dnf" , "install" , "yt-dlp"])
            subprocess.run (["sudo" , "dnf" , "install" , "ffmpeg"])
            subprocess.run([sys.executable , "-m" , "pip" , "install" , "rich"])
        else :
            console.print ("Sorry the download faild" , "red")
    elif auto == "no" :
        print ("ok download pkgs and then restart the app")
    if not check :
        print ("somthing went wrong try again")
Console = Console()
Console.input (f"[yellow]Enter to contenue....[/yellow]")

def show_logo():
    logo = r'''

            __              __                .__   
    ___.__._/  |_          _/  |_  ____   ____ |  |  
    <   |  |\   __\  ______ \   __\/  _ \ /  _ \|  |  
    \___  | |  |   /_____/  |  | (  <_> |  <_> )  |__
    / ____| |__|            |__|  \____/ \____/|____/
    \/                                               
                        /\_/\
                       ((@v@))
                       ():::()
                        VV-VV

              >>Youtube Download Tool 3.0<<      
    '''
   
    Console.print(
        Panel(
            logo,
            style="cyan bold",
            title="[white]Welcome[/white]",
            subtitle="[yellow]v3.0[/yellow]",
            expand=False
        )
    )

CONFIG_FILE = "config.txt"
if not os.path.exists(CONFIG_FILE):
    Console.print(f"\nWelcome !\nThis app will make yt-dlp much easier!", style="yellow")
    download_path = Console.input("[cyan]Where do you want videos to be saved?\n[/cyan]")
    download_path = os.path.expanduser(download_path)
    os.makedirs(download_path, exist_ok=True)
    cmd_down = Console.input(f"Do you want to this app to work enywhere on terminal ?\n")
    with open(CONFIG_FILE, "w") as f:
        f.write(download_path+"\n")
        f.write("Download automatic : " + cmd_down + "\n")
        Console.print ("The file will be saved is : " + download_path)
    Console.input("[yellow]Press Enter to continue...[/yellow]")
else:
    with open(CONFIG_FILE, "r") as f:
        lines = f.readlines()
        download_path = lines[0].strip()
        cmd_down = lines[1].strip() if len(lines) > 1 else "no"
    if cmd_down in ["yes" , "y" , ""] :
        subprocess.run('sudo ln -s "$(pwd)/yt-tool.py" /usr/local/bin/yt-tool')
    else :
        pass


def print_quality() :
        Console.print ("Please choose a quality" , style="cyan bold")
        Console.print ("[yellow] |1| [/yellow] 4k")
        Console.print ("[yellow] |2| [/yellow] 2k")
        Console.print ("[yellow] |3| [/yellow] 1080p")
        Console.print ("[yellow] |4| [/yellow] 720p")
        Console.print ("[yellow] |5| [/yellow] 480p")


def after_dow(result):
    if platform.system().lower() == "windows" :
        pass
    if result.returncode == 0:
        Console.print("Success !!!", style= "green")
    else:
        Console.print("Download failed ", style="red")
if platform.system().lower():
    os.environ["PATH"] += os.pathsep + os.path.expanduser("~/.local/bin")

def download() :
            result = subprocess.run(cmd)
            after_dow(result)
            Console.input("[red]Enter to continue[/red]")

def choices () :
    Console.print ("[cyan bold]\nPlease choose one of this :[/cyan bold]")
    Console.print ("[yellow] |1| [/yellow] Video")
    Console.print ("[yellow] |2| [/yellow] Playlist")
    Console.print ("[yellow] |3| [/yellow] Sound from video")
    Console.print ("[yellow] |4| [/yellow] Download from inestegram or other socioal")
    Console.print ("[yellow] |5| [/yellow] Help")
    Console.print ("[yellow] |6| [/yellow] Exit")
# def enywhere() :
#     if platform.system().lower() == "windows" :
#         pass
    #   ناقص اخليه يحمل تلقائي
    
while True :
    formats_1 = {
    "1": 'bv*[vcodec^=avc1][height<=2160]+ba[acodec^=mp4a]/b[height<=2160]',  # 4K
    "2": 'bv*[vcodec^=avc1][height<=1440]+ba[acodec^=mp4a]/b[height<=1440]',  # 2K
    "3": 'bv*[vcodec^=avc1][height<=1080]+ba[acodec^=mp4a]/b[height<=1080]',  # 1080p
    "4": 'bv*[vcodec^=avc1][height<=720]+ba[acodec^=mp4a]/b[height<=720]',    # 720p
    "5": 'bv*[vcodec^=avc1][height<=480]+ba[acodec^=mp4a]/b[height<=480]',    # 480p
    }
    if platform.system().lower() == "windows" :
        pass 
    else :
        subprocess.run(["clear"])
    show_logo()
    choices()
    choice = Console.input ("[cyan]> [/cyan]")
    if choice == "1" : 
        print_quality()

        quality = Console.input ("[cyan]What quality you want?\n> [/cyan]")
        url = Console.input ("[cyan]]Please paste URL: \n> [/cyan]")
        cmd = ["yt-dlp" , 
        "-f" , formats_1[quality] ,
        "--merge-output-format", "mp4",
        "-o", f"{download_path}/%(title)s.mp4",
        url 
            ]

        if quality == "1" :
            download()
        elif quality == "2" :
            download()
        elif quality == "2" :
            download()
        elif quality == "3" :
            download()
        elif quality == "4" :
            download()
        elif quality == "5" : 
           download()
        else :
            Console.input("[red]Please try again[/cyan]")
            pass

    elif choice == "2" :
        file_choice = Console.input("[yellow]Do you want a file for a play list ? \n[yellow]")
        if file_choice.lower() in ["yes" , "y" , "" ]:
            print_quality()
            quality = Console.input ("[cyan]> [/cyan]")
            url = Console.input ("[yellow]Please paste a URL: \n> [/yellow]")
            cmd = ["yt-dlp" , 
            "-f" , formats_1[quality] ,
            "--merge-output-format", "mp4",
            "-o", f"{download_path}%(playlist_title)s/%(title)s.mp4" ,
            url 
                ]
            if quality == "1" :
                download()
            elif quality == "2" :
                download()
            elif quality == "3" :
                download()
            elif quality == "4" :
               download()
            elif quality == "5" : 
                download()
        elif file_choice.lower() in ["no" , "n"] :
            print_quality()
            quality = Console.input ("[yellow]What quality you want?\n> [/yellow]")
            url = Console.input ("[yellow]Please paste a URL:[/yellow] \n[cyan]> [/cyan]")
            cmd = ["yt-dlp" , 
            "-f" , formats_1[quality] ,
            "--merge-output-format", "mp4",
            "-o", f"{download_path}/%(title)s.mp4",
            url 
                ]

            if quality == "1" :
                download()
            elif quality == "2" :
               download()
            elif quality == "3" :
               download()
            elif quality == "4" :
               download()
            elif quality == "5" : 
               download()
    elif choice == "3" :
        file_choice = Console.input(f"[yellow]Do you want a file for a play list ?[/yellow]\n[cyan]> [/cyan]")
        url = Console.input ("[yellow]Please enter URL:[/yellow] \n[cyan]> [/cyan]")
        if file_choice.lower() in ["yes" , "y" ,""] :
            cmd=[
                'yt-dlp',
                '-x',
                '--audio-format', 'mp3',
                '--audio-quality', '0',
                '-o', f"{download_path}/%(playlist_index)s - %(title)s.%(ext)s",
             url
            ]
            download()
        elif file_choice.lower() in ["no" , "n"] :
            cmd = [
                'yt-dlp',
                '-x',
                '--audio-format', 'mp3',
                '--audio-quality', '0',
                '-o', f"{download_path}/%(title)s.mp3",
                url
            ]
            
            download()
    elif choice == "4" :
        Console.print("Paste URL:" , style="yellow")
        url = Console.input("[cyan]> [/cyan]")
        cmd = [
            'yt-dlp',
            url
        ]
        subprocess.run(cmd)
        Console.input("[red]Enter to continue[/red]")
    elif choice == "5" :
        table = Table()
        table.add_column("most errors" , style = "yellow")
        table.add_column("selution" , style = "cyan")
        table.add_row("yt-dlp or ffmpeg are missing" , "--linux : download from pkg maneger\n--Windows : install exe file and put in same yt-tool file")
        table.add_row("Using ald version of yt-dlp or ffmpeg" , "--youtube every weak make patches make sure to download latest version")
        table.add_row("File downloading in other path" , "--Open config file and chainge the path")
        Console.print (table)
        Console.input("[red]Enter to continue[/red]")
    elif choice == "6" :
        break