import tkinter as tk
import webbrowser
from  tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from bs4 import BeautifulSoup
from urllib.request import urlopen


def click_presiona():
    """
      Muestra un mensaje en la pantalla, dando la bienvenida al programa y mostrando los nombres de los creadores.

      """
    messagebox.showinfo("Bienvenido", """Este programa ha sido codificado en lenguaje phyton
                                    Por los estudiantes: 
                                    
                                    -Yeison Rojas
                                    -Manuel Vasquez""")
def unal_logo():
    """
      Envia al usuario a la pagina web oficial de la Univesidad Nacional de Colombia)

      """
    new=2
    url="https://unal.edu.co/"
    webbrowser.open(url, new=new)

def ventana_todo():
    """
      Es donde se crea una ventana con la libreria Tkinter, la cual provee de una interfaz grafica al programa

      """
    ventana1=tk.Tk()
    ventana1.title('_____________| Mi Tienda |______________')
    ventana1.geometry('600x420')
    ventana1.config(background="green")


    tab_control = ttk.Notebook(ventana1)
    tab1 = ttk.Frame(tab_control)
    tab2 = ttk.Frame(tab_control)
    tab3 = ttk.Frame(tab_control)
    tab4 = ttk.Frame(tab_control)
    tab5 = ttk.Frame(tab_control)
    tab6 = ttk.Frame(tab_control)
    tab7 = ttk.Frame(tab_control)
    tab_control.add(tab1, text= 'Inicio')
    tab_control.add(tab2, text= 'Agregar Productos' )
    tab_control.add(tab3, text= 'Buscar Producto')
    tab_control.add(tab4, text= 'Lista de Productos')
    tab_control.add(tab5, text= 'Venta de Productos')
    tab_control.add(tab6, text= 'Historial de ventas')
    tab_control.add(tab7, text='Precios Metro')
    tab_control.pack(expand=1, fill='both')
#Comienza primera pestaña

    etiqueta_tab1= ttk.Label(tab1, text=''' Bienvenido a
    "Mi Tienda"''', font=('Adobe Fan Heiti Std B', 25, "bold"))
    etiqueta_tab1.place(x=360, y= 10)
    etiqueta2_tab1 = ttk.Label(tab1, text='''    Este es un programa capaz de almacenar información sobre el inventario 
    de una tienda, siendo de utilidad para llevar un conteo de insumos 
    de manera rigurosa y para tener un orden a la hora de comprar
    y vender productos, siendo estos problemas muy comunes en pequeñas 
    tiendas en donde sus inventarios varían constantemente.''', font=('Adobe Fan Heiti Std B', 12))
    etiqueta2_tab1.place(x=10, y=180)

    botonxd= tk.PhotoImage(file= 'button.png')
    boton_nombre = tk.Button(tab1, image= botonxd, command=click_presiona, bg='white', fg='black')
    boton_nombre.place(x=365, y= 100)

    imagen= tk.PhotoImage(file='logo.png')
    fondo= ttk.Button(tab1, image= imagen, command=unal_logo).place(x=10, y=5)


