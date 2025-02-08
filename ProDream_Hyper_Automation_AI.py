
import os
import sys
import time
import json
import platform
import subprocess
import pyttsx3

class ProDreamAI:
    def __init__(self):
        self.name = "ProDream AI"
        self.version = "9.0"
        self.os_info = platform.system()
        self.voice_engine = pyttsx3.init()

    def speak(self, text):
        print(f"{self.name}: {text}")
        self.voice_engine.say(text)
        self.voice_engine.runAndWait()

    def manage_os(self, command):
        if "list files" in command:
            files = os.listdir(".")
            self.speak(f"Current directory files: {', '.join(files)}")
        elif "shutdown" in command:
            self.speak("Shutting down the system.")
            os.system("shutdown /s /t 5")
        else:
            self.speak("OS management command not recognized.")

    def run(self):
        self.speak("ProDream AI Hyper-Automation System Activated.")
        self.manage_os("list files")

if __name__ == "__main__":
    ai = ProDreamAI()
    ai.run()
