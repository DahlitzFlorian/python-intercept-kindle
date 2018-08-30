import shutil
import sys
import os
import subprocess
import configparser

from pathlib import Path, PurePath


flag = False

config = configparser.ConfigParser()
config.read("config.ini")

sender = config["KINDLE"]["sender_address"]
recipient = config["KINDLE"]["kindle_address"]


def convert_files():
    if not os.path.exists("tmp"):
        flag = True
        return
        
    print("Get files to convert...")
    path = Path("tmp")
    files = path.iterdir()

    print("Convert files...")
    print("-"*40)
    for file in files:
        if file.is_file() and file.name.endswith("html"):
            file_mobi = file.stem + ".mobi"
            subprocess.run(["ebook-convert", file.name, file_mobi], cwd="tmp",
                shell=True)
        
    print("-"*40)
    print("Convertion was successful.")
    

def send_files():
    if flag:
        return
        
    print("Get files to send to kindle...")
    path = Path("tmp")
    files = path.iterdir()

    print("Send files...")
    for file in files:
        if file.is_file() and file.name.endswith("mobi"):
            subprocess.run(["calibre-smtp", "-a", file.name, sender, recipient, " "],
                cwd="tmp", shell=True)
        
    print("Files were send.")
    print("="*40)
    print("INFORMATION: Deletion has to be done by hand!")
    print("="*40)
