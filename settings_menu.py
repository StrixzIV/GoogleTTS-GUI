import os
import json
import customtkinter as ctk

class SettingsMenu(ctk.CTkToplevel):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.geometry('300x400')
        self.title('Settings')

        self.settings = self.load_settings()

        ctk.set_appearance_mode(self.settings['theme'])

        self.combobox1 = ctk.CTkComboBox(
            self,
            values = ['system', 'dark', 'light'], 
            variable = ctk.StringVar(value = self.settings['theme']),
            command = lambda choice: self.set_theme(choice)
        ).pack()


    def load_settings(self) -> dict:

        if not os.path.exists('./config/settings.json'):
            with open('./config/settings.json', 'w') as file:
                json.dump({'theme': 'system'}, file)

        with open('./config/settings.json') as file:
            return json.load(file)

    
    def write_settings(self, settings: dict) -> None:
        with open('./config/settings.json', 'w') as file:
            json.dump(settings, file)

    
    def set_theme(self, theme):
        
        self.settings['theme'] = theme
        ctk.set_appearance_mode(theme)

        self.write_settings(self.settings)

