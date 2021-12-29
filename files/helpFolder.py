import tkinter as tk
from tkinter import Message, ttk
from tkinter import scrolledtext as tx
from tkinter import messagebox as mb
import cairosvg
import io
from PIL import ImageTk, Image

class helpInter(tk.Frame):
    def __init__(self,container,*args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(width=550,height=550)
        self.rowconfigure(1,weight=2)
        self.columnconfigure(1,weight=2)
        self.elemt()


    def elemt(self):
    
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
                                 bg="#FF8C00", activebackground="#FF8C00", text="Usuarios", image=self.img_user)
        self.btnUser.grid(row=0, column=4)
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        self.btnUser.configure(height=40, width=100, compound="r")

# -------------------------------------------btn- help-----------------------------------------------
        self.btn_help = tk.Button(self, relief='raised', borderwidth=5,
                                  bg="#FF8C00", activebackground="#FF8C00", text="Informacion", image=self.img_help)
        self.btn_help.grid(row=1, column=4 )
        self.btn_help.configure(height=40, width=100, compound="r")

# -------------------------------------------btn- exit-----------------------------------------------
        self.btn_exit = tk.Button(self, relief='raised', borderwidth=5,
                                  bg="#FF8C00", activebackground="#FF8C00", text="Salir", image=self.img_exit,)
        self.btn_exit.grid(row=2, column=4)
        self.btn_exit.configure(height=40, width=100, compound="r")


# -----------------------------------------btn options-----------------------------------------
        self.btn_opt = tk.Button(self, relief='raised', borderwidth=5, bg="#FF8C00",
                                 activebackground="#FF8C00", image=self.tk_image, text='Opciones')
        self.btn_opt.configure(height=40, width=100, compound="r")
        self.btn_opt.grid(row=3, column=4)

        self.rowconfigure(1,weight=1)
        self.columnconfigure(1,weight=1)
        self.rowconfigure(2,weight=1)
        self.columnconfigure(2,weight=1)
        self.rowconfigure(3,weight=1)
        self.columnconfigure(3,weight=1)