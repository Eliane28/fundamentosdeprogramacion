def sueldosdeTrabajadores():
    #Datos de entrada
    n=int(input("Cuantos trabajadores son:"))
    #proceso
    for i in range(1,n+1):
        print('PROCESO'+ repr (i))
        nt=input("Digite el nombre del trabajador:")
        ht=float(input("Digite el valor de horas trabajadas:"))
        sh=float(input("Digite el valor de sueldo por hora:"))
        ss=ht*sh
        desc=0
        if ss>0 and ss<=150:
            desc=ss*0.05
        if ss>150 and ss<=300:
            desc=ss*0.07
        if ss>300 and ss<=450:
            desc=ss*0.09
            ss=ss-desc
        print("Nombre del trabajador:",repr(nt))
        print("Valor de descuento:",repr(desc))
        print("Valor de sueldo semanal:",repr(ss))
sueldosdeTrabajadores()
