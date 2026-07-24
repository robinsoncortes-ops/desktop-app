from tkinter import *
from tkinter import messagebox

# funciones de app
def salir():
    messagebox.showinfo("suma 1,0", "hizo clik en el boton salir...")
    ventana_principal.destroy()

def borrar():
    messagebox.showinfo("suma 1,0", " los datos seran borrados")
    x.set("")
    y.set("")
    t_resultodos.delete("1.0", "end")

def sumar():
    messagebox.showinfo(" suma 1,0","hizo clik en el boton de sumar...")
    z = int(x.get()) + int(y.get())
    t_resultodos.insert(INSERT, " la suma de " + x.get() + " + " + y.get() + "casi siempre es " + str(z) + "\n")

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

# variables globales
x = StringVar()
y = StringVar()

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

# boton para sumar
bt_sumar = Button(frame_operaciones, text="Sumar", command=sumar)
bt_sumar.place(x=45,y =45, width=120, height=30)

# boton para borrar
bt_sumar = Button(frame_operaciones, text="borrar", command=borrar)
bt_sumar.place(x=200,y =45, width=120, height=30)

# boton para salir
bt_sumar = Button(frame_operaciones, text="salir", command=salir)
bt_sumar.place(x=350,y =45, width=120, height=30)



#agregamos una imagen al frame 
escudo = PhotoImage(file="img/escudoColegio.png")
lb_escudo = Label(frame_entrada, image=escudo)
lb_escudo.place(x=10, y=20)

# label para titulo de la app
titulo = Label(frame_entrada, text="suma numero enteros")
titulo.config(bg="yellow", fg="blue",font=("arial",16))
titulo.place(x=200, y=5)

# label para titulo de la app
lb_x = Label(frame_entrada, text="X = ")                        
lb_x.config(bg="yellow", fg="blue",font=("TIME NEW ROMAN",16))
lb_x.place(x=200, y=50)

# Entrada para el valor de X
entry_x = Entry(frame_entrada, textvariable=x)
entry_x.config(bg="white", fg="black", font=("Times New Roman",16))
entry_x.focus_set()
entry_x.place(x=249, y=50, width=150, height=30)

lb_y = Label(frame_entrada, text="y = ")
lb_y.config(bg="yellow", fg="blue",font=("TIME NEW ROMAN",16))
lb_y.place(x=200, y=100)

# Entrada para el valor de y
entry_x = Entry(frame_entrada, textvariable=y)
entry_x.config(bg="white", fg="black", font=("Times New Roman",16))
entry_x.focus_set()
entry_x.place(x=250, y=100, width=150, height=30)

#-------------------------------------------------
#frame resultados
#------------------------------------------------
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="#BA0C2F" , width=480, height=120)
frame_resultados.place(x=10,y=390)

# AREA de texto para resultdos
t_resultodos = Text(frame_resultados)
t_resultodos.config(bg= "yellow", fg="black", font=("Arial", 28))
t_resultodos.place(x=10, y=10, width= 460, height=90)


# bucle principal
ventana_principal.mainloop()