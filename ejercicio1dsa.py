lista = [1,2,3,4,5,6,7,8,9,10]
numeroin = float(input("ingresa un numero para comprobar que este en la lista: "))
if numeroin in lista:
    print("el numero: ",numeroin,"esta en la lista: ",lista)
else:
    print("el numero: ",numeroin,"no esta en la lista.")