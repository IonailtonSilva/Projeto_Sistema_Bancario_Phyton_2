import textwrap


print("======= SEJA BEM VINDO A SUA CONTA ==========")
print("======== O QUE DESEJA FAZER HOJE?! ==========")


def menu():

    print("""

[1] - Depositar
[2] - Saque
[3] - Extrato
[4] - Novo Usuario
[5] - Nova Conta
[6] - Listar Usuarios                      
[7] - Sair

""")


def depositar(saldo, extrato, deposito):

    if deposito > 0:

        print(f"\n===== Seu depósito de: R${deposito: .2f}, foi realizado com sucesso!=====\n")

        saldo += deposito
        extrato += f"Você Efetuou Um Deposito de:R${deposito: .2f}\n"

    else:
        
        print("\n===== A OPERAÇÂO FALHOU, TENTE NOVAMENTE! =====\n")  

    return saldo, extrato


def sacar(saque, saldo, limite, extrato, quant_saques, limite_saques):

    
    if saque <= limite:

            print("\n===OPERAÇÃO REALIZADA COM SUCESSO! AGUARDE A CONTAGEM DAS CÉDULAS===\n")

    if saque > saldo:

            print("\n=====OPERACAO INVÁLIDA, SALDO INSUFICIENTE!=====\n")

    elif saque > limite:

            print("\n=====OPERACAO INVÁLIDA, LIMITE DE SAQUE EXCEDIDO!=====")

    elif quant_saques >= limite_saques:
        
            print("\n=====OPERACAO INVÁLIDA, LIMITE DE SAQUES DIARIOS EXCEDIDO!=====")

    elif saque > 0:

            saldo -= saque 
            extrato += f"Você realizou um saque de: R$ {saque:.2f} \n"
            quant_saques += 1
        

    else:

        print("=====OPERAÇAO INVÁLIDA, TENTE NOVAMENTE!=====")
    

    return saldo, extrato, 


def exibirExtrato(saldo, extrato):
     
    print("\nOK... Vamos Ao Seu Extrato!\n")
    print("=================Extrato====================\n")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("===========================================")


def novaConta(agencia, numeroConta, usuarios):

    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrarUsuario(cpf, usuarios)

    if usuario:
        print("\n\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numeroConta, "usuario": usuario}

    print("\n=== Usuário não encontrado, fluxo de criação de conta encerrado! ===")          


def novoUsuario(usuarios):

    print("Ok... Criando Um Novo Usuario")
    cpf = (input("Digite o Seu CPF: "))
    usuario = filtrarUsuario(cpf, usuarios)

    if usuario:
            print("\n=== Já existe usuário com esse CPF! ===")
            return
    
    nome = input("Digite Seu Nome: ")
    dataNascimento = input("digite sua data de nascimento (dd-mm-aa): ")
    endereco = input("Digite seu endereço(Rua,Nº - Bairro, cidade/UF): ")

    usuarios.append({"nome": nome, "data_nascimento": dataNascimento, "cpf": cpf, "endereco": endereco})

    print(f"\n=== Usuário criado com sucesso! ===")


def filtrarUsuario(cpf, usuarios):
        usuariosFiltrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
        return usuariosFiltrados[0] if usuariosFiltrados else None


def listarContas(contas):

    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():

    opcao = 0
    saldo = 0
    limite = 500
    extrato = ""
    quant_saques = 0
    limite_saques = 3
    usuarios = []
    contas = []
    agencia = "0001"

    while opcao != 7:

        menu()

        opcao = int(input("Selecione Uma Das Opçoes Acima: "))

        if opcao == 1:

            print("\nVoce Escolheu a Opção de Depósito!")

            deposito = float(input("\nOk!...Quanto deseja depositar?: "))

            print("\n")
   
            saldo, extrato = depositar(saldo, extrato, deposito)     

        elif opcao == 2:

            print("\nEntendi, Você Gostaria de Sacar!\n")

            saque = float(input("\nQuanto Deseja Sacar?:"))

            saldo, extrato = sacar(saque=saque, saldo=saldo, limite=limite, extrato=extrato, quant_saques=quant_saques, limite_saques=limite_saques)

        elif opcao == 3:

            exibirExtrato(saldo, extrato = extrato)

        elif opcao == 4:

            novoUsuario(usuarios)

        elif opcao == 5:

            print("Vamos Iniciar o Processo de Criação de Conta...")

            numeroConta = len(contas) + 1
            conta = novaConta(agencia, numeroConta, usuarios)

            if conta:
                contas.append(conta)  

        elif opcao == 6:

            listarContas(contas)    

        elif opcao == 7:
        
            print("\n==========SISTEMA FINALIZADO!===========")
            print("\n=============VOLTE SEMPRE!==============")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()