""" 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e
guarde os resultados em uma lista """

tupla = (4,5,6,7)
lista = []
for i in range(4):
    lista.append(tupla[i]*2)
print(lista)