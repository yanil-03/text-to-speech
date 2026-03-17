from gtts import gTTS
import os

# Create output folder
os.makedirs("output", exist_ok=True)

# text = "Hello Yanil, your lightweight text to speech model is working successfully on Python 3.12."

tts = gTTS(text="नमस्ते आपका मॉडल सफलतापूर्वक चल रहा हे", lang="hi")

# tts =gTTS(text=text, lang="en")

file_path = "output/output_hi.mp3"
tts.save(file_path)

print("Audio generated successfully at:", file_path)
