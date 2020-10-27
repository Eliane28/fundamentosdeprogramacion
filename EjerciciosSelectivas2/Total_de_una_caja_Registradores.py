def Total_de_una_caja_Rejistradora():
    #Datos de entrada 
    texto=' CAJA REGISTRADORA '
    print(format(texto,'=^100'))
    # Procesos
    t=0
    b1000=int(input("Digite cuantos billetes de 1000 tienes:"))
    b500=int(input("Digite cuantos billetes de 500 tienes:"))
    b100=int(input("Digiye cuantos billetes de 100 tienes:"))
    b200=int(input("Digite cuantos billetes de 200 tienes:"))
    b50=int(input("Digite cuantos billetes de 50 tienes:"))
    b20=int(input("Digite cuantos billetes de 20 tienes:"))
    m1=int(input("Digite cuantas monedas de S/.1 tienes:"))
    m2=int(input("Digite cuantas monedas de S/.2 tienes:"))
    m5=int(input("Digite cuantas monedas de S/.5 tienes:"))
    t=(b1000*1000)+(b500*500)+(b100*100)+(b200*200)+(b50*50)+(b20*20)+(m2*2)+(m5*5)+m1
    #Datos de Salida 
    print("\nLa caja registradora almaceno un total de:",t,"\n")
Total_de_una_caja_Rejistradora()
