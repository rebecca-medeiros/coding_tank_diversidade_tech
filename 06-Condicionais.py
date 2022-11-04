#6)Vamos fazer um programa para verificar quem é o assassino de um crime. Para descobrir o assassino, a polícia faz um pequeno questionário com 5 perguntas onde a resposta só pode ser sim ou não:

print('Responda às perguntas abaixo com "sim" ou "não":')
moradia=input('Mora perto da vítima? ')
trabalho=input('Já trabalhou com a vítima?' )
contato=input('Telefonou para a vítima?' )
local=input('Esteve no local do crime?' )
divida=input('Devia para a vítima? ')


if moradia == 'sim':
  moradia = 1
elif moradia == 'não':
  moradia = 0
if trabalho == 'sim':
  trabalho=1
elif trabalho == 'não':
  trabalho = 0 
if contato == 'sim':
  contato = 1
elif contato == 'não':
  contato = 0
if local == 'sim':
  local = 1
elif local == 'não':
  local = 0 
if divida == 'sim':
  divida = 1
elif divida == 'não':
  divida = 0 
soma = moradia+trabalho+contato+local+divida


if soma <= 1:
  print('Pessoa não é suspeita e pode ser liberada.')
if soma == 2:
  print('Pessoa é suspeita e deve ser investigada.')
if 2<soma<5:
  print('Pessoa é cúmplice do crime.')
if soma == 5:
  print('Pessoa é assassina.')