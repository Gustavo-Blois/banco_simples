operacao = None
deposito = 0
saldo = 0
extrato = """"""
n_saques = 0
valor_de_saque = 0
while(operacao != 0):
    operacao = int(input("Insira [1] para depositar\nInsira [2] para sacar\nInsira [3] para exibir o extrato\nInsira [0] para sair\n"))
    match operacao:
        case 1:
            deposito = int(input("Insira o valor de depósito: "))
            if deposito > 0:
                saldo += deposito
                extrato += f"""Quantia de {deposito} adicionada ao saldo da conta\n"""
            else:
                print("valor de depósito inválido")
        case 2:
            if n_saques < 3:
              valor_de_saque = int(input("Insira o valor de saque: "))
              if valor_de_saque < saldo and valor_de_saque > 0:
                  n_saques += 1
                  saldo -= valor_de_saque
                  extrato += f"""Quantia de {valor_de_saque} removida do saldo da conta\n"""
              else:
                  print("valor inválido")
            else:
                print("você não pode mais realizar saques hoje")
        case 3:
            print(extrato + f"""\nSeu saldo atual é {saldo}\n""")
        case 0:
            break
        case _:
            print("operação inválida")