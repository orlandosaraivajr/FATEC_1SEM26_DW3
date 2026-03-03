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