import os
import gtts
import json

import customtkinter as ctk
from tkinter.messagebox import showerror

app = ctk.CTk()

app.title('GoogleTTS GUI')
app.geometry('300x400')
app.resizable(width = False, height = False)

with open('language.json') as file:
    languages_list = json.load(file)

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


languages = sorted(languages_list.keys())

input_text = ctk.StringVar()
output_filename = ctk.StringVar()
selected_language = ctk.StringVar()
use_slowmode = ctk.BooleanVar()

label1 = ctk.CTkLabel(app, text = 'GoogleTTS GUI (v1.2)').pack(pady = (20, 15))

label2 = ctk.CTkLabel(app, text = 'Filename').pack(pady = 5)
fnameBox = ctk.CTkEntry(app, textvariable = output_filename).pack(pady = 5)

label3 = ctk.CTkLabel(app, text = 'Your text goes here').pack()
txtBox = ctk.CTkEntry(app, textvariable = input_text).pack(pady = 5)

label4 = ctk.CTkLabel(app, text = 'Language').pack()
langBox = ctk.CTkComboBox(app, variable = selected_language , values = languages).pack(pady = 5)

CheckBtn1 = ctk.CTkSwitch(app, text = 'Slowmode', variable = use_slowmode).pack(pady = 10)

btn = ctk.CTkButton(app, text = 'Generate', command = generate).pack(pady = 20)

app.mainloop()
