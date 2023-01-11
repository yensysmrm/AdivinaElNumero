#Importando las clases
import tkinter as t
import random as ra
from playsound import playsound

#Definiendo el tamano de la ventana
pan=t.Tk()
pan.title("Adivina el valor")
pan.geometry("291x200")

#Variables
p=0
i=0
r=ra.randint(0, 100)

#Variables de texto
b=t.StringVar()
pu=t.StringVar()
tr=t.StringVar()
b.set("Introduce el número")
pu.set("Puntos:   "+str(p))
tr.set("Intentos: "+str(i))

#Introducir el numero
inputtxt = t.Text(pan,height = 1,width = 15)
inputtxt.pack()
inputtxt.place(x=39, y=78)

#pantalla puntuacion
campo=t.Label(pan,textvariable=pu,width=11,height=1,background="white",anchor="w")
campo.place(x=198, y=78)
#pantalla intentos
campo=t.Label(pan,textvariable=tr,width=11,height=1,background="white",anchor="w")
campo.place(x=198, y=100)
#Pantalla principal
cart=t.Label(pan,font=("Arial",10,"bold"),textvariable=b,foreground="black",width=20,height=1,anchor="w")
cart.place(x=39, y=38)

#Funciones
def func1():
    global i
    i+=1
    global pu
    tr.set("Intentos: "+str(i))

def func2():
    global p
    p+=1
    global pu
    pu.set("Intentos: "+str(p))

def func():
    global r
    try:
        a=int(inputtxt.get(1.0, "end-1c"))
        if (a < 0) or (a > 100):
            raise Exception("")
        else:
            func1()
            if a < r:
                b.set("El numero es mayor")
            elif a > r:
                b.set("El numero es menor")
            else:
                func2()
                b.set("FELICIDADES")
                playsound("victoria.wav")
                r=ra.randint(0, 100)

    except:
        b.set("Valor no valido")

foreground="black"
#Definiendo boton
boton1=t.Button(pan, text="Ok",command=func,foreground=foreground,width=2,height=1)
boton1.place(x=140, y=124)

pan.mainloop()
