#tarea hogar
#1
a = int(input('ingrese su primer numero'))
b = int(input('ingrese su segundo numero'))

resultado = a + b
print(resultado)

print(resultado - 3)
print (resultado *7)
print (resultado /2)


#2
numero= int(input("ingresa el numero"))
resultado=numero%2==0
print(resultado)

#3
a= int(input("ingresa el numero"))
b= int(input("ingresa el numero"))
resultado= a == b
print(resultado)

#4
numero= int(input("ingresa el numero"))
dias = 366
resultado = numero == 366
print(resultado)
#5
monto= int(input("ingresa un monto"))
descuento= int(input("ingresa un descuento"))
operacion= monto *(descuento/100)
precio = monto-operacion
print (precio)
limite= 100 
resultado = precio<limite
print (resultado)