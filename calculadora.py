import math 
from rich import print

while True:
    def menu():
        print("[bold red] \n------- CALCULADORA --------[/bold red]")
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("5 - Potência")
        print("6 - Raiz quadrada")

        opcao = input("Escolha uma opção: ")

        if opcao in ["1", "2", "3", "4", "5"]:
            numero0 = float(input("Digite o primeiro número: "))
            numero1 = float(input("Digite o segundo número: "))

        if opcao == "1":
            somar(numero0, numero1)
        elif opcao == "2":
            subtrair(numero0, numero1)
        elif opcao == "3":
            multiplicar(numero0, numero1)
        elif opcao == "4":
            dividir(numero0, numero1)
        elif opcao == "5":
            potencia(numero0, numero1)
        elif opcao =="6":
            raiz(numero0, numero1)

        else:
            print("ERRO : Digite uma opção válida!")

    def somar(numero0, numero1):
        resultado = numero0 + numero1
        print(f"A soma dos números{numero0} e {numero1} é de: {resultado}")    
        
    def subtrair(numero0, numero1):
        resultado = numero0 - numero1 
        print(f"A subtração dos números {numero0} e {numero1} é de: {resultado}")

    def multiplicar(numero0, numero1):
        resultado = numero0 * numero1 
        print(f"A multiplicação dos números {numero0} e {numero1} é de: {resultado}")

    def dividir(numero0, numero1):
        resultado = numero0 / numero1
        print(f"A divisão dos números {numero0} e {numero1} é de {resultado}")

    def potencia(numero0, numero1):
        resultado = numero0 ** numero1
        print(f"Sendo {numero0} a base, e {numero1} o expoente, o resultado da pontecialização é de {resultado}.")

    def raiz(numero0, numero1):
        raiz_cubica0_math = math.sqrt(numero0)
        raiz_cubica1_math = math.sqrt(numero1)
        print(f"{raiz_cubica0_math} e {raiz_cubica1_math} ")

    menu()
