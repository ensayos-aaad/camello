# https://ttsmp3.com/text-to-speech/US%20Spanish/
from openai import OpenAI

"""
import os

api_key=os.environ.get("OPENAI_API_KEY")
print(api_key)
client = OpenAI(
   api_key=os.environ.get("OPENAI_API_KEY")
)
"""
client = OpenAI()

# audio_file= open("buenas-noches.mp3", "rb")
# audio_file = open("PFS_Podcast_313_comida_en_el_futuro.mp3", "rb")
# audio_file = open("output.wav", "rb")
audio_file = open("trabalenguas.mp3", "rb")
transcript = client.audio.transcriptions.create(
  model="whisper-1",
  file=audio_file,
  response_format="text"
)

print(transcript)
