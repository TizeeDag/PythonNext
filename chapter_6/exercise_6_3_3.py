"""Speak the course sentence with pyttsx3.

Install: python -m pip install pyttsx3
Reference: https://pyttsx3.readthedocs.io/en/latest/engine.html
"""
import pyttsx3


def main():
    engine = pyttsx3.init()
    engine.say("first time i'm using a package in next.py course")
    engine.runAndWait()


if __name__ == '__main__':
    main()
