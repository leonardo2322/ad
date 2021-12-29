import tkinter as tk
from tkinter import Message, ttk
from tkinter import scrolledtext as txtsc
from tkinter import messagebox as mb
import cairosvg
import io
from PIL import ImageTk, Image
import files.user as user
import files.helpFolder as helpFolder
import files.options as options


class FrameUsers(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # --------------------------------------------window------------------------------------------
        self.title("Administrador Profesional")
        self.geometry("1000x850")


# --------------------------------------------images- home----------------------------------
        image_data = cairosvg.svg2png(url="img/example.svg")
        imageh = Image.open(io.BytesIO(image_data))
        imageh = imageh.resize((16, 16), Image.ANTIALIAS)

        self.tk_image = ImageTk.PhotoImage(imageh)
# -----------------------------Image user------------------------------------------------
        image_data_user = cairosvg.svg2png(url="img/user.svg")
        image_user = Image.open(io.BytesIO(image_data_user))
        image_user = image_user.resize((16, 16), Image.ANTIALIAS)

        self.img_user = ImageTk.PhotoImage(image_user)

# ----------------------------------image help -------------------------------------------
        image_data_help = cairosvg.svg2png(url="img/info.svg")
        image_help = Image.open(io.BytesIO(image_data_help))
        image_help = image_help.resize((16, 16), Image.ANTIALIAS)

        self.img_help = ImageTk.PhotoImage(image_help)

# -----------------------------------------Image exit------------------------------------------

        image_data_exit = cairosvg.svg2png(url="img/exit.svg")
        image_exit = Image.open(io.BytesIO(image_data_exit))
        image_exit = image_exit.resize((16, 16), Image.ANTIALIAS)

        self.img_exit = ImageTk.PhotoImage(image_exit)
# -------------------------------------------Buttons btn user---------------------------------------
        self.btnUser = tk.Button(self, relief='raised', borderwidth=5,
                                 bg="#FF8C00", activebackground="#FF8C00", text="Usuarios", image=self.img_user, font="Pushster", command=lambda: self.notebookUser())
        self.btnUser.grid(row=0, column=4)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.btnUser.configure(height=40, width=100, compound="r")

# -------------------------------------------btn- help-----------------------------------------------
        self.btn_help = tk.Button(self, relief='raised', borderwidth=5,
                                  bg="#FF8C00", activebackground="#FF8C00", text="Informacion", image=self.img_help, font="Pushster", command=lambda: self.notebookhelp())
        self.btn_help.grid(row=2, column=4)
        self.btn_help.configure(height=40, width=100, compound="r")

# -------------------------------------------btn- exit-----------------------------------------------
        self.btn_exit = tk.Button(self, relief='raised', borderwidth=5,
                                  bg="#FF8C00", activebackground="#FF8C00", text="Salir", font="Pushster",image=self.img_exit, command=lambda: self.destroy())
        self.btn_exit.grid(row=3, column=4)
        self.btn_exit.configure(height=40, width=100, compound="r")


# -----------------------------------------btn options-----------------------------------------
        self.btn_opt = tk.Button(self, relief='raised', borderwidth=5, bg="#FF8C00",
                                 activebackground="#FF8C00", image=self.tk_image, font="Pushster", text='Opciones',command=lambda:self.notebooOptions())
        self.btn_opt.configure(height=40, width=100, compound="r")
        self.btn_opt.grid(row=1, column=4)

        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.columnconfigure(3, weight=1)


# ------------------------------------------callbacks----------------------------------------------------------


# ------------------------------------------notebook--------------------------------------------------------

    def notebookUser(self):
        self.user = ttk.Notebook(self)
        self.user.grid(row=1, column=1, padx=20, pady=40,
                       ipadx=20, ipady=20, sticky="nsew")
        frameUser = user.UserInterf(self.user)
        self.user.add(frameUser, text="Inicio Sesion")
        frameUser.tkraise()
        return frameUser

    def notebookhelp(self):
        self.help = ttk.Notebook(self)
        self.help.grid(row=1, column=1, padx=20, pady=40,
                       ipadx=20, ipady=20, sticky="nsew")
        framehelp = helpFolder.helpInter(self.help)
        self.help.add(framehelp, text="help")
        framehelp.tkraise()
        return framehelp
        
    def notebooOptions(self):
        self.Options = ttk.Notebook(self)
        self.Options.grid(row=1, column=1, padx=20, pady=40,
                       ipadx=20, ipady=20, sticky="nsew")
        frameOptions = options.OptionsInterf(self.Options)
        self.Options.add(frameOptions, text="help")
        frameOptions.tkraise()
        return frameOptions


if __name__ == "__main__":
    wind = FrameUsers()
    wind.mainloop()
