""" 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a
função não recebe parâmetro) e depois faça uma chamada à função para listar os números """

def imprimePares():
    for i in range(19):
        if ((i+1)%2) == 0:
            print(i+1)

imprimePares();