# -*- coding: utf-8 -*-
"""Desafio02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FR88-v8LOht_zD1T06TmYyb54ckcMGSQ
"""

#DESAFIOS INICIANTES EM PYTHON
#ALUNO: MARCOS AURELIO


#DESAFIO 2: BUSCA EM UMA LISTA DE 100 NÚMEROS ALEATÓRIOS INTEIROS E ORDENADOS.

print("\n------------------------------------------------------------------------")
print("DESAFIO 2: BUSCA EM UMA LISTA DE 100 NÚMEROS ALEATÓRIOS INTEIROS E ORDENADOS.\n")

numeroSolicitado = int(input("Por favor, digite um número inteiro: "))
listaOrdenada = []

def criarListaOrdenada(listaOrdenada):
  for x in range(101):
      listaOrdenada.append(x)
  listaOrdenada.remove(0)
  print("\nUm momento, estamos criando uma lista ordenada...")
  print("Lista criada com sucesso!")
  analisarLista(listaOrdenada)

def analisarLista(listaOrdenada):
  if numeroSolicitado in listaOrdenada:
    print("\nNúmero solicitado:", numeroSolicitado)
    print("\nO número >", numeroSolicitado, "< se encontra no índice >",listaOrdenada.index(numeroSolicitado),"< da nossa lista.")
  
  else:
    print("\nNúmero solicitado:", numeroSolicitado)
    print("\nDesculpe, o número >", numeroSolicitado, "< não está na lista.")

criarListaOrdenada(listaOrdenada)