#comienza segunda pestaña
    fondo_azul = tk.PhotoImage(file="fondo.png")
    tk.Label(tab2, image=fondo_azul).place(x=0, y=0, relwidth=1, relheight=1)

    producto = tk.Label(tab2, text="Producto: ", font=('Adobe Fan Heiti Std B',10), bg="LightSkyBlue2")
    producto.place(x=180, y=40)

    enter_producto = tk.Entry(tab2, width= 23)
    enter_producto.place(x=260, y=40)

    precio = tk.Label(tab2, text="Precio: ", font=('Adobe Fan Heiti Std B',10), bg="LightSkyBlue2")
    precio.place(x=180, y=70)

    enter_precio = tk.Entry(tab2, width= 23)
    enter_precio.place(x=260, y=70)

    cantidad = tk.Label(tab2, text="Cantidad: ", font=('Adobe Fan Heiti Std B',10), bg="LightSkyBlue2")
    cantidad.place(x=180, y=100)

    enter_cantidad = tk.Entry(tab2, width= 23)
    enter_cantidad.place(x=260, y=100)

    def se_guardo_producto():
        """
          Muestra un mensaje al usuario indicandole que el producto ha sido guardado

          """
        messagebox.showinfo("Guardado", "El producto se guardó satisfactoriamente")
    def no_guardo_producto():
        """
                  Muestra un mensaje al usuario indicandole que su entrada tiene un error

                  """
        messagebox.showerror("No se pudo guardar", "El producto no se guardo dado que sus entradas en precio o cantidad no son numericas"
                                                   " o son valores negativos, modifiquelas e intentelo de nuevo")
    def agregar_producto():
        """
          Abre el archivo .txt y escribe en el las entradas de tipo tk.Entry

          """
        etiqueta_nombre = enter_producto.get()
        etiqueta_precio = enter_precio.get()
        etiqueta_cantidad = enter_cantidad.get()
        lista=[]
        with open('archivo.txt') as lineas:
            for linea in lineas:
                final= linea.split(" - ")
                lista.append(final[0])
        if etiqueta_nombre in lista:
            messagebox.showerror("No se pudo guardar",
                                 "El producto no se guardo dado que ya se encuentra dentro del inventario")
            return

        if etiqueta_nombre == "" or etiqueta_precio =="" or etiqueta_cantidad == "":
            messagebox.showerror("No se guardo", "Algunas entradas estan vacias, modifiquelas e intentelo de nuevo")
            return
        valor1= True
        for caracter1 in etiqueta_precio:
            if caracter1 not in "1234567890":
                valor1= False
                break
        valor2= True
        for caracter2 in etiqueta_cantidad:
            if caracter2 not in "1234567890":
                valor2= False
                break
        if valor1 == True and valor2 == True:
            archivo = open("archivo.txt", "a")
            archivo.write(f'{etiqueta_nombre} - {etiqueta_precio} - {etiqueta_cantidad}\n')
            archivo.close()
            se_guardo_producto()
        else:
            no_guardo_producto()
    boton = tk.Button(tab2, text="Listo", command=agregar_producto, font=('Adobe Fan Heiti Std B',9), bg="purple",
                             fg="white")
    boton.place(x=300, y=125)

# Comienza tercera pestaña
    fondo_azul3 = tk.PhotoImage(file="fondo.png")
    tk.Label(tab3, image=fondo_azul3).place(x=0, y=0, relwidth=1, relheight=1)

    def configura(palabra):
        """
          Busca en el archivo .txt la palabra ingresada en el tipo tk.Entry, y configura las palabras similares en una lista treeview
          """
        linea_similar = []
        with open('archivo.txt') as lineas:
            for linea in lineas:
                if palabra in linea:
                    linea_similar.append(linea)
        if linea_similar==[]:
            messagebox.showerror('Error', 'No se encontró el producto, puede que el producto haya sido guardado con mayusculas,'
                                          ' sin embargo puede revisar en la pestaña "Lista de productos"')
            return
        linea_elegida = linea_similar[0]
        linea_elegida = linea_elegida.split(" - ")
        tree = ttk.Treeview(tab3, columns=('Nombre', 'Precio'))

        tree.heading('#0', text='Producto')
        tree.heading('#1', text='|  Precio  |')
        tree.heading('#2', text=' Cantidad  |')

        tree.column('#0', stretch=tk.YES)
        tree.column('#1', width=77, stretch=tk.YES)
        tree.column('#2', width=72, stretch=tk.YES)
        style = ttk.Style()
        style.configure(".", font=('Adobe Fan Heiti Std B', 10), foreground="black")
        style.configure("Tree", foreground='red')
        style.configure("Tree.Heading", font=('Adobe Fan Heiti Std B', 10), foreground='green')

        tree.place(x=90, y=100)

        for y in linea_similar:
            y=y.split(" - ")
            tree.insert('', 'end', text=f"{y[0]}",
                        values=(y[1], y[2]))


    etiqueta_insertar = tk.Label(tab3, text='Digite palabra clave del producto : ', font=('Adobe Fan Heiti Std B',10), bg="LightSkyBlue2").place(
        x=83, y=40)

    entrada = tk.Entry(tab3, width='17')
    entrada.place(x=290, y=40)

    boton_buscar = tk.Button(tab3, text='Buscar', command=lambda:configura(entrada.get()),
                             font=('Adobe Fan Heiti Std B',9), bg="purple",
                             fg="white")
    boton_buscar.place(x=410, y=40)

