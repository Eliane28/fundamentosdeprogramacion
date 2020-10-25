def Hambuergueas():
   r1=0
   r2=0
   print("HOLA BIENVENIDO")
   print("Que Hamburguesas deseas:\n")
   print("Sencilla = S")
   print("doble = D")
   print("Triple = T")
   c=input(f"Digite su tipo de hamburguesa:")
   N=int(input(f"Digite cuantas hamburhuesa desea:"))
   #proceso
   if c=='S':
       r1=20*N
       r2=r1+(r1*0.05)
   if c=='D':
       r1=25*N
       r2=r1+(r1*0.05)
   if c=='T':
       r1=28*N
       r2=r1+(r1*0.05)   
   print("Usted debe pagar:",r2)
Hambuergueas()