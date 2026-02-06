while True:
    comando = input("Digite 'sair' para encerrar o programa: ")
    if comando.lower() == 'sair':
        print("Encerrando o programa...")
        break
    else:
        print(f"Você digitou: {comando}")