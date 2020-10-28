def Ahorro_de_Inversion():
    #Datos de entrada 
    Ahorros= "inversion"
    N=2020-1961
    P=1500.0
    i=15.0/100.0
    ahorros=P*pow(1.0*i,N)
    print(f'valor de P:'+ repr(P))
    print(f'valor de ahorros:'+ repr(ahorros))
    print(f'valor de i:'+ repr(i))
    print(f'valor de N:'+ repr(N))
    print()

Ahorro_de_Inversion()