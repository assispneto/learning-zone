# Crie um programa que leia e compare duas frases qualquer e 
# diga se elas são um palíndromo, desconsiderando os espaços.

# OBS -> Palidromo é algo que se ler da mesma forma ao contrário


frase1 = str(input('Digite a primeira frase > ')).strip().lower()
frase2 = str(input('Digite a segunda frase > ')).strip().lower()     

# Tratando os valores recebidos
# 1) Separo suas palavras
palavras1        = frase1.strip()           
palavras2        = frase2.strip() 
# 2) Junto todas as palavras 
frase1Junta      = ''.join(palavras1)        
frase2Junta      = ''.join(palavras2)

# Declaro o vetor para guardar o inverso
fraseInversa    = ''                    

# Percorrendo a frase recebida
for letra in range(len(frase1Junta)-1, -1, -1):  
    # PARAMENTRO:
        # 1 > len(fraseJunta)-1 -> faço isso pq as letras começam a ser armazenadas em 0 e não em 1, então preciso tirar 1 do tam total
        # 2 > -1                -> a primeira letra é zero, então ele vai até antes da primeira
        # 3 > -1                -> para ir voltando
    fraseInversa = (fraseInversa + frase1Junta[letra])

if (fraseInversa == frase2):
    print('A segunda frase é um palidromo da primeira')
else:
    print('A segunda frase NÃO é um palidromo da primeira')


# Para não utilizar o FOR, basta que eu use o seguinte comando:
#   fraseInversa = fraseJunta[ : :-1] 


