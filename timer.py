import time
from playsound import playsound

def play_audio(seconds):
    start = time.time()
    time.process_time()
    elapsed = 0
    while elapsed < seconds:
        elapsed = time.time() - start
        playsound("D:\Models\DrowsinessDetector\warningbeep.mp3")
