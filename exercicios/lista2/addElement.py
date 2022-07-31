""" 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos,
adicione 2 elementos a lista e imprima a lista """

def addElement(lista):
    lista.append(6)
    lista.append(7)
    print(lista)

lista = [1,2,3,4]
addElement(lista)