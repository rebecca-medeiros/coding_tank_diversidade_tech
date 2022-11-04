#7)Desafio - Um hospital quer fazer o diagnóstico de gripe ou dengue a partir de um questionário de sintomas, tendo as perguntas abaixo, faça um programa que faça o diagnóstico deste hospital:
print('Responda às perguntas abaixo com "sim" ou "não":')
A=input('Sente dor no corpo? ')
B=input('Você tem febre? ')
C=input('Você tem tosse? ')
D=input('Está com congestão nasal? ')
E=input('Tem manchas pelo corpo? ')

if A=='sim' and B=='sim' and C=='não' and D=='não' and E=='sim':
  print ('Você está com dengue.')
elif A=='sim' and B=='sim' and C=='sim' and D=='sim' and E=='não':
  print ('Você está com gripe.')
elif A=='não' and B=='sim' and C=='sim' and D=='sim' and E=='não':
  print ('Você está com gripe.')
elif A=='sim' and B=='não' and C=='não' and D=='não' and E=='não':
  print ('Você está sem doenças.')
elif A=='não' and B=='não' and C=='não' and D=='não' and E=='não':
  print ('Você está sem doenças.')
else:
  print('Não foi possível definir um diagnóstico. Por favor, procure um profissional.')