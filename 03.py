#Peça um número ao usuário e informe se
# ele é par ou ímpar.

while True:
    num = int(input("Digite um número: "))

    if num % 2 == 1:
        print(f"{num} é impar!")

    else:
        print(f"{num} é par!")
