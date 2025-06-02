#################### Variáveis compostas - Tuplas ####################

#  -> As tuplas são IMUTÁVEIS
# '()' -> para tuplas
# '[]' -> para listas
# '{}' -> para dicionários

lanche = ('pizza', 'coca', 'batata frita', 'hambuguer')
# Print 1
for comida in lanche:
    print(f'(print 1) Hoje vou comer {comida}')
print('\n')
# Print 2
for count in range(0, len(lanche)):
    print(f'(print 2) Hoje vou comer {lanche[count]}') 
print('\n')
# Enumerate -> me mostra dado e posição
# Print 3
for posicao, comida in enumerate(lanche):
    print(f'(print 3) Hoje vou comer {comida} (posição {posicao}) ')

# -------------------- Metodos para usar nas tuplas --------------------
#  -> 'sorted()': mostra a tupla em ordem
a = (2, 3, 4, 5)
b = (5, 4, 8, 2, 1)
c = (a+b)
print(len(c))       # Tamanho
print(c.count(5))   # Conta as aparições de um determinado numero
print(c.index(8))   # Em que posição tal número esta (pega a primeira occorrência)
del(a)              # Apaga um determinado valor da memória
print(a)