import Produto

class Ebook:
    def __init__(self, nome, preco, autor):
        self.nome = nome
        self.preco = preco
        self.autor = autor

    def AdicionarEntrada(self):
        print(f"Não é possível dar entrada no estoque de um E-Book, pois é um produto digital!")
        read = input()

    def AdicionarSaida(self):
        print(f"Adicionar vendas no E-Book {self.nome}")
        entrada = int(input("Digite a quantidade de vendas que você quer dar de entrada: "))

        # vagas += entrada

        print("Saida registrada.")
        read = input()

    def Exibir(self):
        print(f"Nome: {self.nome}\n"
              f"Autor: {self.autor}\n"
              f"Preço: {self.preco}\n"
              f"Vendas : --\n"
              f"======================")

