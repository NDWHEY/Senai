nome = input("Digite seu nome ")
peso = int((input("Digite seu peso ")))
altura = float((input("Digite sua altura ")))

imcpeso = (altura*2)

resultadoimc = (peso / imcpeso)

if resultadoimc <= 18.5:
    print("Seu IMC é magreza grau 0")
elif resultadoimc >= 18.5 and resultadoimc <= 24.9:
    print("Seu IMC é normal grau 0")
elif resultadoimc >= 25 and resultadoimc <= 29.9:
    print("Seu IMC é sobre peso grau 1")
elif resultadoimc >= 30.0 and resultadoimc <= 39.9:
    print("Seu IMC é obesidade grau 2")
else:
    print("Seu IMC é obsidade grave grau 3")