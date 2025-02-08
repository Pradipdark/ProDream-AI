 
import os
import sys
import time
import json
import random
import platform
import subprocess
import speech_recognition as sr
import pyttsx3

class ProDreamAI:
    def __init__(self):
        self.name = "ProDream AI"
        self.version = "1.0"
        self.os_info = platform.system()
        self.voice_engine = pyttsx3.init()
        self.voice_engine.setProperty('rate', 160)  # Adjust speed
        self.voice_engine.setProperty('volume', 1.0)  # Set volume to max

    def speak(self, text):
        print(f"{self.name}: {text}")
        self.voice_engine.say(text)
        self.voice_engine.runAndWait()

    def listen(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            try:
                command = recognizer.recognize_google(audio)
                print(f"You said: {command}")
                return command.lower()
            except sr.UnknownValueError:
                self.speak("Sorry, I didn't understand.")
                return None
            except sr.RequestError:
                self.speak("There was an issue connecting to the recognition service.")
                return None

    def execute_command(self, command):
        if "open notepad" in command:
            self.speak("Opening Notepad.")
            subprocess.run("notepad.exe")
        elif "time" in command:
            self.speak(f"The current time is {time.strftime('%H:%M:%S')}")
        elif "shutdown" in command:
            self.speak("Shutting down the system.")
            if self.os_info == "Windows":
                os.system("shutdown /s /t 5")
        else:
            self.speak("Command not recognized.")

    def run(self):
        self.speak("ProDream AI Core System Activated. How can I assist you?")
        while True:
            command = self.listen()
            if command:
                self.execute_command(command)
            time.sleep(1)

if __name__ == "__main__":
    ai = ProDreamAI()
    ai.run()
