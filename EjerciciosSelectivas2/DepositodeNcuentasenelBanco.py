def depositoXcuentabanco():
    #Datos de entrada 
    t=0
    n=int(input("Digite el valor de año que desea depositar:"))
    # proceso 
    for i in range (1,n+1):
        print('PEOCESO'+repr (i))
        c1=float(input("Digite la cantidad de pesos del mes de Enero:"))
        c2=float(input("Digite la cantidad de pesos del mes de Febrero:"))
        c3=float(input("Digite la cantidad de pesos del mes de Marzo:"))
        c4=float(input("Digite la cantidad de pesos del mes de Abril:"))
        c5=float(input("Digite la cantidad de pesos del mes de Mayo:"))
        c6=float(input("Digite la cantidad de pesos del mes de Junio:"))
        c7=float(input("Digite la cantidad de pesos del mes de Julio:"))
        c8=float(input("Digite la cantidad de pesos del mes de Agosto:"))
        c9=float(input("Digite la cantidad de pesos del mes de Setiembre:"))
        c10=float(input("Digite la cantidad de pesos del mes de Octubre:"))
        c11=float(input("Digite la cantidad de pesos del mes de Nobiembre:"))
        c12=float(input("Digite la cantidad de pesos del mes de Diciembre:"))
        inte=t*0.1
        t=t+inte+c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12
        inf=t
     # Datos de salida 
        print("El valor de interes es:",repr(inte))
        print("El valor de inversion final es:",repr(inf))
        print("La cantidad total es:",repr(t))
depositoXcuentabanco()
