saldo = 0
limite = 0
opcao = 0
extrato = ""

while True:
    print ("[1]DEPOSITAR\n[2]SACAR\n[3]EXTRATO\n[4]SAIR")
    opcao = int(input("Digite o número da operação: "))
    print (" ")

    if opcao == 1:
        deposito = float(input("Valor de deposito: R$"))
        if deposito > 0:
            saldo += deposito  
            extrato += f"\nDeposito: R${deposito:.2f}"
            print (" ")
            
        else:
            print ("FALHA NA OPERAÇÃO = Não são permitidos valores negativos")
            print (" ")

    elif opcao == 2:        
        saque = float(input("Valor de saque: R$"))
        if saque < saldo:
            if saque > 0:
                if saque <= 500:
                    if limite < 3:
                        saldo -= saque
                        limite += 1
                        extrato += f"\nSaque: R${saque:.2f}"
                        print(" ")
                    else:
                        print("FALHA NA OPERAÇÃO = Excedeu o limite de 3 saques")
                        print(" ")
                else:
                    print("FALHA NA OPERAÇÃO = Limite de saque: R$500")
                    print(" ")
            else:
                print("FALHA NA OPERAÇÃO = Não são permitidos valores negativos")
                print(" ")
        else:
            print("FALHA NA OPERAÇÃO = Saldo insuficiente!")
            print(" ")

    elif opcao == 3:
        print(" ")
        print(" EXTRATO ".center(35,"▬"))
        print("\nSem movimentações" if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("▬".center(35,"▬"))
        print(" ")

    elif opcao == 4:
        confirmar_sair = int(input("Tem certeza que deseja sair?\n[1]Sair  [2]Continuar:  "))
        if confirmar_sair == 1:
            print(" ")
            break
        else:
            print(" ")

    else: 
        print("operação invalida")
        print(" ")


print ("Obrigado por sua visita ☺ ")