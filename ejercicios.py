def tablas_multiplicacion(numero):
    for i in range(1, 11):
        res = numero*(i)
        print('{0}x{1}'.format(numero, (i)), "= {0}".format(res))
    

def factorial(numero):
    fact = 1
    while numero > 1:
        fact *= numero
        numero -= 1
    
    return fact

def multiplicar_rango(n, m):
    contador = 1
    while n < (m+1):
        contador *= n
        n += 1
    
    return contador

tablas_multiplicacion(8)
print(factorial(5))
print(multiplicar_rango(10, 16))


# ======================================== Forma didáctica ========================================

def tablas_multiplicacion():

    n = input("Introduce un número positivo: ")
    while n.isalpha() or int(n) < 1:
        n = input("Introduce un número positivo: ")

    numero = int(n)

    for i in range(1, 11):
        res = numero*(i)
        print('{0}x{1}'.format(numero, (i)), "= {0}".format(res))
    
# Para obtener el factorial de un número de una manera mas eficiente se utiliza el módulo math: marh.factorial()
def factorial():
    n = input("Introduce un número que no sea negativo: ")
    while n.isalpha() or int(n) < 0:
        n = input("Introduce un número que no sea negativo: ")

    numero = int(n)
    num = numero

    fact = 1
    while numero > 1:
        fact *= numero
        numero -= 1

    print('{0}! = {1}'.format(num, fact))

def multiplicar_rango():
    n = input("Introduce un número positivo N: ")
    while n.isalpha() or int(n) < 0:
        n = input("Introduce un número positivo N: ")

    m = input("Introduce un número positivo mayor que N: ")
    while m.isalpha() or int(m) < 0:
        m = input("Introduce un número positivo mayor que N: ")

    n = int(n)
    m = int(m)

    contador = 1
    while n < (m+1):
        contador *= n
        n += 1
    
    print(contador)

tablas_multiplicacion()
factorial()
multiplicar_rango()
