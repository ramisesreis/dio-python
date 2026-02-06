texto = input("Digite um texto: ")
VOGAIS = "AEIOUaeiou"

for letra in texto:
    if letra in VOGAIS:
        print(letra, end=" ")
    else:
        print("Consoante", end=" ")

# range(stop) - Gera uma sequência de números de 0 até stop - 1.
# range(start, stop) - Gera uma sequência de números de start até stop - 1
# range(start, stop, step) - Gera uma sequência de números de start até stop - 1, incrementando por step.   
  
range(10)  # Gera os números de 0 a 9
range(1, 10)  # Gera os números de 1 a 9        

for numero in range(0, 51, 5):
    print(numero, end=" ")  # Imprime os números de 0 a 50, incrementando por 5


for numero in range(10, 0, -1):
    if numero == 5:
        break  # Interrompe o loop quando o número é 5 
    print(numero, end=" ")  # Imprime os números de 10 a 1

for numero in range(1, 11):
    if numero % 2 == 0:
        continue  # Pula o número se for par
    print(numero, end=" ")  # Imprime apenas os números ímpares 