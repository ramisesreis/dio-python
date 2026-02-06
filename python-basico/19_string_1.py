nome = "Otávio"

print(nome.upper())  # Deixa todas as letras maiúsculas
print(nome.lower())  # Deixa todas as letras minúsculas
print(nome.title())  # Deixa a primeira letra de cada palavra maiúscula

texto = "   Olá, mundo!   "

print(texto + ".")  # Imprime o texto com os espaços em branco
print(texto.strip() + ".")  # Remove os espaços em branco no início e no final
print(texto.lstrip() + "!")  # Remove os espaços em branco no início
print(texto.rstrip() + ".")  # Remove os espaços em branco no final   


menu = "Python"
# Centraliza o texto em uma largura de 20 caracteres, preenchendo
# com '-'
print(menu.center(20, "-"))
# Alinha o texto à esquerda em uma largura de 20 caracteres,
# preenchendo com '-'
print(menu.ljust(20, "-"))

# Adiciona '-' entre cada caractere do texto
print("-".join(menu))

for letra in menu:
    print(letra, end="-")  
print()  # Imprime cada letra do texto seguida de '-'