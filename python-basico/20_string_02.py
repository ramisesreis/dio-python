nome = "Otávio"
idade = 7
profissao = "estudante"
linguagem = "Python"
saldo = 100.5096

print("Olá, me chamo %s, tenho %d anos, sou %s e estou aprendendo %s!" %
      (nome, idade, profissao, linguagem))

print("Olá, me chamo {0}, tenho {1} anos, sou {2} e estou aprendendo {3}!"
      .format(nome, idade, profissao, linguagem))

print(f"Olá, me chamo {nome}, tenho {idade} anos, sou {profissao} "
      f"e estou aprendendo {linguagem}!")

print(f"Olá, me chamo {nome}, tenho {idade} anos, sou {profissao} "
      f"e estou aprendendo {linguagem}! Meu saldo é R${saldo:.2f}.")