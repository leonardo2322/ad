import tkinter as tk
from tkinter import Message, ttk
from tkinter import scrolledtext as tx
from tkinter import messagebox as mb
import cairosvg
import io
from PIL import ImageTk, Image

class UserInterf(tk.Frame):
    def __init__(self,container,*args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(width=550,height=550)
        self.columnconfigure(1,weight=1)
        self.elemt()



    def elemt(self):
#-----------------------------image--------------------------------------------        
        image_data_conec = cairosvg.svg2png(url="img/key.svg")
        imageconect = Image.open(io.BytesIO(image_data_conec))
        imageconect = imageconect.resize((16, 16), Image.ANTIALIAS)

        self.imgconect = ImageTk.PhotoImage(imageconect)


        image_data_exit = cairosvg.svg2png(url="img/exit.svg")
        image_exit = Image.open(io.BytesIO(image_data_exit))
        image_exit = image_exit.resize((16, 16), Image.ANTIALIAS)

        self.img_exit = ImageTk.PhotoImage(image_exit)
#--------------------------------Entryes------------------------------------------
        text_user_input= tk.Label(self, text="Introduce tu Usuario", font="Pushster")
        text_user_input.grid(row=0,column=1,pady=10,padx=10)
        
        self.UserInput= tk.Entry(self, width=40)
        self.UserInput.grid(row=1,column=1)
        
        text_passwor = tk.Label(self, text="Introduce tu contraseña", font="Pushster")
        text_passwor.grid(row=2,column=1, padx=10,pady=10)
        
        self.passInput=tk.Entry(self,width=40, show="*")
        self.passInput.grid(row=3,column=1)
#--------------------------------------Btn--------------------------------------------------


        self.btnConect = tk.Button(self, text="Entrar",relief='raised', borderwidth=5,
                                 bg="#FF8C00", activebackground="#FF8C00",image=self.imgconect, font="Pushster")
        self.btnConect.grid(row=4,column=1, padx=10,pady=10) 

        self.btnConect.configure(height=30, width=60, compound="r")
    

        self.btnExit = tk.Button(self, text="Salir",relief='raised', borderwidth=5,
                                 bg="#FF8C00", activebackground="#FF8C00",image=self.img_exit, font="Pushster", command=lambda:self.destroy())
        self.btnExit.grid(row=5, column=2, padx=8,pady=8)
        self.btnExit.configure(height=25, width=50, compound="r")