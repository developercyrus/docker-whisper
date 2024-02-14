### Run by docker 
```bash
sudo docker run \
 --volume ./:/data \
 --rm \
 -it \
 developercyrus/docker-whisper file.mp3 file.mp3.srt
```

### Run by CLi 
```bash
git clone https://github.com/developercyrus/docker-whisper
pip install -r requirements.txt

python3 convert.py file.mp3 file.mp3.srt
```