# Comienza cuarta pestaña
    fondo_azul4 = tk.PhotoImage(file="fondo.png")
    tk.Label(tab4, image=fondo_azul4).place(x=0, y=0, relwidth=1, relheight=1)
    def actualizar_lista():
        """
        Actualiza la lista de productos si ha agregado nuevos

        """
        lista_productos = ttk.Treeview(tab4, columns=('Nombre', 'Precio'))
        lista_productos.heading('#0', text='Producto')
        lista_productos.heading('#1', text='|  Precio  |')
        lista_productos.heading('#2', text=' Cantidad ')

        lista_productos.column('#0', stretch=tk.YES)
        lista_productos.column('#1', width=77, stretch=tk.YES)
        lista_productos.column('#2', width=72, stretch=tk.YES)

        lista_productos.place(x=90, y=100)

        archivo= open('archivo.txt', 'r')
        arch1= archivo.read()
        archivo.close()
        if arch1 != "":
            with open('archivo.txt') as lineas:
                cont=1
                for linea in lineas:
                    linea=linea.split(" - ")
                    lista_productos.insert('', 'end',id=cont, text=f"{linea[0]}",
                                values=(linea[1], linea[2]))
                    cont+=1
        def elimina():
            """
              Elimina de la lista el producto seleccionado

              """
            row_id = int (lista_productos.focus())
            print(row_id)
            lista_productos.delete(row_id)
            lista_productos.destroy()
            with open('archivo.txt') as lineas:
                cont=1
                final=""
                for linea in lineas:
                    if cont != row_id:
                        final+=linea
                    else:
                        print(linea)
                    cont+=1
                print (final)
            texto= open("archivo.txt","w")
            texto.write(final)
            texto.close()
            actualizar_lista()

        def modificar_producto():
            """
            Crea una ventana para la modificación del producto seleccionado

            """
            mod = tk.Tk()
            mod.title('Modificar producto')
            mod.geometry('275x250')
            mod.config(background="LightSkyBlue2")
            rotulo_nombre = tk.Label(mod, text="Producto", font=('Adobe Fan Heiti Std B',9), bg="LightSkyBlue2")
            rotulo_nombre.place(x= 20, y=20)
            rotulo_precio = tk.Label(mod, text="Precio", font=('Adobe Fan Heiti Std B',9), bg="LightSkyBlue2")
            rotulo_precio.place(x=20, y=80)
            rotulo_cantidad = tk.Label(mod, text="Cantidad", font=('Adobe Fan Heiti Std B',9), bg="LightSkyBlue2")
            rotulo_cantidad.place(x=20, y=140)
            modname = tk.Entry(mod)
            modname.place(x=80, y=20)
            modprecio= tk.Entry(mod)
            modprecio.place(x= 80, y=80)
            modcantidad = tk.Entry(mod)
            modcantidad.place(x=80, y=140)
            def mod_producto():
                """
                Modifica el prducto seleccionado en el archivo.txt
                """
                try:
                    num= int (lista_productos.focus())
                except:
                    messagebox.showerror("No selecciono un producto", "Debes seleccionar un producto "
                                                                      "para que se pueda modificar")
                    mod.destroy()
                try:
                    pr= int(modprecio.get())
                    ca= int(modcantidad.get())
                except:
                    messagebox.showerror("Valores no validos", "Debes colocar valores numericos en precio y cantidad"
                                                                      " para que se pueda modificar")
                    return
                with open('archivo.txt') as lineas:
                    cont=1
                    final=""
                    for linea in lineas:
                        if cont != num:
                            final+=linea
                        else:
                            final+=f"{modname.get()} - {modprecio.get()} - {modcantidad.get()}\n"
                        cont+=1
                    print (final)
                texto= open("archivo.txt","w")
                texto.write(final)
                texto.close()
                actualizar_lista()
                messagebox.showinfo("Cambiado con exito", "Se modifico el producto")
                mod.destroy()
            boton_hecho= tk.Button(mod, text= "Realizar cambio", command=mod_producto,
                             font=('Adobe Fan Heiti Std B',9), bg="purple",
                             fg="white")
            boton_hecho.place(x=100, y=180)
            mod.mainloop()


        boton_modificar = tk.Button(tab4, text='Modificar', command=modificar_producto,
                                    font=('Adobe Fan Heiti Std B', 9),
                                    bg="purple",
                                    fg="white")
        boton_modificar.place(x=450, y=200)

        boton_eliminar = tk.Button(tab4, text='Eliminar', command= elimina, font=('Adobe Fan Heiti Std B', 9),
                                     bg="purple",
                                     fg="white")
        boton_eliminar.place(x=450, y=300)


    boton_actualizar = tk.Button(tab4, text='Actualizar', command=actualizar_lista, font=('Adobe Fan Heiti Std B',9), bg="purple",
                             fg="white")
    boton_actualizar.place(x=450, y=100)

    actualizar_lista()

