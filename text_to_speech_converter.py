import pyttsx3
import tkinter as tk
from tkinter import filedialog
import pyautogui


root = tk.Tk()

root.withdraw()

text_to_speech= pyttsx3.init()

text_to_speech.setProperty('rate',125)

text_to_speech.setProperty('volume',0.7)

voices = text_to_speech.getProperty('voices')

text_to_speech.setProperty('voice',voices[1].id)

file_path = filedialog.askopenfilename()

f = open(f"{file_path}","r")

a = f.read()

file_name = pyautogui.prompt(text = "Enter the name with which you \n want to save your with .mp3 extension.\n Eg : xzy.mp3")

text_to_speech.save_to_file(a,f'{file_name}')
text_to_speech.runAndWait()

# end of code