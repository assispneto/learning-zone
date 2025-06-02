frase = str('O Assis é lindo demais')

# Fatiamento
print(frase[3])         # Mostra a posicao 3
print(frase[3:5])       # Mostra do 3 ao 5 (eliminando o que aparece no 5)
print(frase[1:10:2])    # Mostra do 1 ao 10 pulando de 2 em 2
print(frase[:6])        # Mostra do inicio até o 5 (começando do caractere 0)
print(frase[8:])        # Mostra tudo do caractere 8 até o último
print(frase[2::3])      # Inicia do 2 até o final pulando de 3 em 3

# Análise
len(frase)                      # Mostra o tamanho da frase
frase.count('s')                # Conta quantas vezes o 's' aparece
frase.count('s', 2, 6)          # Conta quantas vezes o 's' aparece da posição 2 até a 6
frase.find('is')                # Mostra onde aparece 'is'
lindoOuFeio = 'lindo' in frase  # Retorna se existe a palavra 'lindo' dentro da frase

# Transformação
trocaFrase      = frase.replace('Assis', 'Neto')    # Onde tem 'Assis' ele troca por 'Neto'
fraseMaiuscula  = frase.upper()                     # Minusculo -> Maiusculo
fraseMinuscula  = frase.lower()                     # Maiusculo -> Minusculo
fraseCapitalize = frase.capitalize()                # Só o primeiro caractere da frase fica maiusculo
fraseTite       = frase.title()                     # Todas as palavras iniciam com uma maiuscula
fraseStrip      = frase.strip()                     # Remove os espacos inuteis no inicio e final da string
fraseRStrip     = frase.rsplit()                    # Remove espacos do lado DIREITO (final da frase)
fraseLStrip     = frase.lstrip()                    # Remove espacos do lado ESQUERDA (inicio da frase)

# Divisão
divideFrase    = frase.split()
# Divide as palavras na frase observando os espacos entre elas,
# numerando cada letra dentro da palavra e numerando cada palavra
# CARACTERE DE SPLIT -> por padrão o espaço

# Junção
juntaFrase      = ''.join(frase)
# Junto as frases que foram divididas colocando um '-' entre elas


