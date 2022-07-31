""" 4 - Crie uma função que receba um argumento formal e uma possível lista de
elementos. Faça duas chamadas à função, com apenas 1 elemento e na segunda chamada
com 4 elementos """

def show(lista):
    print(lista)

lista = [1]
show(lista)
lista.append(4)
lista.append(5)
lista.append(6)
show(lista)
