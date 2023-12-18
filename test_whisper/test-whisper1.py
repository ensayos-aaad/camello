"""
Referencias:
- https://wandb.ai/wandb_fc/gentle-intros/reports/OpenAI-Whisper-How-to-Transcribe-Your-Audio-to-Text-for-Free-with-SRTs-VTTs---VmlldzozNDczNTI0

"""

"""
Notebook:
!pip install git+https://github.com/openai/whisper.git
!sudo apt update && sudo apt install ffmpeg
"""

import whisper
import pandas as pd
import os
from whisper.utils import get_writer

model = whisper.load_model("base")
audio = "trabalenguas.mp3"
# audio = "PFS_Podcast_313_comida_en_el_futuro.mp3"
result = model.transcribe(audio)
print(result["text"])
#df = pd.DataFrame(result["segments"])
#df = pd.DataFrame(result["segments"])[['id','start','end','text']]
#print(df)
# save TXT

output_directory = "./"

# Save as a TXT file without any line breaks
with open("transcription.txt", "w", encoding="utf-8") as txt:
    txt.write(result["text"])


# Save as a TXT file with hard line breaks
txt_writer = get_writer("txt", output_directory)
txt_writer(result, audio)


# https://github.com/openai/whisper/tree/main/whisper

