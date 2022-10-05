import Produto


class Curso:
    def __init__(self, nome, preco, autor):
        self.nome = nome
        self.preco = preco
        self.autor = autor

    def AdicionarEntrada(self, vagas):
        print(f"Adicionar vagas no curso {self.nome}")
        entrada = int(input("Digite a quantidade de vagas quer dar de entrada: "))

        vagas += entrada

        print("Entrada registrada.")
        read = input()

    def AdicionarSaida(self):
        print(f"Consumir vagas no curso {self.nome}")
        entrada = int(input("Digite a quantidade de vagas que deseja consumir: "))

        # vagas -= entrada

        print("Saida registrada.")
        read = input()

    def Exibir(self):
        print(f"Nome: {self.nome}\n"
              f"Autor: {self.autor}\n"
              f"Preço: {self.preco}\n"
              f"Vagas : --\n"
              f"======================")
