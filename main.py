import speech_recognition as sr
from googletrans import Translator
from translate import Translator
from gtts import gTTS
import os
import pyaudio

# Initialize the recognizer
r = sr.Recognizer()

# Function to capture audio from microphone using PyAudio
def capture_audio():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 5

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Recording...")
    frames = []

    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    audio_data = b''.join(frames)
    return audio_data, RATE

from translate import Translator

# Function to recognize speech and translate
def recognize_and_translate(audio_data):
    try:
        audio_data = sr.AudioData(audio_data, 44100, 2)  # Convert raw audio data to AudioData object
        text = r.recognize_google(audio_data)
        print(f"You said: {text}")

        # Translate the recognized speech
        translator = Translator(to_lang="hi")
        translated_text = translator.translate(text)
        
        if translated_text is None:
            raise ValueError("Translation failed. No translated text received.")

        print(f"Translated text: {translated_text}")

        # Convert translated text to speech in the destination language
        tts = gTTS(text=translated_text, lang='hi')
        tts.save("translated_audio.mp3")

        # Play the translated audio (cross-platform)
        os.system("start translated_audio.mp3")  # This will open the file with the default audio player

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")

    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

    except ValueError as e:
        print(f"Translation error: {e}")

# Main program
if __name__ == "__main__":
    audio_data, rate = capture_audio()
    recognize_and_translate(audio_data)
