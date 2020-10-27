def Obtencion_de_la_tabla_de_multiplicacion():
    #Datos de entrada 
    texto=' TABLA DE MULTIPLICAR '
    print(format(texto,'=^100'))
    #Procesos 
    k=int(input("Digite el numero que desea multiplacar:"))
    for i in range(1,13):
    # Datos de salida 
        print(f'{i} x {k} = {i*k}')
Obtencion_de_la_tabla_de_multiplicacion()
 