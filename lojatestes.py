produtos = []

class Produto:

    def __init__(self,nome,preco,Cbarras)
    self.nome = nome 
    self.preco = preco
    self.codigo = codigo

    def __str__(self):
        # Retorna uma string personalizada para mostrar o produto
        return f"[{self.preco}] {self.nome} - R${self.codigo}"

class Carrinho:
    def __init__(self):
        self.itens = [] #lista vazia de produtos.

    def adcionar(self, produto)
        self.itens.append(produto)
        print(f"Produto, {produto.nome} adcionado no  carrinho!")
    
    def remover(self, produto)
        for produto in self.intes:
            if produto.codigo == codigo:
                self.intes.remove(produto)
                print(f"o produto," {produto.nome} "Foi removido com sucesso!")
            else
                f"produto não encontrado"

    def vizualizar(self, produto)
    if not self.itens:
            print("🛒 O carrinho está vazio.")
        else:
            print("🛍️ Produtos no carrinho:")
            total = 0  # Inicializa o total da compra
            for produto in self.itens:
                print(f"- {produto}")  # Exibe cada produto usando o __str__
                total += produto.preco
            print(f"💰 Total: R${total:.2f}")  # Mostra o valor total



    def finalizar()
        try 
                


        except not seld.itens
                print("Carrinho está vazio")














    def finalizar_compra(self):
        # Finaliza a compra, esvaziando o carrinho
        if not self.itens:
            print("⚠️ Carrinho vazio. Adicione produtos antes de finalizar.")
        else:
            self.visualizar()  # Mostra o resumo da compra
            print("🎉 Compra finalizada com sucesso!")
            self.itens.clear()  # Esvazia o carrinho após compra


# Define a classe Loja, que gerencia o estoque e o carrinho
class Loja:
    def __init__(self):
        # Cria uma lista para armazenar os produtos disponíveis
        self.estoque = []
        # Cria um objeto Carrinho para o cliente
        self.carrinho = Carrinho()

    def cadastrar_produto(self, codigo, nome, preco):
        # Cria um novo produto e adiciona ao estoque
        produto = Produto(codigo, nome, preco)
        self.estoque.append(produto)
        print(f"📦 Produto '{nome}' cadastrado com sucesso.")

    def listar_produtos(self):
        # Mostra todos os produtos cadastrados no estoque
        if not self.estoque:
            print("📭 Nenhum produto cadastrado.")
        else:
            print("📋 Produtos disponíveis:")
            for produto in self.estoque:
                print(f"- {produto}")  # Usa o __str__ do produto

    def buscar_produto(self, codigo):
        # Busca um produto no estoque com base no código
        for produto in self.estoque:
            if produto.codigo == codigo:
                return produto  # Retorna o produto encontrado
        return None  # Retorna None se não encontrar

    def menu(self):
        # Exibe um menu interativo no terminal
        while True:
            print("\n--- MENU ---")
            print("1 - Listar produtos")
            print("2 - Adicionar produto ao carrinho")
            print("3 - Remover produto do carrinho")
            print("4 - Visualizar carrinho")
            print("5 - Finalizar compra")
            print("6 - Sair")
            escolha = input("Escolha uma opção: ")

            # Ações baseadas na escolha do usuário
            if escolha == "1":
                self.listar_produtos()
            elif escolha == "2":
                codigo = input("Digite o código do produto: ")
                produto = self.buscar_produto(codigo)
                if produto:
                    self.carrinho.adicionar(produto)
                else:
                    print("❌ Produto não encontrado.")
            elif escolha == "3":
                codigo = input("Digite o código do produto para remover: ")
                self.carrinho.remover(codigo)
            elif escolha == "4":
                self.carrinho.visualizar()
            elif escolha == "5":
                self.carrinho.finalizar_compra()
            elif escolha == "6":
                print("👋 Saindo da loja...")
                break
            else:
                print("⚠️ Opção inválida.")


# Ponto de entrada do programa
if __name__ == "__main__":
    # Cria um objeto Loja
    loja = Loja()
    
    # Cadastra alguns produtos iniciais no estoque
    loja.cadastrar_produto("001", "Mouse Gamer", 150.00)
    loja.cadastrar_produto("002", "Teclado Mecânico", 300.00)
    loja.cadastrar_produto("003", "Headset", 200.00)
    
    # Inicia o menu interativo
    loja.menu()
