#Dados
idade = 0
nome = ""
salario = 0.0
brasileiro = False
#Solicitação de dados
idade = int(input("Digite a sua idade: "))
nome = input("Qual seu nome: ")
salario = float(input("Quanto você recebe neste novo emprego? "))
resposta = input("Você é brasileiro? (sim/nao): ").lower()
#Se a resposta for verdadeira(Sim)
if resposta == "sim":
    brasileiro = True
else:
    brasileiro = False

# Saída de dados
print(f"Idade: {idade}")
print(f"Nome: {nome}")
print(f"Seu salário é: R$ {salario:.2f}")
print(f"Brasileiro: {brasileiro}")