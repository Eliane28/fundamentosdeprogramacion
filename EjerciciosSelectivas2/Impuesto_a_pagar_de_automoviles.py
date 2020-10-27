def Impuesto_a_pagar_de_automoviles():
    #Datos de entrada 
  cat1=0
  cat2=0
  cat3=0
  ip=0
  n=int(input("Digite la cantidad de automoviles:"))
  # Procesos
  for i in range (1,n+1):
      print('PROCESO'+repr(i))
      clave=int(input("Digite la clave del vehiculo:"))
      costo=float(input("Digite el valor de costo:"))
      impt=0
      if clave==1:
          impt=costo*0.1
          cat1=cat1+impt
      if clave==2:
          impt=costo*0.07
          cat2=cat2+impt
      if clave==3:
          impt=costo*0.05
          cat3=cat3+impt
      ip=ip+impt
      # Datos de salida 
      print("\nValor de impuesto es:",repr(impt))
      print("Valor de vehiculo 1:",repr(cat1))
      print("Valor de vehiculo 2:",repr(cat2))
      print("Valor de vehiculo 3:",repr(cat3))
      print("Valor de impuesto a pagar",repr(ip))
Impuesto_a_pagar_de_automoviles()
