import tkinter as tk
import webbrowser
from  tkinter import ttk
from tkinter import messagebox


def click_presiona():
    """
      Muestra un mensaje en la pantalla, dando la bienvenida al programa y mostrando los nombres de los creadores.

      """
    messagebox.showinfo("Bienvenido", """Este programa ha sido codificado en lenguaje phyton
                                    Por los estudiantes: 
                                    
                                    -Yeison Rojas
                                    -Alan Escobar
                                    -Manuel Vasquez""")
def unal_logo():
    """
      Envia al usuario a la pagina web oficial de la Univesidad Nacional de Colombia)

      """
    new=2
    url="https://unal.edu.co/"
    webbrowser.open(url, new=new)

def ventana():
    """
      Es donde se crea una ventana con la libreria Tkinter, la cual provee de una interfaz grafica al programa

      """
    ventana=tk.Tk()
    ventana.title('-----_____________| Mi Tienda |______________-----')
    ventana.geometry('600x400')


    tab_control = ttk.Notebook(ventana)
    tab1 = ttk.Frame(tab_control)
    tab2 = ttk.Frame(tab_control)
    tab3 = ttk.Frame(tab_control)
    tab4 = ttk.Frame(tab_control)
    tab_control.add(tab1, text='Inicio')
    tab_control.add(tab2, text='Agregar Productos' )
    tab_control.add(tab3, text= 'Buscar Producto')
    tab_control.add(tab4, text= 'Lista de Productos')
    tab_control.pack(expand=1, fill='both')
#Comienza primera pestaña

    etiqueta_tab1= ttk.Label(tab1, text=''' Bienvenido a
    Mi tienda''', font=('Arial black', 25))
    etiqueta_tab1.place(x=340, y= 5)
    etiqueta2_tab1 = ttk.Label(tab1, text='''    Este es un programa capaz de almacenar información sobre el inventario 
    de una tienda, siendo de utilidad para llevar un conteo de insumos 
    de manera rigurosa y para tener un orden a la hora de comprar
    y vender productos, siendo estos problemas muy comunes en pequeñas 
    tiendas en donde sus inventarios varían constantemente.''', font=('Verdana', 10))
    etiqueta2_tab1.place(x=10, y=180)

    boton_nombre = tk.Button(tab1, text='!PRESIONA!', command=click_presiona, font=('Arial', 14), bg='white', fg='black')
    boton_nombre.place(x=400, y= 120)

    imagen= tk.PhotoImage(file='logo.png')
    fondo= ttk.Button(tab1, image= imagen, command=unal_logo).place(x=10, y=5)


#comienza segunda pestaña
    fondo_azul = tk.PhotoImage(file="fondo.png")
    tk.Label(tab2, image=fondo_azul).place(x=0, y=0, relwidth=1, relheight=1)

    producto = tk.Label(tab2, text="Producto: ", font=('Arial', 10), bg="LightSkyBlue2")
    producto.place(x=180, y=40)

    enter_producto = tk.Entry(tab2, width= 23)
    enter_producto.place(x=260, y=40)

    precio = tk.Label(tab2, text="Precio: ", font=('Arial', 10), bg="LightSkyBlue2")
    precio.place(x=180, y=70)

    enter_precio = tk.Entry(tab2, width= 23)
    enter_precio.place(x=260, y=70)

    cantidad = tk.Label(tab2, text="Cantidad: ", font=('Arial', 10), bg="LightSkyBlue2")
    cantidad.place(x=180, y=100)

    enter_cantidad = tk.Entry(tab2, width= 23)
    enter_cantidad.place(x=260, y=100)

    def se_guardo_producto():
        """
          Muestra un mensaje al usuario indicandole que el mensaje ha sido guardado

          """
        messagebox.showinfo("Guardado", "El producto se guardó satisfactoriamente")

    def agregar_producto():
        """
          Abre el archivo .txt y escribe en el las entradas de tipo tk.Entry

          """
        etiqueta_nombre = enter_producto.get()
        etiqueta_precio = enter_precio.get()
        etiqueta_cantidad = enter_cantidad.get()
        archivo = open("archivo.txt", "a")
        archivo.write(f"{etiqueta_nombre} - {etiqueta_precio} - {etiqueta_cantidad} \n")
        archivo.close()
        se_guardo_producto()

    boton = tk.Button(tab2, text="Listo", command=agregar_producto)
    boton.place(x=300, y=125)

# Comienza tercera pestaña

    tk.Label(tab3, image=fondo_azul).place(x=0, y=0, relwidth=1, relheight=1)

    etiqueta_insertar = tk.Label(tab3, text='Nombre del Producto : ', font=('Arial', 10), bg="LightSkyBlue2").place(x=150, y=40)

    entrada = tk.Entry(tab3, width='20')
    entrada.place(x=290, y =40)

    resultado_precio= tk.Label(tab3, text='Precio : ', bg="LightSkyBlue2")
    resultado_precio.place(x=230, y=70)

    resultado_cantidad= tk.Label(tab3, text='Cantidad : ', bg="LightSkyBlue2")
    resultado_cantidad.place(x=230, y=100)

    boton_buscar= tk.Button(tab3, text='Buscar', command=lambda: configura(resultado_precio, resultado_cantidad))
    boton_buscar.place(x=260, y=130)

    def configura(precio, cantidad):
        """
          Busca en el archivo .txt la palabra ingresada en el tipo tk.Entry, y configura las palabras en la misma linea
          en la etiqueta correspondiente

          :param tk.Label precio : es la etiqueta en donde se configurara el precio del producto
          :param tk.Label cantidad: es la etiqueta en donde se configurara la cantidad de productos que posee
          """
        palabra = entrada.get()

        linea_similar = []
        with open('archivo.txt') as lineas:
            for linea in lineas:
                if palabra in linea:
                    linea_similar.append(linea)
                    valor= True
                    break
                else:
                    valor = False
            if valor == False:
                messagebox.showerror('Error', 'No se encontró el producto, intente con otro nombre')
        linea_elegida = linea_similar[0]
        linea_elegida = linea_elegida.split(" - ")

        precio.configure(text='Precio : ' + str(linea_elegida[1]))
        cantidad.configure(text='Cantidad : ' + str(linea_elegida[2]))

#Comienza cuarta pestaña
    lista_productos = tk.Listbox(tab4, width=30, height=50, bg='LightSkyBlue2',selectbackground="#00aa00",
                                 borderwidth= 4,
                                 font=('Arial', 11))
    with open('archivo.txt') as lineas:
        contador = 0
        for linea in lineas:
            lista_productos.insert(contador, linea)
            contador += 1
    lista_productos.place(x=140, y=80)
    texto_recordatorio= tk.Label(tab4, text='Nombre del Producto - Precio unitario - Cantidad que posee ',
                       font=('Arial', 9))
    texto_recordatorio.place(x=140, y=60)

    texto_reinicie= tk.Label(tab4, text='Si agregó un producto y no se encuentra en la lista,'
                                  ' pruebe a reiniciar la app', font=('Arial', 9), bg='indianRed1')
    texto_reinicie.place(x=10, y=10)

    def elimina():
        """
          Elimina de la lista el producto seleccionado, sin mebargo estos acmbios solo surgen
          efecto en la ventana abierta

          """
        entrada = lista_productos.curselection()
        lista_productos.delete(entrada)

    boton_eliminar = tk.Button(tab4, text='Eliminar', command=elimina)
    boton_eliminar.place(x=400, y=90)

    ventana.mainloop()

def main():
    """
      es la que función que  inicia el programa

      """
    ventana()

main()
