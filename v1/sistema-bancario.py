menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [t] Transferência
    [q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
numero_transferencias = 0
LIMITE_SAQUES = 3
LIMITE_TRANSFERENCIAS = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":

        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:

            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else:
            
            print("O valor informado é inválido. Tente novamente")
    
    elif opcao == "s":

        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            
            print("Você não tem saldo suficiente")
        
        elif excedeu_limite:

            print("O valor do saque excede o limite")

        elif valor > 0:

            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:

            print("O valor informado é inválido")

    elif opcao == "e":

        print("\n====================== EXTRATO ======================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n=====================================================")
    
    elif opcao == "t":

        excedeu_limite_transferencia = numero_transferencias >= LIMITE_TRANSFERENCIAS

        if excedeu_limite_transferencia:

            print("A quantidade de transferências excedeu o limite")
        
        else:

            numero_conta = int(input("\nInforme o número da conta: "))
            agencia = int(input("\nInforme o número da agência: "))
            valor = float(input("\nInforme o valor da transferência: "))

            if valor > 0 and saldo >= valor:

                saldo -= valor

                print("\n=================== TRANSFERÊNCIA ===================")
                print(f"\nFoi transferido o valor de: R$ {valor:.2f}")
                print(f"\nPara a conta: {numero_conta} - {agencia}")
                print(f"\nFoi transferido: R$ {valor:.2f}")
                print("\n=====================================================")

            else:

                print("\nSaldo insuficiente")

    elif opcao == "q":

        break

    else:

        print("Operação inválida! Por favor, selecione uma opção presente na lista")