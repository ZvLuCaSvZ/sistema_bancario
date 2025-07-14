import os
import time
from datetime import datetime

# DEFINIÇÃO DAS VARIÁVEIS GLOBAIS.
saldo = 0.00
quant_saque = 0
LIMITE_SAQUES = 3
limite_saque_diario = 500.00
extrato = ""

# FUNÇÃO PARA COLETAR DATA ATUAL.
def data_atual():
    return datetime.now().strftime("%d/%m/%Y")

# FUNÇÃO DE MENU E COLETAR OPÇÃO DO USÚARIO.
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

# DEFINIÇÃO DA OPERAÇÃO DE DEPÓSITO.
def deposito():
    global saldo, extrato

    try:
        valor = (input("\nInforme o valor que deseja depositar: R$ ")).replace(",",".")
        valor_deposito_float = float(valor)
        if valor_deposito_float > 0:
            saldo += valor_deposito_float
            extrato += f"{data_atual()}  |  DEPÓSITO  |  + R$ {valor_deposito_float:.2f}\n"
            print("Depósito realizado com sucesso.")
        else:
            print("Operação mal sucedida. Valor inválido.")    
    except:
        print("Operação mal sucedida. Tente novamente.")

#DEFINIÇÃO DA OPERAÇÃO SAQUE:
def saque():
    global saldo, limite_saque_diario, extrato, quant_saque, LIMITE_SAQUES

    try:
        valor_saque = input("Informe o valor que deseja sacar: R$ ").replace(",",".")
        valor_saque_float = float(valor_saque)
        if valor_saque_float < 0:
            print("Valor de saque inválido.")
        else:   
            if valor_saque_float > saldo:
                print("Saldo indisponível para realizar essa operação. ")
            elif valor_saque_float > limite_saque_diario:
                print("Saque excedeu o limite diário permitido.")
            elif quant_saque >= LIMITE_SAQUES:
                print("Não foi possível realizar a operação. Limite de saques diário excedido.")
            else:
                saldo -= valor_saque_float
                extrato += f"{data_atual()}  |  SAQUE  |  - R$ {valor_saque_float:.2f}\n"
                quant_saque += 1
                print("Saque realizado com sucesso.")
    except:
        print("Operação mal sucedida. Tente novamente.")

# DEFINIÇÃO DA OPERAÇÃO EXTRATO:
def exibicao_extrato():
    global saque, extrato

    print("\n==============EXTRATO=================")
    print(extrato if extrato else "Nenhuma movimentação.")
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("========================================")
    input("Pressione Enter para sair...")

def main():
    while True:
        opcao = menu()
        
        if opcao == '1':
            deposito()
            time.sleep(2)
            os.system('cls')

        elif opcao == '2':
            saque()
            time.sleep(2)
            os.system('cls')

        elif opcao == '3':
            exibicao_extrato()
            os.system('cls')
            
        elif opcao == '4':
            print("\nObrigado por utilizar nossos serviços.")
            print("Saindo...\n")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
     