import asyncio
import edge_tts
import os

async def generate_audio() -> None:
    os.makedirs("output",exist_ok=True)

    text="Hello yash,this is high quality neural text to speech running " \
    "without gpu."

    communicate = edge_tts.Communicate(text,"hi-IN-SwaraNeural")
    # communicate = edge_tts.Communicate(text,"en-US-AriaNeural")
    

    await communicate.save("output/edge_output_hi.mp3")

    print("Audio Generated succesfully")

asyncio.run(generate_audio())