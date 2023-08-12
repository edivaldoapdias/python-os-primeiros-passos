saldo = 1000
saque = 250
limite = 200
conta_especial = True

print(True and True and True)
print(True and False and True)
print(False and False and False)
print(True or True or True)
print(True or False or False)
print(False or False or False)

print(saldo>=saque and saque<=limite or conta_especial and saldo>=saque)

print((saldo>=saque and saque<=limite) or (conta_especial and saldo>= saque))

conta_normal_com_saldo_suficiente = saldo>=saque and saque<=limite 
conta_especial_com_saldo_suficiente = conta_especial and saldo>= saque

exp_1 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente

print(exp_1)
