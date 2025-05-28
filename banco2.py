import textwrap

# Base de dados
usuarios = []
contas = []

def menu():
    return input(textwrap.dedent("""
    \n===== MENU =====
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Novo Usuário
    [5] Nova Conta
    [6] Listar Contas
    [q] Sair
    => Escolha uma opção: """))

# Funções do sistema bancário
def depositar(saldo, extrato, valor):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Valor inválido para depósito.")
    return saldo, extrato

def sacar(*, saldo, extrato, valor, limite, numero_saques, limite_saques):
    if numero_saques >= limite_saques:
        print("Limite diário de saques atingido.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    elif valor > limite:
        print(f"O valor do saque excede o limite de R$ {limite:.2f}.")
    elif valor <= 0:
        print("Valor inválido para saque.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n=========== EXTRATO ===========")
    print("Nenhuma movimentação." if not extrato else extrato)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("===============================")

# Funções para usuários e contas
def criar_usuario():
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf)

    if usuario:
        print("Já existe um usuário com esse CPF!")
        return

    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (logradouro, número - bairro - cidade/UF): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia="0001"):
    cpf = input("Informe o CPF do titular da conta: ")
    usuario = filtrar_usuario(cpf)

    if not usuario:
        print("Usuário não encontrado. Cadastre primeiro o usuário.")
        return

    numero_conta = len(contas) + 1
    contas.append({
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario
    })
    print(f"Conta criada com sucesso! Agência: {agencia}, Conta: {numero_conta}")

def listar_contas():
    for conta in contas:
        linha = f"""
        Agência: {conta['agencia']}
        Conta: {conta['numero_conta']}
        Titular: {conta['usuario']['nome']}
        """
        print(textwrap.dedent(linha))

# Inicialização de variáveis principais da conta corrente
saldo = 0
extrato = ""
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3

# Loop principal
while True:
    opcao = menu()

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: R$ "))
        saldo, extrato = depositar(saldo, extrato, valor)

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: R$ "))
        saldo, extrato, numero_saques = sacar(
            saldo=saldo,
            extrato=extrato,
            valor=valor,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES
        )

    elif opcao == "3":
        exibir_extrato(saldo, extrato)

    elif opcao == "4":
        criar_usuario()

    elif opcao == "5":
        criar_conta()

    elif opcao == "6":
        listar_contas()

    elif opcao == "q":
        print("Encerrando o sistema. Obrigado!")
        break

    else:
        print("Opção inválida. Tente novamente.")

4