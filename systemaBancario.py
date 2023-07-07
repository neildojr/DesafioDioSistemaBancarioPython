menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(imput("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é invalido")

    elif opcao == "s":
        valor = float(imput("Informe o valor do saque: "))

        execedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saquer = numero_saque >= LIMITE_SAQUES

        if execedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente")

        elif excedeu_limite:
            print("Operação falhou! O valor do saquer excedeu o limete")

        elif excedeu_saquer:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saque += 1
        
        else:
            print("Operação falhou! O valor informado é invalido")


    elif opcao == "e":
        print("\n============= Extrato ============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("====================================")

    
    elif opcao == "q":
        break

    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")