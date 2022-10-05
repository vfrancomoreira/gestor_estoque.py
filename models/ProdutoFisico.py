import Produto

class ProdutoFisico():
    def __init__(self, nome, preco, frete):
        self.nome = nome
        self.preco = preco
        self.frete = frete

    def AdicionarEntrada(self):
        print(f"Adicionar entrada no estoque do produto {self.nome}")
        entrada = int(input("Digite a quantidade que você quer dar de entrada: "))

        # estoque += entrada

        print("Entrada registrada.")

        read = input()

    def AdicionarSaida(self):
        print(f"Adicionar saída no estoque do produto {self.nome}")
        entrada = int(input("Digite a quantidade que você quer dar baixa: "))

        # estoque -= entrada

        print("Saida registrada.")
        read = input()

    def Exibir(self):
        print(f"Nome: {self.nome}\n"
              f"Preço: {self.preco}\n"
              f"Frete: {self.frete}"
              f"Estoque : --\n"
              f"======================")
