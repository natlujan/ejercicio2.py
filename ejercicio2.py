#Funciones
#Crear una rutina, que mediante una función nos indique cuál es el número mayor

def comparar(n1, n2):
    if n1 < n2:
        print(n2)
    elif n2 < n1:
        print(n1)
    else:
        print ("Son iguales")

comparar(8,8)

def compatres(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        print(n1)
    elif n2 > n1 and n2 > n3:
        print(n2)
    elif n3 > n1 and n3 > n2:
        print(n3)
    else:
        print ("Son iguales")

compatres(78, 85, 69)

#Función que calcule la longitud de una lista o una cadena.
def largo(lista):
    cont = 0
    for i in lista:
        cont += 1
    return cont
print(largo("hola"))
print(largo([1,2,3,4,5]))

#Función que nos indique True si encuentra una vocal
def es_vocal(x):
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        return True
    elif x == "A" or x == "E" or x == "I" or x == "O" or x == "U":
        return True
    else:
        return False
    
print(es_vocal("a"))


