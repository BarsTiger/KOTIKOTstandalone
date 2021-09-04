import os
import zipfile, urllib.request
import subprocess, sys
try:
    import progressbar
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'progressbar'])
    import progressbar

pbar = None

def show_progress(block_num, block_size, total_size):
    global pbar
    if pbar is None:
        pbar = progressbar.ProgressBar(maxval=total_size)
        pbar.start()

    downloaded = block_num * block_size
    if downloaded < total_size:
        pbar.update(downloaded)
    else:
        pbar.finish()
        pbar = None

neededfiles = "https://github.com/BarsTiger/KOTIKOTstandalone/raw/master/Exes/shakalizator/Zipped/needed.zip"
exe = "https://github.com/BarsTiger/KOTIKOTstandalone/raw/master/Exes/shakalizator/Zipped/shakalizator.exe"

print("Downloading resources and ffmpeg")
urllib.request.urlretrieve(neededfiles, 'needed.zip', show_progress)
if os.path.exists('needed.zip'):
    print("Success!")
    print()
else:
    print("Something went wrong...")
    input()
    exit()

print("Downloading main exe")
urllib.request.urlretrieve(exe, 'shakalizator.exe', show_progress)
if os.path.exists('shakalizator.exe'):
    print("Success!")
    print()
else:
    print("Something went wrong...")
    input()
    exit()

print("Extracting files")
with zipfile.ZipFile('needed.zip', 'r') as archfile:
    archfile.extractall()
if os.path.exists('ffmpeg.exe') and os.path.exists('resources'):
    print("Success!")
    print()
else:
    print("Something went wrong...")
    input()
    exit()

print("Deleting temp files")
os.remove("needed.zip")
if not os.path.exists('needed.zip'):
    print("Success!")
    print()
else:
    print("Something went wrong...")
    input()
    exit()

input("Installation completed!\nPress Enter to exit...")
