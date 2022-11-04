#2) Faça um programa que peça um número e mostre se ele é positivo ou negativo.

numero = float(input('Informe um número: '))
if numero>0:
  print('O número informado é positivo.')
elif numero<0:
  print('O número informado é negativo.')
else:
  print('O número informado é zero.')