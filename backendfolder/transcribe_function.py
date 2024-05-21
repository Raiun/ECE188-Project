import whisper

model = whisper.load_model("base")

def transcribe_audio(audio_data):
    result = model.transcribe(audio_data)
    return result['text']
