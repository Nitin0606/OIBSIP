

import pyttsx3
import pyaudio
from google.cloud import speech_v1p1beta1 as speech
from datetime import datetime

def get_date_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    current_date = now.strftime("%Y-%m-%d")
    return f"The current time is {current_time} and the date is {current_date}"

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    client = speech.SpeechClient()
    
    with pyaudio.PyAudio() as audio:
        with audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024) as stream:
            print("Listening...")
            audio_data = stream.read(8000)  # Adjust the number of frames as needed
            
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code="en-US",
        )
        
        audio = speech.RecognitionAudio(content=audio_data)
        
        try:
            print("Recognizing...")
            response = client.recognize(config=config, audio=audio)
            query = response.results[0].alternatives[0].transcript.lower()
            print("You said:", query)
            return query
        except Exception as e:
            print(f"Error recognizing speech: {e}")
            return ""

if __name__ == "__main__":
    speak("Hello! I am Veronica, how can I help you?")

    while True:
        command = listen()

        if "hello" in command:
            speak("Hello! How can I help you?")
        elif "time" in command:
            time_text = get_date_time()
            print(time_text)
            speak(time_text)
        elif "date" in command:
            date_text = get_date_time()
            print(date_text)
            speak(date_text)
        elif "exit" in command:
            speak("Goodbye! Have a great day.")
            break
