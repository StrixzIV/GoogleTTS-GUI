from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror
from tkinter import filedialog
from gtts import gTTS as tts
from gtts.tts import gTTSError
import os
import json

# Window setups
screen = Tk()

screen.title('GoogleTTS GUI')
screen.geometry('300x340')
screen.resizable(width = False, height = False)

# get the language codes
with open('language.json') as fs:
    langDict = json.load(fs)

# a main speech synthesis function
def generate() -> None:
    
    '''
        Send request to google text-to-spleech API and save output file to the target directory
    '''
    
    try:
        # set save as file directory
        dir = filedialog.askdirectory()
        os.chdir(dir)
        
        # Speech synthesis
        inpText = txt.get()
        filename = fname.get()
        inpLang = selLang.get()
        isSlowed = setSlow.get()
        to_spleech = tts(text = inpText, lang = langDict[inpLang], lang_check = False, slow = isSlowed)
        to_spleech.save(filename + '.mp3')

    # Error handler
    except gTTSError:
        showerror('Error', 'Cannot generate audio file.')

    except OSError:
        showerror('Error', 'Directory not selected.')


# Combobox values
langCode = sorted(langDict.keys())

# Widget
txt = StringVar()
fname = StringVar()
selLang = StringVar()
setSlow = BooleanVar()

label1 = Label(screen, text = 'GoogleTTS GUI(v1.2)', fg = 'black').pack(pady = 20)

label2 = Label(screen, text = 'Filename', fg = 'black').pack(pady = 5)
fnameBox = Entry(screen, textvariable = fname, bg = 'white', fg = 'black').pack()

label3 = Label(screen, text = 'Your text goes here', fg = 'black').pack()
txtBox = Entry(screen, textvariable = txt, bg = 'white', fg = 'black').pack(pady = 5)

label4 = Label(screen, text = 'Language', fg = 'black').pack()
langBox = ttk.Combobox(screen, foreground = 'black', textvariable = selLang , values = langCode).pack(pady = 5)

CheckBtn1 = Checkbutton(screen, text = 'Slowmode', fg = 'black', variable = setSlow).pack(pady = 10)

btn = Button(text = 'Generate', fg = 'red', font = 20, command = generate).pack(pady = 5)

screen.mainloop()
