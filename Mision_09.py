#Autor: Oscar Alejandro Torres Maya, A01377686
#Descricpión: Varios programas con listas


#Extrae los numeros pares de una lista
def extraerPares(lista):
    listaPares = []
    for datos in lista:
        if datos%2 == 0:
            listaPares.append(datos)
    return listaPares


#Extrae numeros que son mayores al anterior y los agrega a una nueva lista
def extraerMayoresPrevio(lista2):
    if len(lista2) == 0:
        return lista2
    else:
        nuevaLista = []
        numeroAnterior = lista2[0]
        for datos in lista2:
            if datos > numeroAnterior:
                nuevaLista.append(datos)
                numeroAnterior = datos
            else:
                numeroAnterior = datos
        return nuevaLista


#Intercambia a los datos de posicion
def intercambiarParejas(lista):
    nuevaLista = []
    for indice in range(len(lista)):
        if indice%2 == 0:
            nuevaLista.append(lista[indice])
        else:
            nuevaLista.insert(indice-1, lista[indice])
    return nuevaLista


#Intercambia el valor maximo con el minimo
def intercambiarMM(lista2):
    if len(lista2) == 0:
        return []
    else:
        maximo = max(lista2)
        minimo = min(lista2)
        indiceMax = lista2.index(maximo)
        indiceMin = lista2.index(minimo)
        lista2[indiceMax] = minimo
        lista2[indiceMin] = maximo
    return lista2


#Calcula el promedio de todos los datos sin contar los valores maximos y minimos
def promediarCentro(lista2):
    if len(lista2) <= 2:
        return []
    else:
        maximo = max(lista2)
        minimo = min(lista2)
        suma = sum(lista2) - maximo - minimo
        promedio = suma/(len(lista2)-2)
    return promedio


#Calcula la media y la desviacion estandard
def calcularEstadistica(lista):
    if len(lista) == 0:
        return []

    elif len(lista) == 1:
        return lista[0],lista[0]

    elif len(lista) >= 2:
        suma = sum(lista)
        media = suma/len(lista)
        sumaDeviation = 0
        for datos in lista:
            sumaDeviation += (datos-media)**2
        varianza = sumaDeviation/(len(lista)-1)
        standardDeviation = varianza**0.5
        return media, standardDeviation


def calcularSuma(lista):
    nuevaLista = lista[:]
    if 13 not in nuevaLista:
        return sum(lista)
    else:
        for indice in range(len(nuevaLista)):
            if nuevaLista[indice] == 13:
                nuevaLista[indice] = 0
                if indice != 0:
                    nuevaLista[indice - 1] = 0
                if indice != len(nuevaLista) - 1:
                    nuevaLista[indice + 1] = 0
    return sum(nuevaLista)


def main():
    lista = [1,2,3,4,5,6,4,9,10,20,4]
    lista2 = []
    lista3 = [1,3]
    print("Problema 1. Regresa una lista con los valores pares de la lista original.")
    print("Con la lista", lista, "regresa", extraerPares(lista))
    print("Con la lista", lista2, "regresa", extraerPares(lista2))
    print("Con la lista", lista3, "regresa", extraerPares(lista3))
    print("")

    print("Problema 2. Extrae numeros que son mayores al anterior y los agrega a una nueva lista.")
    print("Con la lista", lista, "regresa", extraerMayoresPrevio(lista))
    print("Con la lista", lista2, "regresa", extraerMayoresPrevio(lista2))
    print("Con la lista", lista3, "regresa", extraerMayoresPrevio(lista3))
    print("")

    print("Problema 3. Intercambia a los datos de posicion con el anterior.")
    print("Con la lista", lista, "regresa", intercambiarParejas(lista))
    print("Con la lista", lista2, "regresa", intercambiarParejas(lista2))
    print("Con la lista", lista3, "regresa", intercambiarParejas(lista3))
    print("")


    #PROFESOR, EL PROGRAMA NO SE PORQUE NO CORRE AQUI PERO SI ABRE UN NUEVO ARCHIVO, CORRE PERFECTO
    print("Problema 4. Intercambia el valor maximo con el minimo.")
    print("Con la lista", lista, "regresa", intercambiarMM(lista))
    print("Con la lista", lista2, "regresa", intercambiarMM(lista2))
    print("Con la lista", lista3, "regresa", intercambiarMM(lista3))
    print("")

    print("Problema 5. Calcula el promedio sin contar maximo y minimo.")
    print("Con la lista", lista, "regresa", promediarCentro(lista))
    print("Con la lista", lista2, "regresa", promediarCentro(lista2))
    print("Con la lista", lista3, "regresa", promediarCentro(lista3))
    print("")

    print("Problema 6. Calcula la media y desviacion estandar de una lista.")
    print("Con la lista", lista, "regresa", calcularEstadistica(lista))
    print("Con la lista", lista2, "regresa", calcularEstadistica(lista2))
    print("Con la lista", lista3, "regresa", calcularEstadistica(lista3))
    print("")

    lista4 = [2,13,1]
    lista5 = [8,9,10,2,13,20,210,102,1]
    print("Problema 7. Calcula la suma de una lista de datos menos los datos alrededor del 13")
    print("Con la lista", lista4, "regresa", calcularSuma(lista4))
    print("Con la lista", lista2, "regresa", calcularSuma(lista2))
    print("Con la lista", lista5, "regresa", calcularSuma(lista5))

main()