import textwrap

def menu():

    menu = """\n
    ======================== MENU ========================
        [d]\tDepositar
        [s]\tSacar
        [e]\tExtrato
        #[t]\tTransferência
        [nc]\tNova Conta
        [lc]\tListar Contas
        [nu]\tNovo Usuário 
        [q] \tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):

    if valor > 0:

        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\nDepósito realizado com sucesso!")
    
    else:

        print("\nO valor informado é inválido")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:

        print("\nSaldo insuficiente!")

    elif excedeu_limite:

        print("O valor do saque excede o limite")

    elif excedeu_saques:

        print("Número máximo de saques excedido")

    elif valor > 0:

        saldo -= valor
        extrato -= f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\nSaque realizado com sucesso!")

    else:

        print("\nO valor informado é inválido")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):

    print("\n====================== EXTRATO ======================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("\n=====================================================")

def criar_usuario(usuarios):

    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:

        print("\nJá existe um usuário com este CPF")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o seu endereço (logradouro, nº - bairro - cidade/sigla estado): ")

    usuarios.append({"nome":nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso")

def filtrar_usuario(cpf, usuarios):

    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado, processo finalizado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta["agencia"]}
            C/C:\t\t{conta["numero_conta"]}
            Titular:\t{conta["usuario"]["nome"]}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():

    LIMITE_SAQUES = 3
    #LIMITE_TRANSFERENCIAS = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    numero_transferencias = 0
    usuarios = []
    contas = []
    #numero_conta = 1

    while True:

        opcao = menu()

        if opcao == "d":

            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato) 

        elif opcao == "s":

            valor = float(input("Informe o valor do saque: "))
            saldo, extrato == sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":

            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":

            criar_usuario(usuarios)

        elif opcao == "nc":

            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                #numero_conta += 1

        elif opcao == "lc":

            listar_contas(contas)

        elif opcao == "q":

            break

        else:

            print("Operação inválida! Por favor, selecione uma opção presente na lista")

main()
