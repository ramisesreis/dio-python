conta_normal = True 
conta_universitaria = False

saldo = 3000
saque = 3500
cheque_especial = 1000

if conta_normal:
    if saque <= saldo:
        print("Saque autorizado")
    elif saque <= saldo + cheque_especial:
        print("Saque autorizado utilizando cheque especial")
    else:
        print("Saldo insuficiente")
elif conta_universitaria:
    if saque <= saldo:
        print("Saque autorizado")
    else:
        print("Saldo insuficiente")

