import subprocess, sys, os, shutil

try:
    from moviepy.editor import *
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'moviepy'])
    from moviepy.editor import *

try:
    from PIL import Image
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'pillow'])
    from PIL import Image

videoname = "nominalo"
imagename = 'dababy'
im1 = Image.open(imagename + ".jpg")
IMAGE_10 = imagename + "_shakalized.jpg"
im1.save(IMAGE_10, "JPEG", quality=0)

clip = VideoFileClip(str(videoname + ".mp4"))
clip_resized = clip.resize(10)
clip_resized.write_videofile("movie_resized_temp.mp4")

