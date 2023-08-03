#!/usr/bin/env python

import os
import argparse
import openai
import whisper

SYSTEM_INSTRUCTION="""
You are an assistant that only speaks in Markdown. Do not write text that isn't formatted as markdown.

Example formatting:

Testing No-Code Workflow

--Summary--

This audio recording documents a test of a no-code workflow using Google Drive and a single code step to reduce calls and improve efficiency.

--Additional Info--

## Main Points

- point 1
- point 2

## Action Items

- point 1
- point 2

## Follow Up Questions

- point 1
- point 2

## Potential Arguments Against

- point 1
- point 2
"""

USER_MESSAGE="""

Write a Title for the transcript that is under 15 words.

Then write: "--Summary--"

Write "Summary" as a Heading 1.

Write a summary of the provided transcript.

Then write: "--Additional Info--".

Then return a list of the main points in the provided transcript. Then return a list of action items. Then return a list of follow up questions. Then return a list of potential arguments against the transcript.

For each list, return a Heading 2 before writing the list items. Limit each list item to 100 words, and return no more than 5 points per list.

Transcript:

"""

# define a wrapper function for transcription
def transcribe(audio_filepath, prompt: str) -> str:
    """Given a prompt, transcribe the audio file."""
    transcript = openai.Audio.transcribe(
        file=open(audio_filepath, "rb"),
        model="whisper-1",
        prompt=prompt,
    )
    return transcript["text"]

def main():
    parser = argparse.ArgumentParser("Transcribe a speech audio file into summary text")
    parser.add_argument("audio", help="Audio file")
    parser.add_argument("-m", "--model", help="Which model to use (tiny, base, small, medium, large)")
    parser.add_argument("-d", "--device", default="cpu", help="Accelerator device, cpu|cuda|mps")
    parser.add_argument("-o", "--OPENAI_ORG_ID", help="OpenAI Organization ID")
    parser.add_argument("-a", "--OPENAI_API_KEY", help="OpenAI API KEY")
    args = parser.parse_args()

    # audio to text
    model = whisper.load_model(args.model); model.to(args.device)
    res = model.transcribe(args.audio)
    text = res.get("text")
    
    # summary by openAI
    openai.organization = args.OPENAI_ORG_ID
    openai.api_key = args.OPENAI_API_KEY

    MODEL = "gpt-3.5-turbo"
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_INSTRUCTION},
            {"role": "user", "content": f"{USER_MESSAGE} {text}"},
        ],
        temperature=0,
    )

    print(response['choices'][0]['message']['content'])

if __name__ == "__main__":
    main()
