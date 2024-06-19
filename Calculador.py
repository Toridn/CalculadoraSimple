

#Funcion que suma los valores
def Suma(num1, num2):
    res=num1+num2
    return res
#Funcion que rest los valores
def Resta(num1, num2):
    res=num1-num2
    return res
#Funcion que multilica los valores
def Multiplicacion(num1,num2):
    res=num1*num2
    return res
#Funcion que divide los valores
def Dividir(num1, num2):
    if num2!=0:
        res= num1/num2
        return res
    else:
        print("No se puede dividir por 0")



#MAIN
#Menu
while True:
    print("1.-Sumar")
    print("2.-Restar")
    print("3.-Multiplicar")
    print("4.-Dividir")
    print("5.-Salir")
    op=int(input("Ingrese el numero de la operacion que desea realizar: "))

    if op==1 or op==2 or op==3 or op==4 :
        Numero1 = int(input("Ingrese el primer numero: "))
        Numero2 = int(input("Ingrese el segundo numero: "))

    if op==1:
        #resultado = Suma(Numero1,Numero2)
        print("El resultado de la suma es: ",Suma(Numero1,Numero2))
    elif op==2:
        print ( "El resultado de la resta es: " , Resta( Numero1 , Numero2 ) )
    elif op==3:
        print ( "El resultado de la multiplicacion es: " , Multiplicacion( Numero1 , Numero2 ) )
    elif op==4:
        print ( "El resultado de la divicion es: " , Dividir( Numero1 , Numero2 ) )
    elif op==5:
        break
    else:
        print("Ingrese un valor correcto")




