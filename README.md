# voice to speech

Transcribe an audio file into text, then summarize

## Insatllation

```bash
pip install git+https://github.com/yztxwd/voice_to_speech.git
```

## Usage

Tiny whisper model on example audio file

```bash
voice_to_speech -m tiny -a $OPENAI_API_KEY -o $ORGANIZATION_ID data/audio.mp3
```

if you only have video file, use ffmpeg to extract audio, for example:
```bash
# re-encoding depends on the audio format in video
ffmpeg -i video.mp4 -map 0:a -acodec libmp3lame audio.mp3
```
