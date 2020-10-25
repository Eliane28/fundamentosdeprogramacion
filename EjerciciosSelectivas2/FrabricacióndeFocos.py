def FrabricacióndeFocos():
    # Procesos y datos de entrada 
     n= int(input("Digite la cantidad de focos que hay en el lote:"))
     rojo=0 
     verde=0
     blanco=0
     foco=0
     for i in range(1,n+1):
            foco = input("Digite el color del foco: rojo, verde o blanco: ")
            if foco =='rojo':
                   rojo = rojo + 1
            elif foco == 'verde':
                   verde = verde + 1
            elif foco =='blanco':        
                    blanco = blanco + 1 
      
     print("los focos rojos son:", rojo, "los focos verdes son:", verde, "los focos blancos son:",blanco) 
FrabricacióndeFocos()

