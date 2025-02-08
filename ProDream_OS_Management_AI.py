
import os
import sys
import subprocess
import pyttsx3

class ProDreamAI:
    def __init__(self):
        self.name = "ProDream AI"
        self.version = "10.0"
        self.voice_engine = pyttsx3.init()

    def speak(self, text):
        print(f"{self.name}: {text}")
        self.voice_engine.say(text)
        self.voice_engine.runAndWait()

    def manage_os(self, command):
        if "list processes" in command:
            processes = subprocess.run(["tasklist"], capture_output=True, text=True)
            self.speak("Listing all running processes.")
            print(processes.stdout)
        elif "terminate process" in command:
            process_name = command.replace("terminate process", "").strip()
            os.system(f"taskkill /IM {process_name} /F")
            self.speak(f"Terminated process {process_name}.")
        else:
            self.speak("OS management command not recognized.")

    def run(self):
        self.speak("ProDream AI OS Management System Activated.")
        self.manage_os("list processes")

if __name__ == "__main__":
    ai = ProDreamAI()
    ai.run()
