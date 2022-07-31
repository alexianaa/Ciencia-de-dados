""" 9 - Faça um programa que conte quantas vezes a letra "r" aparece na frase
abaixo. """

frase = "É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir."
count = 0
for i in frase:
    if i == 'r':
        count += 1
print('A letra "r" aparece',count, 'vezes')
