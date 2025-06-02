# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

entrada = str(input('Digite seu sexo (M/F) > ')).strip().lower()[0]     #Está pegando a 1ª letra
while (entrada !='m') and (entrada != 'f'):
    print('### Dado Inválido ###')
    entrada = str(input('Digite novamente seu sexo (M/F) > ')).strip()
print('Agradecemos pela informação!')  

# Solução Prof. Guanabara ------------------------------------------------------------
# while entrada not in 'MmFf':
#    entrada = str(input('Digite novamente seu sexo (M/F) > ')).strip().lower()[0]
# print('Agradecemos pela informação!') 