# comienza quinta pestaña:
    def crear_tabla():
        """
        Crea una tabla o lista de tipo ttk.treeview
        :return class ttk.treeview tree: una tabla para que se coloquen valores
        """
        tree = ttk.Treeview(tab5, columns=('Nombre', 'Precio'))
        tree.heading('#0', text='Producto')
        tree.heading('#1', text='|Precio Total|')
        tree.heading('#2', text=' Cantidad ')
        
        tree.column('#0', stretch=tk.YES)
        tree.column('#1', width=80, stretch=tk.YES)
        tree.column('#2', width=75, stretch=tk.YES)
        style = ttk.Style()
        style.configure(".", font=('Adobe Fan Heiti Std B', 9), foreground="black")
        style.configure("Tree", foreground='red')
        style.configure("Tree.Heading", font=('Adobe Fan Heiti Std B', 10), foreground='green')
        tree.place(x=90, y=100)

        return tree
    fondo_azul5 = tk.PhotoImage(file="fondo.png")
    tk.Label(tab5, image=fondo_azul5).place(x=0, y=0, relwidth=1, relheight=1)

    def combo_productos(k=False):
        """
        Abre el archivo txt y toma una lista de los nombres de lso productos
        :param class boolean k: le dice que valor tiene que devolver
        :return: class dict lista: diccionario con todos los datos del txt
        :return: class list nombres: lista de nombres del producto

        """
        lista = {}
        nombres = []
        with open('archivo.txt') as lineas:
            for linea in lineas:
                final = linea.split(" - ")
                nombres.append(final[0])
                lista[final[0]] = final[1]
        if k == True:
            return nombres
        else:
            return lista

    combo = ttk.Combobox(tab5, font=('Adobe Fan Heiti Std B', 9))
    k= True
    combo['values'] = combo_productos(k)
    combo.current()
    combo.place(x=85, y=50)

    suma={}
    texto_producto= tk.Label(tab5, text="Elija el producto: ", font = ('Adobe Fan Heiti Std B', 9),
                             bg="LightSkyBlue2")
    texto_producto.place(x=85, y= 25)
    texto_cantidad = tk.Label(tab5, text="Escriba la cantidad: ", font=('Adobe Fan Heiti Std B', 9),
                              bg="LightSkyBlue2")
    texto_cantidad.place(x=250, y=25)
    lista_productos=(crear_tabla())
    boton_agregar = tk.Button(tab5, command=lambda: sumar(combo.get(), combo_productos()[combo.get()], cantidad.get(), crear_tabla()),
                      text='Agregar a la venta', font = ('Adobe Fan Heiti Std B', 9),
                      bg="purple",
                      fg="white")

    boton_agregar.place(x=360, y=49)
    cantidad = tk.Entry(tab5, width=17)
    cantidad.place(x=250, y=50)


    texto_total = tk.Label(tab5, text="Total: ", font=('Adobe Fan Heiti Std B', 11),
                              bg="LightSkyBlue2")
    texto_total.place(x=320, y=330)

    boton_finalizar= tk.Button(tab5, command= lambda : agregar_venta(suma),
                      text='Finalizar venta', font = ('Adobe Fan Heiti Std B', 10),
                      bg="purple",
                      fg="white")
    boton_finalizar.place(x= 320,y=355)
    def reinicio_suma():
        """
        Reinicia el diccionario en donde se estan guardando todos los productos que se van a vender
        """
        key_list = list(suma.keys())
        for k in key_list:
            del (suma[k])
        print(suma)
        crear_tabla()
        h= True
        combo['values']=combo_productos(h)


    boton_reiniciar = tk.Button(tab5, command=reinicio_suma,
                                text='Reiniciar la venta', font=('Adobe Fan Heiti Std B', 10),
                                bg="purple",
                                fg="white")
    boton_reiniciar.place(x=200, y=355)

    def sumar(nombre, pos, cantidad, tree):
        """
        suma a la tabla los valores del diccionario suma

        :param class str nombre: nombre del producto
        :param class str pos: precio del producto
        :param class str cantidad: cantidad de la venta
        :param class ttk.Treview tree: tabla para poner todos los datos
        :return: None
        """
        if cantidad == '':
            cantidad = 1
        try:
            cantidad= int(cantidad)
        except:
            messagebox.showerror("Error", "Digíte solo números en el espacio dedicado para cantidad")
            return
        suma[nombre] = [(int(pos) * int(cantidad)), cantidad]
        print(suma)

        for x in suma:
            tree.insert('', 'end', text=f"{x}",
                        values=(suma[x][0], suma[x][1]))
        cuenta_total(suma)


    def agregar_venta(ventafinal):
        """
        abre el archivo txt que contiene el historial y agrega la reciente venta

        :param ventafinal: Diccionario que contiene los datos de la venta que se esta haciendo
        :return: None
        """
        tiempo = str(datetime.now())
        historial=""
        for i in ventafinal:
            historial+=f"{i} - {ventafinal[i][0]} - {ventafinal[i][1]} - {tiempo}\n"
        ventas= open("ventas.txt", "a")
        ventas.write(historial)
        ventas.close()
        with open('archivo.txt') as descuento:
            texto=""
            for linea in descuento:
                linea= linea.split(" - ")
                if linea[0] in ventafinal:
                    new= int(linea[2])- int (ventafinal[linea[0]][1])
                    if new <= 0:
                        messagebox.showinfo("Producto agotado", f"El producto {linea[0]} ya está agotado por lo tanto se ha colocado en valores negativos en el inventario")
                    texto+=f"{linea[0]} - {linea[1]} - {int(linea[2])- int (ventafinal[linea[0]][1])}"
                    texto+="\n"
                else:
                    texto+=f"{linea[0]} - {linea[1]} - {linea[2]}"
            texto= texto.strip("\n")
            texto+="\n"
        escribir= open("archivo.txt", "w")
        escribir.write(texto)
        escribir.close
        sexta_pestaña()
        messagebox.showinfo("Guardado en el historial", "La venta ha finalizado y se ha guardado el registro en el historial de ventas")
    def cuenta_total(diccionario):
        """Hace la suma de la venta que se esta haciendo
        :param class dict diccionario: dict con todos los datos de la venta
        """
        cuenta=0
        for num in diccionario:
            total= float (diccionario[num][0])
            cuenta+=total

        final = tk.Label(tab5, text=f"$ {cuenta}  ", font=('Adobe Fan Heiti Std B', 11),
                               bg="LightSkyBlue2")
        final.place(x=370, y=330)

