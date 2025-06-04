
# #1

x = input("Escolhar entre pedra, papel e tesoura: ")
y = input("Escolhar entre pedra, papel e tesoura: ")

if x == "pedra" and y == "papel":
    print("Papel ganhou")
elif x == "pedra" and y == "tesoura":
    print("Pedra ganhou")
elif x == "papel" and y == "tesoura":
    print("Tesoura ganhou")
elif x == "papel" and y == "pedra":
    print("Papel ganhou")
elif x == "tesoura" and y == "pedra":
    print("Pedra ganhou")
elif x == "tesoura" and y == "papel":
    print("Tesoura ganhou")

#2

num = int(input("Digita um número inteiro: "))

if num % 2 == 0:
    print("Número Par")
else:
    print("Número ímpar")

#3
import random
num = float(input("Digite o número secreto: "))

secreto = random.randint(1,80)

if num == secreto:
    print("Você acertou o número secreto: ", secreto)
else:
    print("Não foi desta vez", secreto)

