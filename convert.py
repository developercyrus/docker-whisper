import whisper
import os
import sys
from datetime import timedelta

path = os.environ.get('DATA', './')
print(path)
model = whisper.load_model("large-v3")
result = model.transcribe(os.path.join(path, sys.argv[1]))

segments = result['segments']

for segment in segments:
    startTime = str(0)+str(timedelta(seconds=int(segment['start'])))+',000'
    endTime = str(0)+str(timedelta(seconds=int(segment['end'])))+',000'
    text = segment['text']
    segmentId = segment['id']+1
    segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] == ' ' else text}\n\n"

    srtFilename = os.path.join(path, sys.argv[2])
    with open(srtFilename, 'a', encoding='utf-8') as srtFile:
        srtFile.write(segment)
