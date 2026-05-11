"""
#### Exercício 3 - Comparando listas.

Receba duas listas de input do usuário. Ele digitará como um texto com os números separados por vígula. 
Para isso, pode-se utilizar o código disponibilizado que vai transformar esse texto em lista para você.

Eu quero que você me diga qual das listas tem o maior número dentro delas. 

Se a primeira lista tiver o maior número, imprima: "Primeira".
Se a segunda lista tiver o maior número, imprima: "Segunda".
Se ambas tiverem o mesmo número como maior, digite: "Ambas".

Exemplos:

----------------------------------

Digite a sua primeira lista (separando os números por vírgula): 1, 50, 2, 40
Digite a sua segunda lista (separando os números por vírgula): 0, 2, 99, 1, 1, 3

Resposta:
Segunda

----------------------------------

Digite a sua primeira lista (separando os números por vírgula): 1, 0, 2, 30
Digite a sua segunda lista (separando os números por vírgula): 9, 9, 9, 30

Resposta:
Ambas
"""

# Código para pegar as listas de input
primeira_lista = [*map(int, input("Digite a sua primeira lista (separando os números por vírgula): ").split(","))]
segunda_lista = [*map(int, input("Digite a sua segunda lista (separando os números por vírgula): ").split(","))]

# Fazer a partir daqui

# Verificar o maior número na primeira lista
maior_lista1 = 0
for elemento in primeira_lista:
    if maior_lista1 < elemento:
        maior_lista1 = elemento
#print(maior_lista1)       

# Verificar o maior número na segunda lista
maior_lista2 = 0
for elemento in segunda_lista:
    if maior_lista2 < elemento:
        maior_lista2 = elemento
#print(maior_lista2)    

#Verificar qual lista tem o maior número
if maior_lista1 > maior_lista2:
    print("\n\nResposta:\nPrimeira")
elif maior_lista1 < maior_lista2:
    print("\nResposta:\nSegunda")
else:
    print("\n\nResposta:\nAmbas")


