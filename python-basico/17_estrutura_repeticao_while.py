opcao = 1

while opcao != 0:
    print('Menu de opções:')
    print('1 - Opção 1')
    print('2 - Opção 2')
    print('0 - Sair')

    opcao = int(input('Digite a opção desejada: '))

    if opcao == 1:
        print('Você escolheu a Opção 1')
    elif opcao == 2:
        print('Você escolheu a Opção 2')
    elif opcao == 0:
        print('Saindo do programa...')
    else:
        print('Opção inválida. Tente novamente.')