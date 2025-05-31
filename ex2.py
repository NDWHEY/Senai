nome = input("Digite o seu nome: ")
nota1 = int(input("Digite a nota1: "))
nota2 = int(input("Digite a nota2: "))
meida = ((nota1+nota2)/2)

if meida >= 7:
    print(nome, " Você está aprovado")
else: 
    print(nome, " você está reprovado:(")