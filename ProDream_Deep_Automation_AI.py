
import os
import sys
import time
import json
import random
import platform
import subprocess
import speech_recognition as sr
import pyttsx3
import openai

# OpenAI API Key (User needs to provide their own API Key)
OPENAI_API_KEY = "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"

class ProDreamAI:
    def __init__(self):
        self.name = "ProDream AI"
        self.version = "4.0"
        self.os_info = platform.system()
        self.voice_engine = pyttsx3.init()
        self.voice_engine.setProperty('rate', 160)
        self.voice_engine.setProperty('volume', 1.0)
        self.memory_file = "ai_memory.json"
        self.load_memory()
        
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

    def load_memory(self):
        if os.path.exists(self.memory_file):
            with open(self.memory_file, "r") as file:
                self.memory = json.load(file)
        else:
            self.memory = {}

    def save_memory(self):
        with open(self.memory_file, "w") as file:
            json.dump(self.memory, file)

    def learn_from_interaction(self, user_input, ai_response):
        if user_input not in self.memory:
            self.memory[user_input] = ai_response
            self.save_memory()

    def chat_with_ai(self, prompt):
        if prompt in self.memory:
            response = self.memory[prompt]
        else:
            try:
                import openai
                openai.api_key = OPENAI_API_KEY
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}]
                )
                response = response['choices'][0]['message']['content']
                self.learn_from_interaction(prompt, response)
            except Exception as e:
                response = "There was an error connecting to the AI chat system."
        
        self.speak(response)
        return response

    def execute_system_task(self, task):
        if "create folder" in task:
            folder_name = task.replace("create folder", "").strip()
            os.makedirs(folder_name, exist_ok=True)
            self.speak(f"Folder '{folder_name}' created successfully.")
        elif "delete file" in task:
            file_name = task.replace("delete file", "").strip()
            if os.path.exists(file_name):
                os.remove(file_name)
                self.speak(f"File '{file_name}' deleted successfully.")
            else:
                self.speak("File not found.")
        elif "list files" in task:
            files = os.listdir(".")
            self.speak(f"Current directory files: {', '.join(files)}")
        elif "execute script" in task:
            script_name = task.replace("execute script", "").strip()
            if os.path.exists(script_name):
                self.speak(f"Executing script {script_name}.")
                subprocess.run(["python", script_name])
            else:
                self.speak("Script file not found.")
        else:
            self.speak("System task not recognized.")

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
        elif "search" in command:
            query = command.replace("search", "").strip()
            self.speak(f"Searching Google for {query}")
            os.system(f"start chrome https://www.google.com/search?q={query}")
        elif "chat mode" in command:
            self.speak("Entering AI Chat Mode. Type your questions below:")
            while True:
                user_input = input("You: ")
                if user_input.lower() in ["exit", "quit", "stop"]:
                    self.speak("Exiting chat mode.")
                    break
                response = self.chat_with_ai(user_input)
                print(f"ProDream AI: {response}")
        elif "learn" in command:
            self.speak("Tell me something to learn.")
            new_input = self.listen()
            if new_input:
                self.speak("Tell me how I should respond.")
                new_response = self.listen()
                if new_response:
                    self.learn_from_interaction(new_input, new_response)
                    self.speak("Got it! I will remember that.")
        elif "system task" in command:
            task = command.replace("system task", "").strip()
            self.execute_system_task(task)
        else:
            self.speak("Command not recognized.")

    def run(self):
        self.speak("ProDream AI Deep Automation System Activated. How can I assist you?")
        while True:
            command = self.listen()
            if command:
                self.execute_command(command)
            time.sleep(1)

if __name__ == "__main__":
    ai = ProDreamAI()
    ai.run()
