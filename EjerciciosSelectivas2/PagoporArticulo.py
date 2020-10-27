def pagoporArticulo():
    pxt=0
    n=int(input("Digite la cantidad de articulos:"))
    #proceso
    for i in range(1,n+1):
        print('PROCESO' + repr(i))
        precio=float(input("Digite el precio del articulo:"))
        desc=precio*0.1
        if precio>=200:
            desc=precio*0.15
        if precio>100 and precio<200:
            desc=precio*0.12
        costo=precio-desc
        pxt=pxt+costo
        print("El costo es",repr(costo))
        print("El descuento es",repr(desc))
        print("El pago de todos los articulos es",repr(pxt))
pagoporArticulo()