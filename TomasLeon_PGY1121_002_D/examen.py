import os
os.system("cls")

vectorUbi = []
vectorAsis = []
fila = 0
columna = 0
n = 1
ocupado = "X"
contPlat = 0
contGold = 0
contSil = 0

menu = """
1. Comprar entradas
2. Mostrar ubicaciones disponible
3. Ver listado asistentes
4. Mostrar ganancias totales
5. Salir
Ingrese opcion: 
"""

preciosEnt = """
Precio entradas:
Platinum 120.000 | Asientos 1 al 20
Gold 80.0000 | Asientos del 21 al 50
Silver 50.000 | Asientos del 51 al 100
"""

for i in range(10):
        vectorUbi.append([])

for i in range(10):
        for j in range(10):
            vectorUbi[i].append(n)
            n = n+1
            

def comprar():
    global contPlat
    global contGold
    global contSil
    print(preciosEnt)
    while True:
        try:
            entradas = int(input("Ingrese cantidad de entradas a comprar (1-3): "))
            if entradas < 1 or entradas > 3:
                print("Cantidad de entradas invalido (Favor comprar de 1 a 3 entradas.)")
            else:
                while entradas > 0:
                    try:
                        ubicacion()
                        asiento = int(input("\nIngrese un asiento a comprar: "))
                        fila = (asiento - 1) // 10 
                        columna = (asiento - 1) % 10
                        if vectorUbi [fila][columna] == 0 or asiento < 1 or asiento > 100:
                            print("Asiento no disponible, escoja otro.")
                        else:
                            vectorUbi[fila][columna] = 0
                            while True:
                                try:
                                    run = int(input("Ingrese Run (Sin puntos ni digito verificador): "))
                                    vectorAsis.append([run, asiento])
                                    if asiento >= 1 and asiento <= 20:
                                        contPlat = contPlat + 1
                                    elif asiento >= 21 and asiento <= 50:
                                        contGold = contGold + 1
                                    elif asiento >= 51 and asiento <= 100:
                                        contSil = contSil + 1
                                    entradas = entradas - 1
                                    print("Compra realizada con exito.")
                                    break
                                except:
                                    print("Excepcion en run")                                
                    except:
                        print("Excepcion en asiento")
        except:
            print("Excepcion en entradas")
        break
def ubicacion():
    print("""
    ---------------------------------
    |                               |
    |           Escenario           |
    |                               |
    ---------------------------------
    """)
    for i in range(10):
        if i != 0:
            print()
        for j in range(10):
            if vectorUbi[i][j] == 0:
                print(f"{ocupado:>4s}", end='')
            else:
                print(f"{vectorUbi[i][j]:4d}", end='')

def listado():
    vectorUbi.sort()
    print("""
    Listado de Asistentes

    RUN             ASIENTO
    """)
    for i in range(len(vectorAsis)):
        print(f"{vectorAsis[i][0]:7d} {vectorAsis[i][1]:16d}")

def ganancia():
    cantTotal = contPlat + contGold + contSil
    Total = contPlat * 120000 + contGold * 80000 + contSil * 50000
    print(f"""
    Entrada         Cantidad        Total
    Platinum        {contPlat:5d}   ${contPlat * 120000:13d}
    Gold            {contGold:5d}   ${contGold * 80000:13d}
    Silver          {contSil:5d}    ${contSil * 50000:12d}
    Total:          {cantTotal:5d}  ${Total:13d}
    """)

while True:
    try:
        opc = int(input(menu))
        if opc == 1:
            comprar()
        elif opc == 2:
            ubicacion()
        elif opc == 3:
            listado()
        elif opc == 4:
            ganancia()
        elif opc == 5:
            print("Ha salido exitosamente del programa.")
    except:
        print("Excepcion en menu")