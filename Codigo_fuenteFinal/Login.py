import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
def login():
    """
    Funcion que hace todo el login
    """
    dic=['123456']
    #esta es la clave que permite crear usuarios administradores
    def iniciar_cesion():
        """funcion que llama una ventana donde se da la opcion de escoger la forma como quiere entregar al programa
         la funcion no recibe nada
        :return  None"""
        ventana = tk.Tk()
        ventana.title('Inicio de Sesión')
        ventana.geometry('400x300')
        titulo_1 = tk.Label(ventana, text='SELECCIONE:', font=('Arial bold', 11))
        titulo_1.pack()
        selec_1 = tk.Button(ventana, text='Iniciar como Administrador', padx=65, pady=10,command=ini_usu_admini)
        selec_1.pack()
        selec_2 = tk.Button(ventana, text='Iniciar como Usuario Normal', padx=62, pady=10, command=ini_usu_normal)
        selec_2.pack()
        def close_window():
            ventana.destroy()
        """funcion para destruir una pestaña 
            no recibe 
         :return None """
        salida = tk.Button(ventana, text='Salida', padx=40, pady=10, bg='red', command=close_window)
        salida.pack()


    def ini_usu_admini():
        """ Funcion que abre una ventana donde hay dos entradas de texto. una de usuario y la otra de contraseña
        no recibe no retorna"""

        ventana = tk.Tk()
        ventana.title('Inicio de Sesión usuario normal')
        ventana.geometry('400x300')
        titulo_1 = tk.Label(ventana, text='Usuario', font=('Arial bold', 11))
        titulo_1.pack()
        usuario = tk.Entry(ventana, font='Arial 12')
        usuario.pack()
        titulo_2 = tk.Label(ventana, text='Contraseña', font=('Arial bold', 11))
        titulo_2.pack()
        contraseña = tk.Entry(ventana, font='Arial 12')
        contraseña.pack()
        def cor():
            """funcion que analiza si el usuario y contraseña existen, si es asi le permite entrar al programa en modo administrador
            la funcion no recibe
            :return None """
            with open("usuarios_Ad.txt") as lineas:
                dic = {}
                for x in lineas:
                    x = x.split(" : ")
                    dic[x[0]] = x[1]
            if usuario.get() in dic:
                if contraseña.get() == dic[usuario.get()]:
                    messagebox.showinfo(message="Felicitaciones", title="inicio exitoso")
                else:
                    messagebox.showinfo(message="Clave incorrecta", title="Error")
            else:
                messagebox.showinfo(message="Usuario inexistente", title="Error")

        listo = tk.Button(ventana, text='Presione al terminar', padx=30, pady=10, command=cor)
        listo.pack()
        def close_window():
            """funcion para destruir una pestaña #
              no recibe
              :return None """
            ventana.destroy()

        salida = tk.Button(ventana, text='Salida', padx=40, pady=10, bg='red', command=close_window)
        salida.pack()

    def ini_usu_normal():
        """ Funcion que abre una ventana donde hay dos entradas de texto. una de usuario y la otra de contraseña
                    no recibe no retorna"""
        ventana = tk.Tk()
        ventana.title('Inicio de Sesión usuario normal')
        ventana.geometry('400x300')
        titulo_1 = tk.Label(ventana, text='Usuario', font=('Arial bold', 11))
        titulo_1.pack()
        usuario = tk.Entry(ventana, font='Arial 12')
        usuario.pack()
        titulo_2 = tk.Label(ventana, text='Contraseña', font=('Arial bold', 11))
        titulo_2.pack()
        contraseña = tk.Entry(ventana, font='Arial 12')
        contraseña.pack()
        def cor():
            """funcion que analiza si el usuario y contraseña existen, si es asi le permite entrar al programa en modo normal
             la funcion no recibe
             :return None """

            with open("usuarios.txt") as lineas:
                dic = {}
                for x in lineas:
                    x = x.split(" : ")
                    dic[x[0]] = x[1]
            if usuario.get() in dic:
                if contraseña.get() == dic[usuario.get()]:
                    messagebox.showinfo(message="Felicitaciones", title="inicio exitoso")
                else:
                    messagebox.showinfo(message="Clave incorrecta", title="Error")
            else:
                messagebox.showinfo(message="Usuario inexistente", title="Error")
        listo = tk.Button(ventana, text='Presione al terminar', padx=30, pady=10,command=cor)
        listo.pack()

        def close_window():
            """ funcion para destruir una pestaña
               no recibe
               :return None """
            ventana.destroy()

        salida = tk.Button(ventana, text='Salida', padx=40, pady=10, bg='red', command=close_window)
        salida.pack()


    def usuario_normal():
        """ funcion que abre pestaña de usuario normal
        no recibe no retorna"""
        ventana = tk.Tk()
        ventana.title('Usuario Normal')
        ventana.geometry('400x300')
        titulo_1 = tk.Label(ventana, text='Usuario Nuevo', font=('Arial bold', 11))
        titulo_1.pack()
        usuario = tk.Entry(ventana, font='Arial 12')
        usuario.pack()
        titulo_2 = tk.Label(ventana, text='Contraseña', font=('Arial bold', 11))
        titulo_2.pack()
        contraseña = tk.Entry(ventana, font='Arial 12')
        contraseña.pack()
        def gua():
            """ Funcion que añade usuario normal al archivo .txt
             no recibe no retorna
             modifica el archivo usuarios.txt"""
            dic = [usuario.get(), contraseña.get()]
            new = f"{dic[0]} : {dic[1]} : k\n"
            claves = open('usuarios.txt', 'a')
            claves.write(new)
            claves.close()
            messagebox.showinfo(message="Ya puede iniciar sesión ", title="Guardado correcto")
            ventana.destroy()

        listo = tk.Button(ventana, text='Presione al terminar', padx=20, pady=10, comman=gua)
        listo.pack()
        def close_window():
            """funcion para destruir una pestaña"""
            ventana.destroy()


        salida = tk.Button(ventana, text='Salida', padx=40, pady=10, bg='red', command=close_window)
        salida.pack()

    def usuario_admi():
        """funcion que abre pestaña para la creacion de un usuario Administrador
         no recibe no retorna"""
        ventana = tk.Tk()
        ventana.title('Usuario Administrador')
        ventana.geometry('400x300')
        titulo_1 = tk.Label(ventana, text='Clave para Crear Usuario Administrador', font=('Arial bold', 11))
        titulo_1.pack()
        usuario = tk.Entry(ventana, font='Arial 12')
        usuario.pack()
        def com():
            """Funcion que revisa que la clave para usuario administrador sea la misma digitada y habilita otras opciones
            no recibe no retorna"""
            cla=usuario.get()
            if cla == dic[0]:
                titulo_1 = tk.Label(ventana, text='Usuario nuevo', font=('Arial bold', 11))
                titulo_1.pack()
                usuario_2 = tk.Entry(ventana, font='Arial 12')
                usuario_2.pack()
                titulo_2 = tk.Label(ventana, text='Contraseña', font=('Arial bold', 11))
                titulo_2.pack()
                contraseña = tk.Entry(ventana, font='Arial 12')
                contraseña.pack()
                def gua():
                    """funcion que permite guardar el nuevo usuario en un archivo .txt
                     recibe no retorna
                     modifica archivo usuarios_Ad.txt"""
                    dic=[usuario_2.get(),contraseña.get()]
                    new = f"{dic[0]} : {dic[1]} : k\n"
                    claves = open('usuarios_Ad.txt', 'a')
                    claves.write(new)
                    messagebox.showinfo(message="Ya puede iniciar sesion ", title="Guardado correcto")
                    ventana.destroy()

                listo = tk.Button(ventana, text='Presione al terminar', padx=20, pady=10, comman=gua)
                listo.pack()
            else:
                messagebox.showinfo(message="Clave incorrecta", title="Error")

        listo = tk.Button(ventana, text='Presione al terminar', padx=30, pady=10,comman=com)
        listo.pack()
        def close_window():
            """Funcón para destruir una pestaña"""
            ventana.destroy()

        salida = tk.Button(ventana, text='Salida', padx=40, pady=10,bg='red',command=close_window)
        salida.pack()


    def selec_nuevo_usuario():
        """funcion que abre una pestaña y da a seleccionar si quiere crear un usuario normal o uno administrador
         no recibe no retorna"""
        ventana=tk.Tk()
        ventana.title('Nuevo usuario')
        ventana.geometry('400x300')
        titulo_1 = tk.Label(ventana, text='SELECCIONAR OPCIÓN:', font=('Arial bold', 11))
        titulo_1.pack()
        selec_1= tk.Button(ventana,text='Usuario Administrador',padx=47,pady=10,command=usuario_admi)
        selec_1.pack()
        selec_2 = tk.Button(ventana, text='Usuario Normal', padx=65, pady=10, command = usuario_normal )
        selec_2.pack()
        def close_window():
            """Destruye un ventana"""
            ventana.destroy()
        salida = tk.Button(ventana, text='Salida', padx=40, pady=10,bg='red',command=close_window)
        salida.pack()
        ventana.mainloop()

    def ventana():
      """funcion que abre la ventana inicial donde da opcion de 'iniciar cesion' o 'crear un usuario'
        no recibe no retorna"""
      ventana=tk.Tk()
      ventana.title('Inventario')
      ventana.geometry('400x300')
      titulo=tk.Label(ventana, text='Inicio',font=('Arial bold',14))
      titulo.pack()
      n_usuario=tk.Button(ventana,text='Nuevo usuario',padx=40,pady=10,command=selec_nuevo_usuario)
      n_usuario.pack(side = tk.TOP, expand = True)
      usuario = tk.Button(ventana, text='Iniciar sesión', padx=40, pady=10, command=iniciar_cesion )
      usuario.pack(side = tk.TOP, expand = True)
      ventana.mainloop()

    ventana()
