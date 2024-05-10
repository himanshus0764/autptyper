#!/usr/bin/env python3
import subprocess
import time
import argparse
from tkinter import filedialog, Tk, simpledialog

def type_text(text, start_delay=5, speed=0.15):
    time.sleep(start_delay + 1)
    for ch in text:
        subprocess.call(["xdotool", "type", ch])
        time.sleep(speed)

def select_text_file():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select Text File", filetypes=[("Text Files", "*.txt")])
    return file_path

def get_typing_speed():
    root = Tk()
    root.withdraw()
    speed = simpledialog.askfloat("Typing Speed", "Enter typing speed (seconds per character):", minvalue=0.01)
    return speed

def main():
    parser = argparse.ArgumentParser(description='Types a string character by character.')
    parser.add_argument('--speed', type=float, help='Typing speed in seconds per character.')
    args = parser.parse_args()

    if not args.speed:
        args.speed = get_typing_speed()

    text_file = select_text_file()

    with open(text_file, "r") as file:
        text = file.read()

    type_text(text, start_delay=5, speed=args.speed)

if __name__ == "__main__":
    main()
