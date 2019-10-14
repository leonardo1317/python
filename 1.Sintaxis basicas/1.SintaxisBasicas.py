#Así se comenta con el caracter #
#Esta línea está comentada

#Imprimir en pantalla con el método print()
print("Hola mundo")

#Declarar variable
mi_nombre ="mi nombre es python"
print(mi_nombre)

#concatenar texto con el caracter \
texto = "este es un texto\
 multilínea"
print(texto)

#Identación
a=0
for i in range(5):
    a+=1
    print(a)

#Suma
print(5+6)

#Módulo
print(10%3)

#Exponencial
print(5**3)

#Division entera
print(9//2)

#Variables
nombre = 5
print(type(nombre))

nombre = "Juan"
print(type(nombre))

nombre = 5.2
print(type(nombre))

mensaje = """Esto es un mensaje
con tres saltos
de línes"""
print(mensaje)

#condicional if
numero1 = 5
numero2 = 7
if numero1>numero2:
    print("El número 1 es mayor")
else:
    print("El número 2 es mayor")