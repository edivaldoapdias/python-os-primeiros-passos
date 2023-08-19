CONTA_NORMAL = False
CONTA_UNIVERSITARIA = False

saldo = 2000
saque = 500
cheque_especial = 450

if CONTA_NORMAL:

    if saldo >= saque:
        print("Saque realizado com sucesso!!")

    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com o uso do cheque especial")

    else:
        print("Não foi possível realizar o saque")

elif CONTA_UNIVERSITARIA:
 if saldo >= saque:
        print("Saque realizado com sucesso")

 else:
        print("Saldo Insuficiente")

else:
        print("Sistema não reconhecido")           

  
    

