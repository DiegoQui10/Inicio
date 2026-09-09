#Primer repaso 
# """""""""""
#  primer ejemplo y vistaso a el uso de un condicional
# 
# "

a = int(input("¿De que año es tu computador?: "))

if a >= 0 and a <= 2:
    print("Tu computador es nuevo")
# primer vistaso con una unica condición
else:
    print("Tu computador es viejo")
# Intrucción con una condicion más y agregamos el uso del "else"

#Ejemplo completo IF ELIF ELSE 

edad = int(input("Ingrese su edad: "))

if edad <0:
    print("Debe ingresar una edad correcta")
elif edad <16:
    print("Todavia no puede conducir")
elif edad <18:
    print("puedes obtener un permiso de conducir")
elif edad <70:
    print("puede obtener la licencia estandar")
else:
    print("Require de una licencia especial")
    
    