# comienza 6 pestaña
    fondo_azul6 = tk.PhotoImage(file="fondo.png")
    tk.Label(tab6, image=fondo_azul6).place(x=0, y=0, relwidth=1, relheight=1)
    def sexta_pestaña():
        """
        Crea la sexta pestaña del programa la cual es la de el historial de ventas
        y configura una tabla con el historial

        :return: None
        """
        historial = ttk.Treeview(tab6, columns=('Nombre', 'Precio', 'fecha'))
        historial.heading('#0', text='Producto')
        historial.heading('#1', text='|Precio Total|')
        historial.heading('#2', text='| Cantidad |')
        historial.heading('#3', text='| Fecha y hora')

        historial.column('#0', stretch=tk.YES)
        historial.column('#1', width=80, stretch=tk.YES)
        historial.column('#2', width=80, stretch=tk.YES)
        historial.column('#3', stretch=tk.YES )
        historial.place(x=20, y=50)

        with open('ventas.txt') as lineas:
            final=''
            for linea in lineas:
                final = linea.split(" - ")
                historial.insert('', 'end', text=f"{final[0]}",
                        values=(final[1], final[2], final[3][:16]))
    sexta_pestaña()
# comienza septima pestaña
    def webs(lista):
        """
            Crea la interfaz grafica del web scraping junto con varios widgets
            :param class dict lista: un diccionario con los nombres de las paginas y su respectivas url.
            """
        lista_direcciones = [x for x in lista]
        etiqueta = tk.Label(tab7, text="Escoja el producto de interes : ", font=('Adobe Fan Heiti Std B', 13))
        etiqueta.place(x=30, y=30)
        productos = ttk.Combobox()
        productos = ttk.Combobox(tab7)
        productos['values'] = lista_direcciones
        productos.current()
        productos.place(x=280, y=30)
        boton = tk.Button(tab7, text="Buscar", command=lambda: imprimir_datos(lista[productos.get()]),
                          font=('Adobe Fan Heiti Std B', 9), bg="purple",
                          fg="white")
        boton.place(x=430, y=28)

    def tabla(diccionario):
        """Crea un tabla con el widget treeview de tkinter en donde se colocaran los datos extraidos de la web
           :param class dict diccionario:  un diccionario con los nombres de las paginas y su respectivas url
            """
        tree = ttk.Treeview(tab7, columns=('Nombre', 'Precio'))

        tree.heading('#0', text='#')
        tree.heading('#1', text='|  Producto  |')
        tree.heading('#2', text='|   Precio  |')

        tree.column('#0', width=50, stretch=tk.YES)
        tree.column('#1', width=280, stretch=tk.YES)
        tree.column('#2', width=110, stretch=tk.YES)

        tree.place(x=90, y=100)
        cont = 1
        for producto in diccionario:
            tree.insert('', 'end', text=f"{cont}",
                        values=(producto, diccionario[producto]))
            cont += 1

    def imprimir_datos(url):
        """
        busca los datos en la web de la opcion que el usuario haya escogido

        :param class str url: es la url de donde se sacaran los datos
        :return: None
        """
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        texto = soup.get_text()
        lineas = [linea for linea in texto.split('\n') if linea != '']
        precios = {}
        for x in range(len(lineas)):
            if lineas[x] == "0" and lineas[x + 1] == "0":
                precios[lineas[x + 2]] = lineas[x + 5]
                continue
            if "%" in lineas[x] and "$" in lineas[x + 1]:
                precios[lineas[x + 2]] = lineas[x + 6]
        tabla(precios)
        print(len(precios))

    def direcciones():
        """
        Provee toda la información de las urls para que se pueda hacer el raspado web

        """
        todos = {
            'Endulzantes': "https://www.tiendasmetro.co/supermercado/despensa/azucar-endulzantes-y-panelas/500?PS=18",
            'Avenas': "https://www.tiendasmetro.co/supermercado/despensa/avenas/500?PS=18",
            'Harinas': "https://www.tiendasmetro.co/supermercado/despensa/harinas/500?PS=18",
            'Chocolates y cafés': "https://www.tiendasmetro.co/supermercado/despensa/chocolate-y-cafe/500?PS=44",
            'Cereales': "https://www.tiendasmetro.co/supermercado/despensa/cereales-y-granolas/500?PS=18",
            'Pastas': "https://www.tiendasmetro.co/supermercado/despensa/pastas/500?PS=44",
            'Arroz y granos': "https://www.tiendasmetro.co/supermercado/despensa/arroz-y-granos/500?PS=44"}

        webs(todos)
    direcciones()
    ventana1.mainloop()
def log():
    f= tk.Tk()
    g= tk.Button(f, text="inicio", command= lambda:ventana_todo() )
    g.place(x= 20, y=20)
    f.mainloop()
def main():
    """
      es la que función que  inicia el programa
      :return None

      """
    ventana_todo()

main()
