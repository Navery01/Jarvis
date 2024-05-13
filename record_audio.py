import pyaudio
import wave
import os

def create_file_name():
    recordings = os.listdir("recordings")
    if len(recordings) == 0:
        return "recordings/output.wav"
    else:
        return f"recordings/output{len(recordings)}.wav"
    
    
def record_audio():
    print("Recording audio")
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
    try :
        frames = []
        while True:
            data = stream.read(1024)
            frames.append(data)
            
    except KeyboardInterrupt:
        print("Recording stopped")


    stream.stop_stream()
    stream.close()
    audio.terminate()
    file_name = create_file_name()

    sound_file = wave.open(file_name, 'wb')  
    sound_file.setnchannels(1)
    sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    sound_file.setframerate(44100)
    sound_file.writeframes(b''.join(frames))
    sound_file.close()
    return file_name