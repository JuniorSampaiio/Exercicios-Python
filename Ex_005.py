#Solicitação de dados
nome = input("Digite seu nome: ")
idade = int(input("Quantos anos você tem? "))
cidade = input("De qual cidade você é?: ")
#Saida de dados
if idade >= 18:
    print("Olá", nome, "você é maior de idade, vejo que você tem", idade, "anos")
else:
    print("Olá", nome, "você é menor de idade, vejo que você tem", idade, "anos")

