# voice to speech

Simply invoke whisper and GPT to transcribe an audio file into text, then summarize into text

## Installation

```bash
pip install git+https://github.com/yztxwd/voice_to_speech.git
```

## Usage

> You need an upgraded [OpenAI API](https://platform.openai.com/) account for using this repo
> 
> Go to settings for your `Organization ID`, and generate an API key at `API keys` (remember to COPY and SAVE IT!)

Tiny whisper model on example audio file

```bash
voice_to_speech -m tiny -a $OPENAI_API_KEY -o $ORGANIZATION_ID data/audio.mp3
```

if you only have video file, use ffmpeg to extract audio, for example:
```bash
# re-encoding depends on the audio format in video
ffmpeg -i video.mp4 -map 0:a -acodec libmp3lame audio.mp3
```
