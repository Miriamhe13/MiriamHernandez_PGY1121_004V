menu = """
Indique lo que desea hacer:

1) Comprar departamento
2) Mostrar departamentos disponibles
3) Ver listado de compradores
4) Mostrar ganancias totales
5) Salir
"""
indiquePiso = """
Indique un piso del departamento
"""

indiqueLetra = """
Indique una letra del departamento
"""
costos = {
    "A":3800,
    "B":3000,
    "C":2800,
    "D":3500,
}

compradores = []

departamentos =[
    ["A","B","C","D"],
    ["A","B","C","D"],
    ["A","B","C","D"],
    ["A","B","C","D"],
    ["A","B","C","D"],
    ["A","B","C","D"],
    ["A","B","C","D"],
    ["A","B","C","D"],
    ["A","B","C","D"],
    ["A","B","C","D"],
]


def mostrar():
    print("\n")
    print("--------------------------")
    for letras in range(len(departamentos)):
        for value in departamentos[letras]:
            if value != "X":
                numero = letras + 1
                departamento = f"{numero}{value}"
                print(departamento,end="\t")    
            else:
                print(value,end="\t")    
            
        print()
    print("--------------------------")
    print("\n")

def disponible(piso ,letraSeleccionada):
    disponible = bool(False)
    piso -= 1
    
    for letras in departamentos[piso]:
        for letra in range(len(letras)):
          if letras[letra] == letraSeleccionada:
                disponible = bool(True)
    return disponible
            
     
def vender(piso , letraSeleccionada):
    disponible = bool(False)
    piso -= 1
    for letras in departamentos[piso]:
        for letra in range(len(letras)):
           if letras[letra] == letraSeleccionada:
                departamentos[piso][letra] = "X"
                disponible = bool(True)
    return disponible

def listaCompradores():
    for value in compradores:
        print( value['rut'])
    
continuarVender = bool(True)

def validarOpcion(opcion):
    respuesta =  bool(False)
    if opcion > 0 and opcion <= 5:
        respuesta = bool(True)
    return respuesta
def mensajeError(mensaje):
     print("******************************************************************")
     print(mensaje)
     print("******************************************************************")
     
def mensajeOk(mensaje):
     print("-------------------------------------------------------------------")
     print(mensaje)
     print("-------------------------------------------------------------------")


def registrarCliente(piso,letra):
   
    continuar = bool(True)
    rut=""
    while continuar :
        rut= input ("Ingrese el RUT del cliente sin digitador ni puntos ni guiones. :")
        rut = rut.replace(".", "").replace("-", "")
        if rut.isdigit():
            continuar = bool(False)
    venta = {
        "rut":rut,
        "precio":costos[letra.upper()],
        "piso":piso,
        "letra":letra,
    }
    compradores.append(venta)

def ordenarImprimir():
    
    lista_ordenada = sorted(compradores, key=lambda x: x['rut'])

   
    for value in lista_ordenada:
        print("Rut ",value['rut'])
    

def opcionVender():
    opcionDepartamentoContinuar = True
    while opcionDepartamentoContinuar:
       
        validarEsNumero = True
        while validarEsNumero:
            try:
                piso = int(input(indiquePiso))
                validarEsNumero =False
            except Exception as e:
                mensajeError("Debe ingresar un número")
                
        
        
        letra = str(input(indiqueLetra))
        letra = letra.upper()
        if disponible(piso,letra):
            vender(piso,letra)
            registrarCliente(piso,letra)
            opcionDepartamentoContinuar = False
            continue
        else:
            mensajeError("No esta disponible")
            opcionVender()

def costoTotal():

    for value in costos:
        for value in compradores:
            if value['letra'] == value:
                print(value[value])
      
    
        
            
while continuarVender:
    
    try:
         opcion = int(input(menu))
    except Exception as e:
        mensajeError("Debe seleccionar una opcion númerica y valida")
        continue
   
    if validarOpcion:
        if opcion == 1:
            opcionVender()
        if opcion == 2:
            mostrar()
        if opcion == 3:
           ordenarImprimir()
        if opcion == 4:
            costoTotal()
        if opcion == 5:
            continuarVender = False
    else:
        mensajeError("Seleccione una opcion valida")