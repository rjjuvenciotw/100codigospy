tarefas = []

def create_list():
    """Adiciona uma tarefa à lista."""
    tarefa = input("Digite a nova tarefa: ")
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

def remover_tarefa():
    """Remove uma tarefa da lista."""
    if not tarefas:
        print("Não há tarefas a fazer! O_o")
        return

    exibir_tarefas()
    try:
        indice = int(input("Digite o número da tarefa a remover: ")) - 1  # Ajuste para índice baseado em 0
        if 0 <= indice < len(tarefas):
            tarefa_removida = tarefas.pop(indice)
            print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
        else:
            print("Número de tarefa inválido. Digite um número válido.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

def exibir_tarefas():
    """Exibe as tarefas pendentes."""
    if not tarefas:
        print("Não há tarefas pendentes.")
    else:
        print("\nTarefas Pendentes:")
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")
        print("")

def menu():
    """Exibe o menu principal e gerencia a interação com o usuário."""
    while True:
        print("++++++++ Gerenciador de Tarefas ++++++++")
        print("1. Adicionar tarefa")
        print("2. Remover tarefa")
        print("3. Exibir tarefas")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            create_list()
        elif escolha == '2':
            remover_tarefa()
        elif escolha == '3':
            exibir_tarefas()
        elif escolha == '4':
            print("Saindo do programa... Até mais!")
            break
        else:
            print("Opção inválida. Digite um número de 1 a 4.")

# Executar o programa
menu()
