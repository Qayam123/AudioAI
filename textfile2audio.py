# Import the required module for text to speech conversion
from gtts import gTTS

# Import pygame for playing the converted audio
import pygame
import time

# The text that you want to convert to audio
with open("codeexplain.txt", 'r') as f:
    mytext = f.read()

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("welcome2.mp3")

# Initialize the pygame mixer
pygame.mixer.init()

# Load the mp3 file
pygame.mixer.music.load("welcome2.mp3")

# Play the loaded mp3 file
pygame.mixer.music.play()

# Keep the script running until the audio finishes playing
while pygame.mixer.music.get_busy():
    time.sleep(1)

