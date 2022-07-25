from urllib import response
from win32com.client import Dispatch
import requests
import json
import time
import os


def speak(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


if __name__ == "__main__":
    speak("Initiating")
    while True:
        os.system("cls")
        print(f"Press\n1. for international news\n2. for Pakistan's news\n3. Exit")
        speak(f"Press\n1. for international news\n2. for Pakistan's news\nand 3 to exit")
        user = int(input())

        if user == 1:
            r = requests.get(
                "https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=7ebb851e81ca4fe99c5c795fc6ddd635")
        elif user == 2:
            r = requests.get(
                "https://newsapi.org/v2/everything?sources=ary-news&apiKey=7ebb851e81ca4fe99c5c795fc6ddd635")
        elif user == 3:
            break
        else:
            speak("Please enter a valid choice")
            continue

        content = r.json()['articles']
        news = []
        for i in content:
            d = i['description']
            news.append(d)

        count = 1
        for item in news:
            speak(f"News number {count}: {item}")
            time.sleep(1)
            count += 1
