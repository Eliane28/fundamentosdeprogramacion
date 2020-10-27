def calificacionAlumnos():
    # Datos de entrada 
    apr=0
    desp=0
    ca=int(input("Digite la calificación aprobatoria:"))
    n=int(input("Digite la cantidad de alumnos:"))
    # Procesos 
    for i in range(1,n+1):
        print('PROCESO'+ repr (i))
        nota=int(input("Digite la calificacion:"))
        if nota>=ca:
            apr=apr+1
        else:
            desp=desp+1
            # Datos de salida 
        print()
    print("La cantidad de aprobados son:",repr(apr))
    print("La cantidad de desaprobados son:",repr(desp))
calificacionAlumnos()