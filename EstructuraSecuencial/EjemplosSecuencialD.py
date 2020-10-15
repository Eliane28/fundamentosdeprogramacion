def CalcularPromedioNota():
    #Datos de Entrada
    N1 = int(input('Ingrese Nota 1: '))
    N2 = int(input('Ingrese Nota 2: '))
    N3 = int(input('Ingrese Nota 3: '))
    N4 = int(input('Ingrese Nota 4: '))
    #Proceso
    PC = (N1+N2+N3+N4)/4
    #Dato de salida
    print(f'El promedio de la calificacion es: {PC}')

def CalcularElPintado():
     #Datos de Entrada
    cantidadM2= int(input('Ingrese la cantidad m2 a pintar: '))
    costoM2 = int(input('Costo por m2 : '))
    #Proceso
    montoC = cantidadM2 * costoM2
    #Dato de salida
    print(f'Monto a cobrar es : {montoC}')    
