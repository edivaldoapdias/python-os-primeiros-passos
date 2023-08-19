MAIOR_IDADE = 18

IDADE_ESPECIAL = 17

idade = int(input("Qual é sua idade: "))

if idade >= MAIOR_IDADE:

    print("Maior de idade, pode tirar sua CNH")

elif idade == IDADE_ESPECIAL:

    print("Pode fazer aulas especiais, mas não as aulas práticas")   

else:

    print("Ainda não pode tirar sua CNH")