# 🏦 Sistema Bancário em Python

Este é um projeto de sistema bancário simples desenvolvido em Python com o objetivo de praticar o uso de **funções**, **listas**, e **dicionários**. O sistema permite operações como depósito, saque, exibição de extrato, cadastro de usuários e contas, e listagem de contas criadas.

---

## 🚀 Funcionalidades

* [x] **Depósito**
* [x] **Saque com limite diário e por operação**
* [x] **Extrato com saldo e histórico de operações**
* [x] **Cadastro de novo usuário com CPF único**
* [x] **Criação de conta corrente vinculada ao usuário**
* [x] **Listagem de contas cadastradas**
* [ ] (Opcional) Listagem de usuários cadastrados

---

## 📁 Estrutura do Projeto

* `menu()` – Exibe o menu principal
* `depositar()` – Realiza depósitos
* `sacar()` – Realiza saques com validação de saldo e limite
* `exibir_extrato()` – Exibe extrato e saldo
* `criar_usuario()` – Cadastra novo usuário com CPF único
* `filtrar_usuario()` – Localiza usuário por CPF
* `criar_conta()` – Cria conta bancária vinculada a um CPF já cadastrado
* `listar_contas()` – Mostra todas as contas existentes

---

## 📋 Pré-requisitos

* Python 3.7 ou superior instalado
* Editor de código como VS Code, PyCharm ou até mesmo o IDLE

---

## ▶️ Como Executar

1. Clone este repositório ou copie o código para sua máquina.
2. Execute o arquivo `.py` com o Python:

```bash
python sistema_bancario.py
```

3. Utilize o menu no terminal para interagir com o sistema.

---

## 💠 Melhorias Futuras (Sugestões)

* Validação do formato do CPF (11 dígitos, apenas números)
* Armazenamento de dados em arquivo (JSON ou banco de dados)
* Interface gráfica com Tkinter ou PyQt
* Integração com SQLite para persistência
* Login com autenticação por CPF

---

## 📄 Licença

Este projeto é apenas para fins educacionais e não possui licença de uso comercial.

---

## 🧓‍♂️ Autor

**Louvensdad Constantin**
Desenvolvedor em formação | Análise e Desenvolvimento de Sistemas
