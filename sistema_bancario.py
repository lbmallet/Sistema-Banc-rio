import os

saldo = 2000
operacoes = []  # Lista para armazenar as operações
comando = ""
qtd_saque = 0
LIMITE_SAQUE = 3
VLR_LIMITE_SAQUE = 500

def deposito(valor, saldo_atual):
    if valor > 0:
        saldo_atual += valor
        operacoes.append(f"Depósitou = R${valor:.2f}\n")
        print('Saldo atual é R$', saldo_atual)
        return saldo_atual
    else:
        print('Valor precisa ser maior que 0')
        return saldo_atual

def sacar(valor, saldo_atual):
    global qtd_saque, LIMITE_SAQUE

    if qtd_saque < LIMITE_SAQUE and valor <= VLR_LIMITE_SAQUE and valor > 0 and valor <= saldo_atual:
        saldo_atual -= valor
        operacoes.append(f"Sacou = -R${valor:.2f}\n")
        print('Saldo atual é R$', saldo_atual)
    else:
        if qtd_saque >= LIMITE_SAQUE:
            print('Limite de quantidade de saques foi ultrapassado.')
        elif valor > VLR_LIMITE_SAQUE:
            print('Limite máximo de R$500,00 por saque.')
        else:
            print('Não será possível sacar o dinheiro por falta de saldo!')

    qtd_saque += 1

    return saldo_atual

while comando != 'q' and comando.title() != 'Sair':
    comando = input("""
        Qual a operação que deseja realizar? 
        [s] Sacar
        [d] Depositar
        [e] Extrato
        [q] Sair 
        """)

    if comando == 'd' or comando.title() == 'Depositar':
        os.system('cls' if os.name == 'nt' else 'clear')
        valor = float(input('Qual o valor deseja depositar? '))
        saldo = deposito(valor, saldo)

    elif comando == 's' or comando.title() == 'Sacar':
        os.system('cls' if os.name == 'nt' else 'clear')
        valor = float(input('Qual o valor deseja sacar? '))
        saldo = sacar(valor, saldo)

    elif comando == 'e' or comando.title() == 'Extrato':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n ================= EXTRATO ===================')
        if not operacoes:  # Verifica se não há operações
            print('Saldo atual é R$', saldo)
            print('\n Não foram realizadas movimentações!')
            print('\n =============================================')
        else:
            print('Operações realizadas desde o início do programa:')
            for operacao in operacoes:
                print(operacao)
            print('Saldo atual é R$', saldo)
            print('\n =============================================')
    else:
        print('Operação falhoou! O valor informado é invalido')
        
print('Volte Sempre')
