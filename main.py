def Listagem():
    i = 0
    for produto in produtos:
        print(f"ID: {i}")
        i += 1


def Remover():
    Listagem()
    id = int(input("Digite o ID do elemento que você quer "))
    if (id >= 0) and (id < len(produtos)):
        produtos.remove(id)


produtos = []

escolheuSair = False

while not escolheuSair:
    print("Sistema de Estoque\n"
          "1-Listar\n2-Adicionar\n3-Remover\n4-Registrar Entrada\n5-Registrar Saída\n6-Sair")

    opcao = int(input("Digite a opção que deseja: "))

    if opcao == 1:
        Listagem()

    elif opcao == 2:
        Remover()

    elif opcao == 3:
        pass

    elif opcao == 4:
        pass

    elif opcao == 5:
        pass

    elif opcao == 6:
        escolheuSair = True
