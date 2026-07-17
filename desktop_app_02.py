from tkinter import *
from tkinter import messagebox

# ventana principal
ventana_principal = Tk()

# titulo
ventana_principal.title("sistemas guanenta")

# tamaño de la vantana
ventana_principal.geometry("500x500")

# color de fonde a la pantalla
ventana_principal.config(bg="black")

# deshabilitar el boton de maximizar
ventana_principal.resizable(0,0)

#------------------------------------------------
# frame entrada de datos
#------------------------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="#BA0C2F" , width=480, height=240)
frame_entrada.place(x=10,y=10)

#-------------------------------------------------
#frame operaciones
#------------------------------------------------
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="#BA0C2F" , width=480, height=120)
frame_operaciones.place(x=10,y=260)

#-------------------------------------------------
#frame resultados
#------------------------------------------------
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="#BA0C2F" , width=480, height=120)
frame_resultados.place(x=10,y=390)

#agregamos una imagen al frame 
escudo = PhotoImage(file="img/escudoColegio.png")
lb_escudo = Label(frame_entrada, image=escudo)
lb_escudo.place(x=10, y=20)


# bucle principal
ventana_principal.mainloop()
