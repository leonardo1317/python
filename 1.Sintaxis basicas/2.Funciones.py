def mensaje():
    print("Hola mundo")    
mensaje()

def suma():
    num1=5
    num2=7
    print(num1+num2)
suma()

#Funcion con parámetros
def suma_con_parametro(num1, num2):
    resultado = num1+num2
    return resultado

print(suma_con_parametro(5,7))
print(suma_con_parametro(2,3))
print(suma_con_parametro(35,358))
