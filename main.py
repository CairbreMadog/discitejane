import tkinter
import tkinter.messagebox
import customtkinter
import pyttsx3
import threading

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

engine = pyttsx3.init()
engine.setProperty('rate', 255)




class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Discite")
        self.geometry(f"{1100}x{580}")


        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)


        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Full", command=self.fullscreen_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Not Full",  command=self.normalscreen_button_event)
        self.sidebar_button_2.grid(row=1, column=2, padx=20, pady=10)



    def sidebar_button_event(self):
        print("sidebar_button click")
    def fullscreen_button_event(self):
        print("full")
        app.attributes("-fullscreen", "True")

        text = "What is 3 times 4?"
        engine.runAndWait()

        threading.Thread(target=say, args=(text,)).start()

    def normalscreen_button_event(self):
        print("not full")
        app.attributes("-fullscreen", "False")

def say(text):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 350)
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    app = App()
    app.mainloop()
