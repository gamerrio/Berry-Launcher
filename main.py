import tkinter
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        #configure window
        self.title("Generic Mincraft Launcher")
        self.geometry("1200x800")

        


if __name__ == "__main__":
    app = App()
    app.mainloop()