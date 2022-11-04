#4) Escreva um programa que peça a nota de 3 provas de um aluno e verifique se ele passou ou não de ano.
nota1=float(input('Informe sua primeira nota: '))
nota2=float(input('Informe sua segunda nota: '))
nota3=float(input('Informe sua terceira nota: '))
media = (nota1+nota2+nota3)/3

if media > 6:
  print('Você passou de ano!')
else:
  print('Você não passou de ano.')