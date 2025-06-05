# liste os dias da semana e , caso seja final de semana exiba  é final de semana.

# dia = str(input("Escolha um dia de semana: "))

# segunda = "Segunda"

# terça = "Terça"

# quarta = "Quarta"

# quinta = "Quinta"

# sexta = "Sexta"

# sábado = "Sábado"

# domingo = "Domingo"



# if dia == sábado or dia == domingo:
#     print("É final de semana")
# else:
#     print("v")

# dia = str.lower(input("Escolha um de semana: "))

# match dia:
#     case "sabado":
#         print("Final de semana")
#     case "domingo":
#         print("Final de semana")
#     case _:
#         print("Dia de semana")

# contador = 0
# while contador < 3:
#     print(contador)
#     contador += 1



contador = int(input("Quantos números vamos verificar ?"))
repeticao = 0

while contador > repeticao:
    repeticao = repeticao +1
    num = int(input("Digite alguns números inteiro "))
    if contador % 2 == 0:
        print("Número par")
    else:
        print("Número Ímpar")


