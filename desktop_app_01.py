from tkinter import *

# ventana principal
ventana_principal = Tk()

# titulo
ventana_principal.title("sistemas guanenta")

# tamaño de la vantana
ventana_principal.geometry("500x500")

# color de fondo
ventana_principal.config(bg="red")

#deshabilitar boton de maxinizar
ventana_principal.resizable(0,0)

# agregamos un objeto tipo frame
frame_1 = Frame(ventana_principal)
frame_1.config(bg="green", width=480, height=240)
frame_1.place(x=10,y=10)

# agregamos una imagen al frame
escudo = PhotoImage(file="img/escudoColegio.png")
lb_escudo = Label(frame_1, image=escudo)
lb_escudo.place(x=10, y=20)


# bucle principal
ventana_principal.mainloop()
