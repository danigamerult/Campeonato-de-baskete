
estoque = {}
def menu():
    print("========== MENU ==========")
    print("1 - Ver estoque")
    print("2 - Adicionar produto")
    print("3 - Remover produto")
    print("4 - Sair")
    print("==========================")
while True:
    menu()
    escolha = input("Digite sua opção: ")

    if escolha == "1":
        print("--- Estoque Atual ---")
        if not estoque:
            print("O estoque está vazio.")
        else:
            for nome, qtd in estoque.items():
                print(f"{nome} : {qtd} unidades")
        print()
    elif escolha == "2":
        nome = input("Nome do produto: ")
        quantidade = int(input("Quantidade: "))
        if nome in estoque:
            estoque[nome] += quantidade
        else:
            estoque[nome] = quantidade
        print(f"{quantidade} unidades de {nome} adicionadas!")
    elif escolha == "3":
        nome = input("Nome do produto: ")
        quantidade = int(input("Quantidade a remover: "))
        if nome in estoque:
            estoque[nome] -= quantidade
            if estoque[nome] <= 0:
                del estoque[nome]
                print(f"{nome} removido completamente do estoque.")
            else:
                print(f"{quantidade} unidades removidas de {nome}.")
        else:
            print("Produto não encontrado no estoque.")
    elif escolha == "4":
        print("Encerrando o programa... Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")
