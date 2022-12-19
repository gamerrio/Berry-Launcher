import tkinter
import customtkinter as ctk
from tkinterweb import HtmlFrame

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        #configure window
        self.title("Generic Mincraft Launcher")
        self.geometry("1200x800")

        # configure grid layour (4x4)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=1)

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
        webview = HtmlFrame(self, horizontal_scrollbar="auto")
        webview.load_website("https://google.com")
        webview.grid(row=0,column=1,sticky="nsew")

if __name__ == "__main__":
    app = App()
    app.mainloop()