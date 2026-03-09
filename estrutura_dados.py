# Link do Zeal: https://zealdocs.org/
# Numeros
numero1 = 10
numero2 = 10.5
numero3 = 4 + 2j
print(type(numero1))
print(type(numero2))
print(type(numero3))

##
# class str - Tudo é objeto em Python

nome = 'Fatec Araras'
print(nome.lower())

for letra in nome:
    print(letra)

# Lista
lista = []
lista.append('Leite')
lista.append('pão')
lista.append('café')

print(lista[0])

# Tupla -> imutável
tupla1 = tuple(lista)
print(type(tupla1))

# https://leetcode.com/problems/merge-two-sorted-lists/description/


'''
09 de março
Desafio: remover elementos duplicados
'''
lista = list(range(1,10))
lista = lista + list(range(5,15))
lista = lista + list(range(10,35))
print(lista)

# Primeira versão
lista2 = []
for elemento in lista:
    if elemento not in lista2:
        lista2.append(elemento)

# Segunda versão

lista3 = list(set(lista))

conjunto1 = set([1,2,3,4,5,6,7])
conjunto2 = set([5,6,7,8,9,10])

# Dicionário

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
f = dict({'one': 1, 'three': 3}, two=2)
