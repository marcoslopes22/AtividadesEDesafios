# -*- coding: utf-8 -*-
"""Desafio03.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1o_ZfsMgTpT74gLYxsEhTxNHdK0rW_Pgy
"""

#DESAFIOS INICIANTES EM PYTHON
#ALUNO: MARCOS AURELIO


#DESAFIO 3: ALGORITMO QUE VERIFICA SE UM TEXTO É UM PALÍNDROMO.

print("\n------------------------------------------------------------------------")
print("DESAFIO 3: ALGORITMO QUE VERIFICA SE UM TEXTO É UM PALÍNDROMO.\n")

meuTexto = str(input("Digite o texto que deseja verificar(sem espaços): "))

def detector(meuTexto):
  if (meuTexto == meuTexto[::-1]):
    print("\nTexto digitado: ",meuTexto)
    print("\nEsse texto é um palíndromo, pois >", meuTexto, "< ao contrário fica >", meuTexto[::-1],"<.")
  else:
    print("\nTexto digitado: ",meuTexto)
    print("\nEsse texto não é um palíndromo, pois >", meuTexto, "< ao contrário fica >", meuTexto[::-1],"<.")

detector(meuTexto)
