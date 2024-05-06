
# excedeu_limite_transferencia = numero_transferencias >= LIMITE_TRANSFERENCIAS
# elif opcao == "t":
#             if excedeu_limite_transferencia:

#                 print("A quantidade de transferências excedeu o limite")

#             else:

#                 numero_conta = int(input("\nInforme o número da conta: "))
#                 agencia = int(input("\nInforme o número da agência: "))
#                 valor = float(input("\nInforme o valor da transferência: "))

#                 if valor > 0 and saldo >= valor:

#                     saldo -= valor

#                     print("\n=================== TRANSFERÊNCIA ===================")
#                     print(f"\nFoi transferido o valor de: R$ {valor:.2f}")
#                     print(f"\nPara a conta: {numero_conta} - {agencia}")
#                     print(f"\nFoi transferido: R$ {valor:.2f}")
#                     print("\n=====================================================")

#                 else:

#                     print("\nSaldo insuficiente")