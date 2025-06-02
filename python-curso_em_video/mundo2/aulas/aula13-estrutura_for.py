#################### Estrutura de repeticao FOR ####################

print('for c in range(inicio, fim, icremento)')

print('\n# Imprime 5 vezes pq ignora o último [range(1,6)]')
for c in range(1,6):
    print('1')
     
print('\n# Imprime de 1 a 6 [range(1, 7)]')
for c in range(1, 7):
    print(c)

# Se não colocar terceiro parametro ele icrementa 1, se quiser diminuir colocar -1
print('\n# Imprime de 6 a 0 [range(6, 0, -1)]')
for c in range(6, 0, -1):
    print(c)

# TERCEIRO PARAMETRO -> serve para ajustar o icrementador 


