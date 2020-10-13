def suma10Numeros():
def suma10NumerosWhile():
    #Definiendo variables e inicializando variables
    nContadorCondicion,numero, suma=1,0,0
    #Proceso y datos de entrada
@@ -8,4 +8,17 @@ def suma10Numeros():
        nContadorCondicion=nContadorCondicion+1
    #Datos de salida
    print(f"La suma de los 10 numeros ingresados es: {suma}")
suma10Numeros()

def suma10NumerosFor():
    #Definiendo variables e inicializando variables
    numero, suma=0,0
    #Proceso y datos de entrada
    for nContadorCondicion in range(1,11):
        numero=float(input(f"Ingrese el numero de la posicion  {nContadorCondicion} :"))
        suma=suma+numero
    #Datos de salida
    print(f"La suma de los 10 numeros ingresados es: {suma}")


#suma10NumerosWhile()
suma10NumerosFor() 