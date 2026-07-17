from tkinter import *

# ventana principal
ventana_principal = Tk()

# titulo
ventana_principal.title("bandera")

# tamaño de la vantana
ventana_principal.geometry("850x550")

# color de fondo
ventana_principal.config(bg="white")

#deshabilitar boton de maxinizar
ventana_principal.resizable(0,0)

# agregamos un objeto tipo frame
frame_1 = Frame(ventana_principal)
frame_1.config(bg="red", width=300, height=220)
frame_1.place(x=10,y=10)
frame_2 = Frame(ventana_principal)
frame_2.config(bg="red", width=300, height=220)
frame_2.place(x=10,y=330)
frame_3 = Frame(ventana_principal)
frame_3.config(bg="red", width=450, height=220)
frame_3.place(x=400, y=330 )
frame_4 = Frame(ventana_principal)
frame_4.config(bg="red", width=450, height=220)
frame_4.place(x=400, y=10)
frame_5 = Frame(ventana_principal)
frame_5.config(bg="blue", width=55,  height= 800)
frame_5.place(x=330,y=10)
frame_6 = Frame(ventana_principal)
frame_6.config(bg="blue", width=850, height=60)
frame_6.place(x=10,y=250)

# bucle principal
ventana_principal.mainloop()
