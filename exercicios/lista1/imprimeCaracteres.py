""" 10 - Considere a string abaixo. 
Imprima na tela apenas os caracteres da posição 1 a 18. """

string = 'Cientista de Dados é o profissional mais sexy do século XXI'
a = len(string)
for i in range(a):
    if i > 0 and i < 19: 
        print(string[i])
    
