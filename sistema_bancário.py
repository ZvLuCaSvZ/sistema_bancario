import os
import time
from datetime import datetime

# Definição das variáveis globais.
saldo = 0.00
quant_saque = 0
LIMITE_SAQUES = 3
limite_saque_diario = 500.00
data_do_ultimo_saque = None
extrato = ""

def limpar_tela():
    # Limpa o terminal de forma multiplataforma.
    os.system('cls' if os.name == 'nt' else 'clear')

def data_atual():
    # Retorna a data atual no formato dd/mm/yyyy.
    return datetime.now().strftime("%d/%m/%Y")

def resetar_saque_diario():
    global quant_saque, data_do_ultimo_saque, LIMITE_SAQUES
    # Se o último saque foi em outro dia, zera o contador de saques.
    data_hoje = data_atual()
    if data_do_ultimo_saque != data_hoje:
        quant_saque = 0
        data_do_ultimo_saque = data_atual()

def menu():
    # Exibição do menu formatado e leitura da opção do usuário.
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
    except ValueError:
        print("Operação mal sucedida. Tente novamente.")

def saque():
    global saldo, limite_saque_diario, extrato, quant_saque, LIMITE_SAQUES

    resetar_saque_diario()
    if quant_saque >= LIMITE_SAQUES:
        print("Operação não autorizada. Limite de saques diário excedido.")
        return
    
    try:
        valor_saque = input("\nInforme o valor que deseja sacar: R$ ").replace(",",".")
        valor_saque_float = float(valor_saque)
        if valor_saque_float < 0:
            print("Valor de saque inválido.")
        else:   
            if valor_saque_float > saldo:
                print("Saldo indisponível para realizar essa operação. ")
            elif valor_saque_float > limite_saque_diario:
                print("Saque excedeu o limite diário permitido.")
            else:
                saldo -= valor_saque_float
                extrato += f"{data_atual()}  |  SAQUE     |  - R$ {valor_saque_float:.2f}\n"
                quant_saque += 1
                print("Saque realizado com sucesso.")
    except ValueError:
        print("Operação mal sucedida. Tente novamente.")

def ver_extrato():
    # Retorna o extrato formatado.
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
            limpar_tela()

        elif opcao == '2':
            saque()
            time.sleep(2)
            limpar_tela()

        elif opcao == '3':
            ver_extrato()
            limpar_tela()
            
        elif opcao == '4':
            print("\nSaindo...")
            print("Obrigado por utilizar nossos serviços.\n")
            break

        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(2)
            limpar_tela()

if __name__ == "__main__":
    main()
     