# Desafio de Projeto - Sistema Bancário em Python

## DIO (Digital Innovation One) - Santander 2025 - Back-End com Python

### Objetivo Geral:

Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.

### Desafio:

Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

### Operação de depósito:

Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

### Operação de saque:

O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

### Operação de extrato:

Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta.
Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:
1500.45 = R$ 1500.45.

### 📌 Funcionalidades:

- 💰 Depósito com validação de entrada;
- 🏦 Saque com limite de valor e número de operações diárias;
- 📄 Extrato com registro de todas as movimentações;
- 🔒 Reset automático do limite de saque a cada novo dia;
- 🧼 Limpeza automática da tela após cada operação.

### 🛠️ Tecnologias Utilizadas:

- Python 3
- Módulos padrão: `datetime`, `time`, `os`

### ▶️ Como Executar:

1. Clone o repositório:
   ```bash
   git clone https://github.com/ZvLuCaSvZ/sistema-bancario.git
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd sistema_bancario
   ```
3. Execute o script:
   ```bash
   python main.py
   ```

### Estrutura do Projeto:

```sistema-bancario/
sistema_bancario/
├── bank/
│ ├── init.py
│ ├── account.py                    # Contain the Account class
│ ├── menu.pyt                      # Contains the menu function
│
├── services/
│ ├── init.py
│ ├── bank_statement.py             # Contains the bank statement function
│ ├── transactions.py               # Contains the transaction functions (deposit, withdraw)
│
├── utils/
│ ├── init.py
│ ├── clear_screen.py               # Function to clear the console screen
│ ├── daily_reset_withdrawals.py    # Function to reset daily withdrawals
│ ├── date_today.py                 # Function to get today's date
│
├── .gitignore
├── main.py
├── README.md
```

### Melhorias Futuras:

✅ Armazenamento dos dados em arquivos

✅ POO (Programação Orientada a Objetos)

### Autor:

- Desenvolvido por: Lucas Semião Marques.
- GitHub: [ZvLuCaSvZ](https://github.com/ZvLuCaSvZ)

### Licença:

Este projeto é de código aberto e pode ser utilizado, modificado e distribuído livremente, desde que respeitadas as condições da licença MIT.

### Contribuições:

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para melhorias e correções.
