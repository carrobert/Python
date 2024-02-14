'''"Precisamos imprimir um número para cada andar de um hotel de 20 andares.
Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.

Escreva um código que imprima todos os números exceto o número 13.

Escreva mais um código que resolva o mesmo problema,
mas dessa vez usando o laço de repetição 'while'.

Como desafio, imprima eles em ordem decrescente (20, 19, 18...)"'''

#Imprimir todos os números, exceto 13 (laço 'for_ in range')

for i in range(1,21):
    if i == 13:
        continue
    else:
        print(i,"andar")

#Imprimir todos os números, exceto 13 (laço 'while')

contador = 1
while contador <= 20:
    if contador == 13:
        contador = contador + 1
        continue
    else:
        print(contador,"andar")
        contador = contador + 1

#Imprimir todos os números, exceto 13 em ordem decrescente

for i in range(20,0,-1):
    if i == 13:
        continue
    else:
        print(i,"andar")

