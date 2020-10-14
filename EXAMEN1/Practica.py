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

def VacunacovidNMVA():
 str
 tipoA=int(0)
 tipoB=int(0)
 tipoC=int(0)
 for x in range(0,1):
    edad=int(input("ingresar la edad:"))
    sexo=int(input("ingresar el sexo >>[1:varon;2:mujer]:"))
    if (edad>70) :
           print("se aplicara la vacuna tipo C")
           tipoC=tipoC+1
    if (edad>15 and edad <70 and sexo==2):
        print("se aplicara vacuna B")
        tipoB=tipoB+1
    if(sexo==1 or (edad<16)):
        print("se aplicara vacuna tipo A")
        tipoA=tipoA+1
VacunacovidNMVA()  

def CalcularOperacion():
    #datos de entrada
    str
    operacion=int(input("(1) suma, (2) resta, (3) multiplicacion, (4) division, (5) potencia:"))
    dato1=int(input("ingresar el primer valor: "))
    dato2=int(input("ingresar el segundo valor: "))
    #proceso

    if (operacion==1) :
        suma=dato1+dato2
        print("el reultado es", suma)
    
    if (operacion==2) :
        resta=dato1-dato2
        print("el reultado es", resta)
    
    if (operacion==3) :
        multiplicacion=dato1*dato2
        print("el reultado es", multiplicacion)
    
    if (operacion==4) :
        division=dato1/dato2
        print("el reultado es", division)
    
    if (operacion==5) :
        potencia=dato1**dato2
        print("el reultado es", potencia)
CalcularOperacion()

def Incremento_Salario():
    str
print("inicio")
salario=1400
for años in [1,2,3,4,5,6]:
     print(f"La cantidad de años es {años} y tu salario es {salario*100/100}")
     salario=salario*1.1
Incremento_Salario()

ELIAN

