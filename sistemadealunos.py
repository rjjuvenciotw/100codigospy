#notas sistem


alunos = []
notas1 = []
notas2 = []
notas3 = []
notas4 = []

def Menu():
    
    opcao = input(str("Escolha uma das opções: "))
    print("(0) Para, Ver tabela.")    
    print('(1) Para, Adcionar alunos.')
    print("(2) Para, Remover Aluno da Tabela.")
    print("(3) Para, Adcionar notas.")
    print("(4) Para, Limpar toda a Tabela.")

    if opcao == "1":
        Adcionar_Alunos()
    elif opcao == '2':
        Remove_Aluno()
    elif opcao == "3":
        Adcionar_Nota()
    elif opcao == "4":
        Limpar_Tabela()
    elif opcao == "0":
        Ver_Tabela()
    else:
        print("X - Escolha um opção válida.")


def Adcionar_Alunos(alunos):
    while True:
        aluno = input(str("Digite o nome do aluno: "))
        aluno.append = alunos
        print("Aluno adcionado com sucesso, precione x caso queira sair")
        if aluno == 'x':
            break
    Menu()

def Remove_Aluno():
    Ver_Tabela()
    while True:
        try:
            posicao = input(int("Digite o número do aluno que deseja remover: "))
            alunos.remove = posicao
        except: ValueError
            f'Digite um valor válido para remover!'
        
    
def Ver_Tabela():

Menu()
