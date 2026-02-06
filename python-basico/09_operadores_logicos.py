saldo = 1000
saque = 200
limite = 500   
conta_especial = True

# AND = para que a condição seja verdadeira, todas as expressões precisam ser verdadeiras
# OR = para que a condição seja verdadeira, apenas uma das expressões precisa ser verdadeira    

exemplo_1 = saque >= saldo and saque <= limite or conta_especial and saldo >= saque
exemplo_2 = (saldo >= saque and saque <= limite) or conta_especial and saldo >= saque


print(exemplo_1)
print(exemplo_2)    


conta_normal_saldo_suficiente = saque >= saldo and saque <= limite 
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exemplo_3 = conta_normal_saldo_suficiente or conta_especial_com_saldo_suficiente

print(exemplo_3)
