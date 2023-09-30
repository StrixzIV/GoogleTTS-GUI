import os
import gtts
import json

import customtkinter as ctk
from tkinter.messagebox import showerror

from settings_menu import SettingsMenu

app = ctk.CTk()

app.title('GoogleTTS GUI')
app.geometry('300x400')
app.resizable(width = False, height = False)

with open('./config/language.json') as file:
    languages_list = json.load(file)

def load_settings() -> dict:

    if not os.path.exists('./config/settings.json'):
        with open('./config/settings.json', 'w') as file:
            json.dump({'theme': 'system'}, file)

    with open('./config/settings.json') as file:
        return json.load(file)


def generate() -> None:
    
    '''
        Send request to google text-to-spleech API and save output file to the target directory
    '''
    
    try:
        
        dir = ctk.filedialog.askdirectory()

        if not dir:
            return

        inpText = input_text.get()
        filename = output_filename.get() if output_filename.get() else 'output'
        language = selected_language.get()
        slowmode = use_slowmode.get()

        speech = gtts.gTTS(text = inpText, lang = languages_list[language], lang_check = False, slow = slowmode)
        speech.save(os.path.join(dir, f'{filename}.mp3'))

    except gtts.gTTSError:
        showerror('Error', 'Google API Error: Cannot generate audio file.')


def open_settings() -> None:
    settings_tab = SettingsMenu(app)


ctk.set_appearance_mode(load_settings()['theme'])

languages = sorted(languages_list.keys())

input_text = ctk.StringVar()
output_filename = ctk.StringVar()
selected_language = ctk.StringVar()
use_slowmode = ctk.BooleanVar()

label1 = ctk.CTkLabel(app, text = 'GoogleTTS GUI (v1.3)').grid(row = 0, column = 0, padx = (80, 0), pady = (20, 15))

label2 = ctk.CTkLabel(app, text = 'Filename').grid(row = 1, column = 0, padx = (80, 0), pady = 5)
fnameBox = ctk.CTkEntry(app, textvariable = output_filename).grid(row = 2, column = 0, padx = (80, 0), pady = 5)

label3 = ctk.CTkLabel(app, text = 'Your text goes here').grid(row = 3, column = 0, padx = (80, 0), pady = 5)
txtBox = ctk.CTkEntry(app, textvariable = input_text).grid(row = 4, column = 0, padx = (80, 0), pady = 5)

label4 = ctk.CTkLabel(app, text = 'Language').grid(row = 5, column = 0, padx = (80, 0), pady = 5)
langBox = ctk.CTkComboBox(app, variable = selected_language , values = languages).grid(row = 6, column = 0, padx = (80, 0), pady = 5)

CheckBtn1 = ctk.CTkSwitch(app, text = 'Slowmode', variable = use_slowmode).grid(row = 7, column = 0, padx = (80, 0), pady = 10)

btn = ctk.CTkButton(app, text = 'Generate', command = generate).grid(row = 8, column = 0, padx = (80, 5), pady = 20)
settings_btn = ctk.CTkButton(app, text = '⚙️', command = open_settings, width = 10).grid(row = 8, column = 1, pady = 20)

app.mainloop()
