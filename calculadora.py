
import math 

numero0 = float(input("Digite um primeiro número: "))
numero1 = float(input("Digite um segundo número: "))

def menu(): 

    print("/n-------Calculadora--------")
    print("1 - para somar")
    print("2 - para subtrair")
    print("3 - para multiplicar")
    print("4 - para dividir")
    print("5 - para potência")
    print("6 - para raíz quadrada")

    opcao = input("Escolah uma opção: ")

    if opcao == "1":
        somar()
    elif opcao == "2":
        subtrair()
    elif opcao == "3":
        multiplicar()
    elif opcao == "4":
        dividir()
    elif opcao == "5":
        potencia()
    elif opcao =="6":
        raiz()

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
    print("Sendo {numero0} a base, e {numero1} o expoente, o resultado da pontecialização é de {resultado}.")

def raiz(numero0, numero1):
    raiz_cubica0_math = math.sqrt(numero0)
    raiz_cubica1_math = math.sqrt(numero1)
    print("{raiz_cubica0_math} e {raiz_cubica1_math} ")

menu()

