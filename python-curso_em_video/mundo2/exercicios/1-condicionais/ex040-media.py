# Crie um programa que leia duas notas de um aluno e calcule sua média, 
# mostrando uma mensagem no final, de acordo com a média atingida:
# –> Média abaixo de 5.0:   REPROVADO
# –> Média entre 5.0 e 6.9: RECUPERAÇÃO
# –> Média 7.0 ou superior: APROVADO


nota1 = float(input('Qual sua primeira nota? '))
nota2 = float(input('Qual sua segunda nota? '))

media = ((nota1+nota2)/2)

if media<5:
  print('Sua média foi {:.2f}, portando você foi REPROVADO!'.format(media))
  
elif media>=5.0 and media<=6.9:
  print('Sua média foi {:.2f}, portando você está na RECUPERAÇÃO!'.format(media))
  
elif media>=7.0:
  print('Sua média foi {:.2f}, portando você foi APROVADO!'.format(media))