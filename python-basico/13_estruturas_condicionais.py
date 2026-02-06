MAIOR_IDADE = 18
IDADE_MINIMA = 12

idade = int(input("Digite a sua idade: "))
if idade >= MAIOR_IDADE:
    print("Você é maior de idade.")
elif idade == IDADE_MINIMA:
    print("Você é adolescente.")
else:
    print("Você é menor de idade.") 
