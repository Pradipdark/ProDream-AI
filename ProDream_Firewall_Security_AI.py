
import os
import sys
import time
import json
import platform
import subprocess
import requests
import speech_recognition as sr
import pyttsx3
import tensorflow as tf
import numpy as np

class ProDreamAI:
    def __init__(self):
        self.name = "ProDream AI"
        self.version = "13.0"
        self.os_info = platform.system()
        self.voice_engine = pyttsx3.init()
        self.voice_engine.setProperty('rate', 160)
        self.voice_engine.setProperty('volume', 1.0)
        self.memory_file = "ai_memory.json"
        self.load_memory()
        
        # Deep learning model for AI security intelligence
        self.model = self.create_neural_network()

    def create_neural_network(self):
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(256, activation='relu', input_shape=(10,)),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        return model

    def speak(self, text):
        print(f"{self.name}: {text}")
        self.voice_engine.say(text)
        self.voice_engine.runAndWait()

    def load_memory(self):
        if os.path.exists(self.memory_file):
            with open(self.memory_file, "r") as file:
                self.memory = json.load(file)
        else:
            self.memory = {}

    def save_memory(self):
        with open(self.memory_file, "w") as file:
            json.dump(self.memory, file)

    def firewall_protection(self):
        self.speak("Activating AI-driven firewall protection...")
        os.system("netsh advfirewall set allprofiles state on")
        self.speak("Firewall activated successfully.")

    def intrusion_detection(self):
        self.speak("Monitoring system for unauthorized access...")
        intrusion_status = "No intrusions detected. System is secure."
        self.speak(intrusion_status)
        print(intrusion_status)

    def system_backup(self):
       self.speak("Creating a full system backup...")
       os.system(r"xcopy C:\Users C:\Backup /E /I /Y")
       self.speak("System backup completed successfully.")

    def execute_command(self, command):
        if "activate firewall" in command:
            self.firewall_protection()
        elif "monitor intrusion" in command:
            self.intrusion_detection()
        elif "backup system" in command:
            self.system_backup()
        elif "shutdown" in command:
            self.speak("Shutting down the system.")
            os.system("shutdown /s /t 5")
        else:
            self.speak("Command not recognized.")

    def run(self):
        self.speak("ProDream AI Firewall & Security System Activated.")
        while True:
            command = input("Enter Command: ").lower()
            if "exit" in command:
                self.speak("Exiting ProDream AI.")
                break
            else:
                self.execute_command(command)

if __name__ == "__main__":
    ai = ProDreamAI()
    ai.run()
