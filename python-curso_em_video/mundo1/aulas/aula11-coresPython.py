# Codigos ASCII

# Comando base para formatação de cor:
# \033(style:text:backm (o back é o valor, e o 'm' é uma letra que realmente precisa ser acionada

# style -> estilo do txt; negrito, itálico ou normal
# 0=nada | 1=negrito | 4=sublinhado | 7=inverte as conf entre txt e fundo
#-------------------------------------------------------------------------------------
# text -> cor do que será escrito
# 30=branco | 31=verm | 32=verde | 33=amare | 34=azul | 35=roxo | 36=ciano | 37=cinza
#-------------------------------------------------------------------------------------
# back -> o fundo do texto
# 40=branco | 41=verm | 42=verde | 43=amare | 44=azul | 45=roxo | 46=ciano | 47=cinza

# Códigos para testar o código
# \033[0:30:41m
# \033[4:33:44m
# \033[1:35:43m
# \033[30:42m
# \033[m          (Desfaz as configurações de style)
# \033[7:30m

print('\033[0:30:41mOlá, mundo!!! \033[m')
print('\033[4;33;44mOlá, mundo!!! \033[m')
print('\033[1;35;43mOlá, mundo!!! \033[m')
print('\033[30;42mOlá, mundo!!! \033[m')
print('\033[mOlá, mundo!!! \033[m')
print('\033[7:30mOlá, mundo!!! \033[m')
