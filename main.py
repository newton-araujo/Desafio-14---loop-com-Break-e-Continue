'''
Desafio 14 - Loop com Break e Continue 

Para este desafio, vamos criar um loop que imprima os números de 1 a 10.
1° Loop:
- Requisitos:
    *Deverá ir até o número 5, e parar.

2° Loop:
- Requisitos:
    *Deverá imprimir os números de 1 a 10 e pular o número 5.

'''

#1° Loop com o break
for contador in range(1,11):
    if contador == 5:
        break
    print(contador)

#2° Loop com o continue
    
for contador in range(1,11):
    if contador == 5:
        continue
    print(contador)


