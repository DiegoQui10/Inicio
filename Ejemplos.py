#Punto 1 
#Mostrar Edad de una persona

a = int(input("Ingrse su edad: "))

if a < 0:
    print("Ingrese una edad correcta")
elif a < 18:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")
    
####
#Punto 2
#Numero positivo, negativo o cero 

b = int(input("Ingrese un numero: "))

if b < 0:
    print("El numero es negativo")
elif b > 0:
    print("El numero es positivo")
else:
    print("El numero es 0")
    
#######
#Punto 3
#Aprboar o suspender 

c = int(input("Ingrese su nota: "))

if c < 0:
    print("Ingrese una nota correcta")
elif c < 5:
    print("Suspendido")
elif c >= 5 and c <= 6:
    print("Aprobado")
elif c >= 7 and c <= 8:
    print("Notable")
elif c <= 10:
    print("Sobresaliente")
else:
    print("Ingrese una nota correcta")


#######
#Punto 4 
# Numero mayores menos e iguales

d = int(input("Ingrese primer numero: "))
e = int(input("Ingrese segundi numero: "))

if d == e:
    print("Los numero son iguales")
elif d > e:
    print(d, "es mayor")
    print(e,"es menor")
elif e > d:
    print(e,"es mayor")
    print(d,"es menor")
elif d < e:
    print(d, "es menor")
    print(e,"es mayor")
elif e < d:
    print(e, "es menor")
    print(d,"es mayor")
else:
    print("Solo ingrese numeros")
    

#######
#Punto 5
#Contraseña correcta

contraseña_correcta = "python123"

contraseña = input("Ingrese la contraseña: ")

if contraseña == contraseña_correcta:
    print("Acceso permitido")
else:
    print("Contraseña incorrecta")
    
    
######
#Punto 6
#Dias de la semana


dia = int(input("Ingrese un numero para seleecionar un dia de la semana: "))

if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miercoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
elif dia == 6:
    print("Sabado")
elif dia == 7:
    print("Domingo")
else:
    print("Ingrese un numero correcto")


######
#Punto 7 
#Par o Impar

numero = int(input("Ingrese un numero: "))

if numero == 0:
    print("El numero es cero")
elif numero < 0:
    print("El numero es negativo")
elif numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")
    
    
########
#punto 8 
#Calculadora 

print("1 suma")
print("2 resta")
print("3 multiplicación")
print("4 división")
operacion = int(input("Ingrese un numero: " ))


numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))


if operacion == 1:
    resultado = numero1 + numero2
    print(resultado)
elif operacion == 2:
    resultado = numero1 - numero2
    print(resultado)
elif operacion == 3:
    resultado = numero1 * numero2
    print(resultado)
elif operacion == 4:
    if numero2 == 0:
        print("No se puede dividir por 0")
    else:
        resultado = numero1 / numero2
        print(resultado)
else:
    print("Ingrese un numero correcto")
    
# print(type(operacion))
    

##########
#Punto 9 
#Semaforo

print("1 Verde")
print("2 amarillo")
print("3 rojo")

smf = int(input("seleccione un color: "))

if smf == 1:
    print("Puede pasar")
elif smf == 2:
    print("Ten cuidado")
elif smf == 3:
    print("Debe parar")
else:
    print("Ingrese un numero correcto")

##########
#Punto 10 
#Tienda con descuento

print("Si su compra es mayor a $100, tendra un descuento del 20%")
print("Si su compra esta entre $50 a $100, tendra un descuento del 10%")
print("Si su compra es menor a $50, no tendra descuento")

precio = int(input("Ingrese el precio a pagar para calcular su descuento: "))

if precio <= 0:
    print("No ha comprado nada")
elif precio < 50:
    print("Usted no tiene descuento y su total a pagar es: ", precio)
elif precio >= 50 and precio <= 100:
    descuento = precio * 10/100
    total = precio - descuento
    print("Se le aplico un descuento de 10% y usted debe pagar: ", total)
elif precio > 100:
    descuento = precio * 20/100
    total = precio - descuento
    print("Se le aplico un descuento del 20% y usted debe pagar: ", total)
else:
    print("Solo ingrese numeros")
     

