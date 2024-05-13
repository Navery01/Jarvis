from openai import OpenAI
from config import API_KEY

client = OpenAI(
    api_key=API_KEY,
)

def get_response(input):
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user","content": input,}] ,model="gpt-3.5-turbo",)
    response = chat_completion.choices[0].message.content
    return response


def transcribe(audio_file_path):
    audio_file = open(audio_file_path, "rb")
    print("Transcribing audio")
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
        )
    
    print(f'Finished Transcription: {transcription.text}')
    return transcription.text

