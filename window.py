import tkinter as tk
from tkinter import Message, ttk
from tkinter import scrolledtext as tx
from tkinter import messagebox as mb
import cairosvg
import io
from PIL import ImageTk, Image


class FrameUsers:
    def __init__(self):
        # --------------------------------------------window------------------------------------------
        self.ventana = tk.Tk()
        self.ventana.title("Administrador Profesional")


# ------------------------------------------notebook--------------------------------------------------------
        self.cuaderno = ttk.Notebook(self.ventana)

        self.cuaderno.grid(row=0, column=0)
# ------------------------------------------callbacks----------------------------------------------------------
        self.elemt()
        self.ventana.mainloop()

    def hola(self):
        saludo = mb.askokcancel("Patricia","hola patricia asi funciona un boton")
        if saludo:
            self.ventana.destroy()
        else:
            mb.showinfo("todo","ha salido bien")

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

# ----------------------------------image ayuda -------------------------------------------
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
        self.btnUser = tk.Button(self.cuaderno, relief='raised', borderwidth=5,
                                 bg="#FF8C00", activebackground="#7FFF00", text="Usuarios", image=self.img_user, command=lambda: self.hola())
        self.btnUser.grid(row=1, column=2)
        self.btnUser.configure(height=40, width=100, compound="r")

# -------------------------------------------btn- help-----------------------------------------------
        self.btn_help = tk.Button(self.cuaderno, relief='raised', borderwidth=5,
                                  bg="#FF8C00", activebackground="#FF8C00", text="Informacion", image=self.img_help)
        self.btn_help.grid(row=1, column=3)
        self.btn_help.configure(height=40, width=100, compound="r")

# -------------------------------------------btn- exit-----------------------------------------------
        self.btn_exit = tk.Button(self.cuaderno, relief='raised', borderwidth=5,
                                  bg="#FF8C00", activebackground="#FF8C00", text="Salir", image=self.img_exit)
        self.btn_exit.grid(row=1, column=4)
        self.btn_exit.configure(height=40, width=100, compound="r")


# -----------------------------------------btn options-----------------------------------------
        self.btn_opt = tk.Button(self.cuaderno, relief='raised', borderwidth=5, bg="#FF8C00",
                                 activebackground="#FF8C00", image=self.tk_image, text='Opciones')
        self.btn_opt.configure(height=40, width=100, compound="r")
        self.btn_opt.grid(row=1, column=1)


if __name__ == "__main__":
    wind = FrameUsers()
