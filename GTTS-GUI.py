from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from gtts import gTTS as tts
import os

#Window setups
screen = Tk()

screen.title('GoogleTTS GUI')
screen.geometry('300x320')
screen.resizable(width = False, height = False)

#a main speech synthesis function
def generate():
    
    #set save as file directory
    dir = filedialog.askdirectory()
    os.chdir(dir)
    
    #Language code dict
    langDict = {'English':'en',
                'Thai':'th',
                'Japanese':'ja',
                'Korean':'ko',
                'German':'de',
                'Russian':'ru',
                'Indonesia':'id',
                'Polish':'pl',
                'Chinese(Simplified)':'zh-CN',
                'Chinese(Traditional)':'zh-TW',
                'Vietnamese':'vi',
                'Arabic':'ar',
                'Bengali':'bn',
                'Welsh':'cy',
                'Ukrainian':'uk',
                'Turkish':'tr',
                'Bulgarian':'bg',
                'Catalan':'ca',
                'Dutch':'nl',
                'Filipino':'fil',
                'France':'fr',
                'Finnish':'fi',
                'Greek':'el',
                'Hebrew':'iw',
                'Hindi':'hi',
                'Hungarian':'hu',
                'Italian':'it',
                'Portuguese(Portugal)':'pt-PT',
                'Portuguese(Brazil)':'pt-BR',
                'Romanian':'ro',
                'Spanish':'es',
                'Swedish':'sv',
                'Malay':'ms'}
    
    #Speech synthesis
    inpText = txt.get()
    filename = fname.get()
    inpLang = selLang.get()
    to_spleech = tts(text = inpText, lang = langDict[inpLang], lang_check = False)
    to_spleech.save(filename + '.mp3')


#Combobox values
langCode = ('Arabic',
            'Bengali',
            'Bulgarian',
            'Catalan',
            'Chinese(Simplified)',
            'Chinese(Traditional)',
            'Dutch',
            'English',
            'France',
            'Finnish',
            'Filipino',
            'German',
            'Greek',
            'Hebrew',
            'Hindi',
            'Hungarian',
            'Italian',
            'Indonesia',
            'Japanese',
            'Korean',
            'Malay',
            'Polish',
            'Portuguese(Portugal)',
            'Portuguese(Brazil)',
            'Romanian',
            'Russian',
            'Spanish',
            'Swedish',
            'Thai',
            'Turkish',
            'Ukrainian',
            'Vietnamese',
            'Welsh')

#Widget
txt = StringVar()
fname = StringVar()
selLang = StringVar()

label1 = Label(screen, text = 'GoogleTTS GUI(v1.0)', fg = 'black').pack(pady = 25)

label2 = Label(screen, text = 'Filename', fg = 'black').pack(pady = 5)
fnameBox = Entry(screen, textvariable = fname, bg = 'white', fg = 'black').pack()

label3 = Label(screen, text = 'Your text goes here', fg = 'black').pack()
txtBox = Entry(screen, textvariable = txt, bg = 'white', fg = 'black').pack(pady = 5)

label4 = Label(screen, text = 'Language', fg = 'black').pack()
langBox = ttk.Combobox(screen, foreground = 'black', textvariable = selLang , values = langCode).pack()
btn = Button(text = 'Generate', fg = 'red', font = 20, command = generate).pack(pady = 25)
screen.mainloop()
