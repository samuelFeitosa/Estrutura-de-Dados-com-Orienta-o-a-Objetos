# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1--V6UL7YaY8cIRnggNk_YnqvuKw8vInt
"""

# Listagem 6.6

notas = [0, 0, 0, 0, 0]

soma = 0

x = 0

while x<5:
    notas[x] = float (input ("nota %d: " %x))

    soma += notas[x]
  
    x += 1
  
x = 0

while x<5:
    print("Nota %d: %6.2f" % (x, notas[x]))
    x += 1

  print("Média: %5.2f" % (soma/x))

# Esta sintaxe tem por objetivo inicializar todas as notas com valor zero. Após isso, é realizado um loop de repetição para que sejam inseridas as notas, e por fim, é calculado e impresso a média final.