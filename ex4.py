compras = float(input("Qual é o valor da sua compra ? "))




if compras < 100:
    print("Você não teve desconto o valor da sua compra é: ", compras)
else:
    print("Seu desconto foi de:", (compras*0.10))
    print("O valor final da sua compra foi:", (compras*0.9))      