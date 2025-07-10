from datetime import datetime

def data_atual():
    return datetime.now().strftime("%d/%m/%Y")

def menu():
    print("""
Seja Bem-Vindo!
========================================
1 - DEPÓSITO
2 - SAQUE
3 - EXTRATO
4 - SAIR
========================================""")
    opcao = input("Selecione uma operação: ").strip()
    return opcao

def main():
    saldo = 0.00
    limite_saque_diario = 500.00
    extrato = ""
    quant_saque = 0.00
    LIMITE_SAQUES = 3

    while True:

        opcao = menu()
        
        if opcao == '1':
            try:
                valor = (input("\nInforme o valor que deseja depositar: R$ ")).replace(",",".")
                valor_float = float(valor)
                if valor_float > 0:
                    saldo += valor_float
                    extrato += f"{data_atual()}  |  Depósito  |  + R$ {valor_float:.2f}\n"
                    print("Depósito realizado com sucesso.")
                else:
                    print("Operação mal sucedida. Valor inválido.")    
            except ValueError:
                print("Operação mal sucedida. Tente novamente.") 

        elif opcao == '2':
            print("Você escolheu a opção SAQUE.")

        elif opcao == '3':
            print("\n==============EXTRATO=================")
            print(extrato if extrato else "Nenhuma movimentação.")
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("========================================")

        elif opcao == '4':
            print("\nObrigado por utilizar nossos serviços.")
            print("Saindo...\n")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
     