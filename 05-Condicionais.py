#5)Faça um programa que leia a validade das informações:
#a. Idade: entre 0 e 150;
#b. Salário: maior que 0;
#c. Sexo: M, F ou Outro;
#O programa deve imprimir uma mensagem de erro para cada informação inválida.

idade = float(input('Informe sua idade (entre 0 a 150): '))
salario = float(input('Informe seu salário (maior que 0): '))
sexo = input('Informe seu sexo (M, F ou Prefiro não Informar): ')

if (0 > idade) or (idade > 150):
  print('Idade inválida.')
if salario<0:
  print('Salário inválido.')
if sexo != 'M' and sexo != 'F' and  sexo != 'Prefiro não Informar':
  print('Sexo inválido.')