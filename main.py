import tkinter
from tkinter.ttk import Progressbar
import customtkinter as ctk
from tkinterweb import HtmlFrame
import minecraft_launcher_lib
import asyncio  

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#global veriable 
minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()

class App(ctk.CTk):
    def __init__(self,loop) -> None:
        super().__init__()
        self.loop = loop
        #configure window
        self.title("Generic Mincraft Launcher")
        self.geometry("1200x800")

        # configure grid layour (4x4)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.rowconfigure((1),weight=1)
        self.rowconfigure(0,weight=0)

        # create side bar
        self.sidebar = ctk.CTkFrame(self,width=250,corner_radius=0)
        self.sidebar.grid(row=0,column=0,rowspan=2,sticky="nsew")
        # Create side bar grid and widgets
        self.sidebar.grid_columnconfigure(0,weight=1)
        self.logo_label = ctk.CTkLabel(self.sidebar,text="About Us:",font=("Arial",20))
        self.logo_label.grid(row=0,column=0,sticky="nsew",padx=20, pady=10)
        self.github_button = ctk.CTkButton(self.sidebar,text="Github")
        self.discord_button = ctk.CTkButton(self.sidebar,text="Discord")
        self.twitter_button = ctk.CTkButton(self.sidebar,text="Twitter")
        self.coffee_button = ctk.CTkButton(self.sidebar,text="Buy me a coffee")
        self.github_button.grid(row=1,column=0,sticky="nsew",padx=20, pady=10)
        self.discord_button.grid(row=2,column=0,sticky="nsew",padx=20, pady=10)
        self.twitter_button.grid(row=3,column=0,sticky="nsew",padx=20, pady=10)
        self.coffee_button.grid(row=4,column=0,sticky="nsew",padx=20, pady=10)

        # adding webview 
        """webview = HtmlFrame(self, horizontal_scrollbar="auto")
        webview.load_website("https://feedback.minecraft.net/hc/en-us/sections/360001186971-Release-Changelogs")
        webview.grid(row=0,column=1,sticky="nsew")
        """
        #temporary textbox
        self.label_name = ctk.CTkLabel(self,text="Berry Launcher",font=("Arial",40))
        self.label_name.grid(row=0,column=1,sticky="nsew",padx=20, pady=10)
        self.textbox = ctk.CTkTextbox(self, width=250)
        self.textbox.grid(row=1,column=1,sticky="nsew",padx=(5,20), pady=(10,0))
        # content bar bottom

        self.content_bar = ctk.CTkFrame(self,height=100,corner_radius=0)
        self.content_bar.grid(row=2,column=0,rowspan=3,columnspan=4,sticky="nsew",padx=0, pady=(10,0))
        self.content_bar.rowconfigure(2,weight=0)
        # Create content bar grid and widget
        self.version_label = ctk.CTkLabel(self.content_bar,text="Version:",fg_color='#2B2B2B')
        self.name_label = ctk.CTkLabel(self.content_bar,text="Name:",bg_color='#2B2B2B')
        self.version_box = ctk.CTkComboBox(self.content_bar,values=['loading'])
        self.name_entry = ctk.CTkEntry(self.content_bar,placeholder_text="Name",corner_radius=10)
        self.name_label.grid(row=3,column=0,sticky="nsew",padx=20, pady=10)
        self.version_label.grid(row=4,column=0,sticky="nsew",padx=20, pady=10)
        self.name_entry.grid(row=3,column=1,sticky="nsew",padx=20, pady=10)
        self.version_box.grid(row=4,column=1,sticky="nsew",padx=20, pady=10)
        self.start_button = ctk.CTkButton(self.content_bar,hover=True,hover_color="#455E34",fg_color='#7A9D5B',text="Start")
        self.start_button.grid(row=3,column=2,sticky="nsew",padx=20, pady=10)

    def start_game():
        minecraft_launcher_lib.install.install_minecraft_version("1.17", minecraft_directory)
        options = minecraft_launcher_lib.utils.generate_test_options()
        minecraft_command = minecraft_launcher_lib.command.get_minecraft_command("1.17", minecraft_directory, options)
        minecraft_launcher_lib.command.run_minecraft_command(minecraft_command)

    async def get_versions(self,version_box):
            versions =[]
            for i in minecraft_launcher_lib.utils.get_available_versions(minecraft_directory):
                if i['type']== 'release':
                    versions.append(i['id'])
            self.version_box.configure(values=versions)
            return versions
    
    def close(self):
        for task in self.tasks:
            task.cancel()
        self.loop.stop()
        self.destroy()

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    app = App(loop)
    try:
        asyncio.run(app.mainloop())
    except KeyboardInterrupt:
        pass