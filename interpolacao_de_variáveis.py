nome = "Edivaldo"

idade = 43

profissao = "Programador"

linguagem = "Python"

dados = {"nome":"Edivaldo","idade": 43}

saldo = 99.935879241

print("Olá me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome,idade,profissao,linguagem))

print(f"Olá me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

print("Olá me chamo {0}. Eu tenho {1} anos de idade, trabalho como {2} e estou matriculado no curso de {3}.".format (nome,idade,profissao,linguagem))

PI = 3.14159

print(f"Valor de PI: {PI:.2f}")

print(f"Valor de PI: {PI:10.2f}")

print("nome: %s idade: %d" % (nome,idade))

print("nome: {} idade: {}".format(nome,idade))

print("nome:{nome} idade:{idade}".format(**dados))

print(f"nome:{nome} idade:{idade}")

print(f"nome:{nome} idade:{idade} saldo: {saldo:16.2f}")