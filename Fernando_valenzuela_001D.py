productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}

stock_HP = 200
stock_lenovo = 200
stock_Asus = 200


def validar_texto(mensaje:str):
    while True:
        texto = input(mensaje)
        if len(texto.strip()) == 0:
            continue
        else:
            return texto
        
def validar_num_entero_pos(mensaje_i:str):
    while True:
        try:
            numero = int(input(mensaje_i))
            if numero <= 0:
                print("NO SE PERMITEN NEGATIVOS O CEROS")
                continue
            else:
                return numero
        except ValueError:
            print("SOLO INGRESAR NUMEROS ENTERO")
            continue

def stock_marca(nombre_pro:str):
    for i in productos:
        if productos [i][0].lower() == nombre_pro.lower:
            print("PRODUCTO ENCONTRADO")
            marca_encontra = productos[i]
            marca_encontra.insert(0,i)
            return marca_encontra
        


def busqueda_precio(p_min,p_max:int):
    for i in stock:
        if stock[i][0] >= p_min and stock[1][9] <= p_max:
            print (stock[i])






def actualizar_precio(modelo:str , p:int):
    producto_encontrado = busqueda_precio(modelo)
    if producto_encontrado != None:
        print(producto_encontrado)
        for i in stock:
            if i.upper() == producto_encontrado[0].upper():
                stock[i][0] = p
    else:
        print("EL PRODUCTO NO ESTA")





        

            
while True:
        print ("   ***MENU PRINCIPAL***")

        print ("[1] - STOCK MARCA ")
        print ("[2] - BUSQUEDA POR PRECIO")
        print ("[3] - ACTUALIZAR PRECIO")
        print ("[4] - SALIR")

        try:
            opc =int(input("INGRESE UNA OPCION: "))
        except ValueError:
            print("INGRESE UNA OPCION VALIDA DEL 1-4")

        if opc == 1:
            stock_marc = validar_texto("QUE MARCA DESEA CONSULTAR: ")
            print(stock)



        elif opc == 2:
            p_min = validar_num_entero_pos("INGRESE PRECIO MIN: ")
            p_max = validar_num_entero_pos("INGRESE PRECIO MAX: ")

            busqueda_precio(p_min,p_max)




        elif opc == 3:
            nombre_marca = validar_texto("INGRESE EL NNUMBRE DE LA MARCA: ")
            nuv_precio = validar_num_entero_pos("INGRESE EL NUEVO PRECIO: ")

            actualizar_precio(nombre_marca,nuv_precio)




        elif opc == 4:
            print("PROGRAMA FINALIZADO")
            break
        else:
                print("PROGRAMA FINALIZADO")


  

        







































    