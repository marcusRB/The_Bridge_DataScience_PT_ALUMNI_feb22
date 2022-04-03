import os
from tkinter import *
from tkinter import messagebox

def organiza_os():

    global ruta_origen,rd,ri,rs,ro
    ruta_origen,rd,ri,rs,ro =e1.get(), e2.get(),e3.get(),e4.get(),e5.get()
    nombres = os.listdir(ruta_origen)
    documentos = (".txt",".docx",".doc",".xlsx",".xls",".pptx",".ppt",".pdf",".csv")
    imagenes = (".png",".jpg",".jpeg",".gif",".tif",".svg",".tiff")
    software = (".exe","pkg",".dmg")

    def comprobador_vacio():
        """comprueba que haya archivos que organizar en el directorio"""
        counter = 0
        for f in nombres:
            path = f"{ruta_origen}/{f}"
            check = os.path.isfile(path)
            if check == True:
                counter += 1
        return counter

    def organizador():

        """cambia los archivos en el directorio origen indicado a los directorios 
        destino que se establezca según la extensión de estos"""
        
        for nombre in nombres:
            file = f"{ruta_origen}/{nombre}"
            if os.path.isfile(file):
                if nombre.lower().endswith(documentos):
                    new_file = f"{rd}/{nombre}"
                    os.rename(file,new_file)
                elif nombre.lower().endswith(imagenes):
                    new_file = f"{ri}/{nombre}"
                    os.rename(file,new_file)
                elif nombre.lower().endswith(software):
                    new_file = f"{rs}/{nombre}"
                    os.rename(file,new_file)
                else:
                    new_file = f"{ro}/{nombre}"
                    os.rename(file,new_file)
            else:
                continue

    vacio = comprobador_vacio()
    if vacio != 0:
        organizador()
        messagebox.showinfo(message=' ficheros organizados correctamente',title = 'Info')
    else:
        messagebox.showerror(message="El directorio no tiene archivos que organizar",title="Info")

window= Tk()
window.title("APLICACION")
window.geometry("800x275")
window.geometry("+{}+{}".format(550,180))

l1=Label(window,text='',fg="#13375B", font=('Helvetica', 11,'bold'), height=1, anchor="e",width=20)
l1.grid(row=0)
l1=Label(window,text='',fg="#13375B", font=('Helvetica', 11,'bold'), height=1, anchor="e",width=20)
l1.grid(row=1)

ruta_origen = StringVar(value = 'Escribe la ruta de origen a organizar')
l1=Label(window,text='Ruta Origen',fg="#13375B", font=('Helvetica', 11,'bold'), height=1, anchor="e",width=20)
l1.grid(row=3,column=0)
e1=Entry(window,textvariable=ruta_origen ,width=85,fg="#13375B",font=('Helvetica', 9))
e1.grid(row=3,column=1)

rd = StringVar(value="Escribe la ruta destino para los documentos")
l2=Label(window,text='Ruta Docs',fg="#13375B", font=('Helvetica', 11), height=1, anchor="e",width=20)
l2.grid(row=4,column=0)
e2=Entry(window,textvariable=rd ,width=85,fg="#13375B",font=('Helvetica', 9))
e2.grid(row=4,column=1)

ri = StringVar(value="Escribe la ruta destino para las imágenes")
l3=Label(window,text='Ruta Imágenes',fg="#13375B", font=('Helvetica', 11), height=1, anchor="e",width=20)
l3.grid(row=5,column=0)
e3=Entry(window,textvariable=ri ,width=85,fg="#13375B",font=('Helvetica', 9))
e3.grid(row=5,column=1)

rs = StringVar(value="Escribe la ruta destino para los archivos de software")
l4=Label(window,text='Ruta Software',fg="#13375B", font=('Helvetica', 11), height=1, anchor="e",width=20)
l4.grid(row=6,column=0)
e4=Entry(window,textvariable=rs ,width=85,fg="#13375B",font=('Helvetica', 9))
e4.grid(row=6,column=1)

ro = StringVar(value="Escribe la ruta destino para lo que no sea lo anterior")
l5=Label(window,text='Ruta Otros',fg="#13375B", font=('Helvetica', 11), height=1, anchor="e",width=20)
l5.grid(row=7,column=0)
e5=Entry(window,textvariable=ro ,width=85,fg="#13375B",font=('Helvetica', 9))
e5.grid(row=7,column=1)

b1 = Button(window,text='ORGANIZAR',width=10,height=1,bg='#13B833',fg='White',command=organiza_os,font=('Helvetica',11,'bold'))
b1.place(x=350,y=175)

window.grid_columnconfigure(6, minsize=120)
window.grid_rowconfigure(8, minsize=120)
window.mainloop()