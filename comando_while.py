opcao = -1

while opcao != (0,1,2):
     
     opcao = int(input("[1] Sacar \n [2] Extrato \n [0] Sair:"))

     if opcao == 1:
          print("Sacando...")

     elif opcao == 2:
          print("Exibindo o seu extrato")

     else:
        print("Opção invalida")
        print("Obrigado por usar nosso sistema bancário") 