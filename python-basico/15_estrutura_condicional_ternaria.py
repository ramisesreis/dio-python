saldo = 2000
saque = 2500

status = "Saque autorizado utilizando cheque especial" if saque <= saldo + 1000 else "Saldo insuficiente"
print(status)
