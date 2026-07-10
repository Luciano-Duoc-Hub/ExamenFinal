dicjuegos = {}
dicinventario = {}

def leer_opcion():
    opci = int(input("ingrese una opción"))
    try:
        if opci in range(1,7):
            return opci
    except ValueError:
        print("Debe seleccionar una opción válida")

def stock_plataforma(plataforma):
    if plataforma in "PS5, PC, XBOX, SWITCH":
        for codg, plats in dicjuegos.items():
            if plataforma in plats:
                for stock in dicinventario[codg][1]:
                    stock = stock + 0
                    print("Esta es la cantidad de juegos disponibles en",plataforma,":",stock)                
    else:
        print("plataforma no encontrada")

def buscar_codigo(codigo):
    if codigo in dicinventario:
        return True
    else:
        return False

def actualizar_precio(codigo, nuevo_precio):
    if buscar_codigo == True:
        dicinventario[codigo][0] = nuevo_precio
        print("Precio actualizado")
        return True
    else:
        print("El código no existe")
        return False   

def codigo_juego(codigo):
    if "qwertyuiopasdfghjklñzxcvbnm1234567890QWERTYUIOPASDFGHJKLÑZXCVBNM" not in codigo or codigo in dicjuegos:
        print("Codigo no valido")
        return False 
    else:
        return True

def titulo_juego(titulo):
    if "qwertyuiopasdfghjklñzxcvbnm1234567890QWERTYUIOPASDFGHJKLÑZXCVBNM" not in titulo or titulo in dicjuegos:
        print("Titulo no valido")
        return False 
    else:
        return True

def plataforma_juego(plataforma):
    if plataforma is "PS5" or plataforma is "XBOX" or plataforma is "PC" or plataforma is "SWITCH":
        return True
    else:
        print("Plataforma No valida")
        return False

def genero(genero):
    if "qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM" not in genero:
        print("no valido")
        return False
    else:
        return True
    
def clasificacion(clas):
    if clas is "E" or clas is "e" or clas is "T" or clas is "t" or clas is "M" or clas is "m":
        return True
    else:
        print("No valido")
        return False

def precio_base(precio):
    if precio is int and precio > 0:
        return True
    else: 
        print("no valido")
        return False

def stock_base(stockbase):
    if stockbase is int and stockbase >= 0:
        return True
    else:
        print("no valido")
        return False
    

while True:
    print("""""""""
    ========== MENÚ PRINCIPAL ==========
    1. Stock por plataforma
    2. Juegos
    3. Actualizar precio de juego
    4. Agregar juego
    5. Salir
    ===================================== """)
    opcion = leer_opcion
    if opcion == 1:
        nplat = input("Ingrese nombre de una plataforma:").upper()
        stock_plataforma(nplat)

    elif opcion == 2:
        for games in dicjuegos:
            print(games)

    elif opcion == 3:
        while True:

            while True:
                codig = input("Ingrese codigo del juego:")
                nprec = int(input("Ingrese nuevo precio:"))
                buscar_codigo(codig)
                actualizar_precio(codig, nprec)
                break
            op = input("¿Desea actualizar otro precio (s/n)?")
            try:
                if op == "s" or op == "S":
                    True
                elif op == "n" or op == "N":
                    False
            except:
                print("opcion invalida")
                
    elif opcion == 4:
        while True:
            codex = input("Ingrese codigo del juego:")
            codigo_juego(codex)
            titulo = input("titulo juego:")
            titulo_juego(titulo)
            plataforma = input("plataforma:")
            plataforma_juego(plataforma)
            generow = input("genero:")
            genero(generow)
            clasi = input("clasificacion(E,T o M):")
            clasificacion(clasi)
            preciss = input("precio)")
            precio_base(preciss)
            stock_baadasd = input("stock")
            stock_base(stock_baadasd)
            
            dicjuegos["juego"] = [codex, titulo, plataforma, generow, clasi]
            dicinventario["codigo"] = [codex, preciss, stock_baadasd]
    
    elif opcion == 5:
        break
print("Programa finalizado.")
