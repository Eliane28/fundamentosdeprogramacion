def Calificacion():
     n1=int(input("Nota de primera unidad:"))
     n2=int(input("Nota de primera unidad:"))
     n3=int(input("Nota de primera unidad:"))
     n4=int(input("Nota de primera unidad:"))
    #proceso 
    pc=(n1+n2+n3+n4)/4
    #datos de salida
    print("la nota final es : ",pc) 

promedio_de_la_nota()

def Monto_bono_del_profesor():
    # #Definiendo variables e inicializando variables
    monto,salario,puntos=0
    puntos=int(input("Digite el valor de puntos:"))
    salario=int(input("Digite el salario minimo:"))
    #Proceso y datos de entrada
    if  puntos >= 50:
    monto <- salario * 0.1
    if puntos <= 100:
    monto <- salario * 0.1
    if  puntos >=101 y puntos <= 150:
    monto <- salario * 0.50
    if puntos >=151:
    monto <- salario * 0.8
    #datos de salida 
    print("El monto del bono del profesor es:",monto)


