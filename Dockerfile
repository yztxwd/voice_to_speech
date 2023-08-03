FROM python:3.9.16

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY voice_to_speech.py ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python", "./voice_to_speech.py"]
CMD ["--help"]
