# -*- coding: utf-8 -*-
"""aula_0708_map.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Eyy-KjUNhnQU9R4Rl6icd7uIJKsC23O0
"""

# Exemplo SEM utilizar o MAP

def calcula_dobro(lista, tam):
  lista_dobro = []
  for i in range(tam):
    lista_dobro.append(lista[i]*2)
  return(lista_dobro)

lista = [5,7,4,3,2,6]
tam = 6
lista_dobro = calcula_dobro(lista,tam)
print(lista_dobro)

# Exemplos COM utilização do MAP
def calc_dobro(elem):
  return(elem * 2)

lista = [5,7,4,3,2,6]

lista_dobro = list(map(calc_dobro,lista))

print(lista_dobro)

# Fazer o acrescimo de 10% aos valores de uma lista de preços

def calcula_acrescimo(valor):
  return(valor * 1.10)

lista_precos = [40.50, 100.30, 245.80, 340.20, 150.75]

lista_acrescimos = list(map(calcula_acrescimo, lista_precos))

print(lista_acrescimos)

