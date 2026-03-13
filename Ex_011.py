#Importação
from collections import defaultdict

#criação de um defaultdic com uma lista como valor padrão

dicionario_lista = defaultdict(list)
dicionario_lista["Produto"] = "Macbook Pro"
dicionario_lista["Marca"] = "Apple"

print(dicionario_lista["PREÇO"])
print(dicionario_lista)

#Criação de função que rretorna a frase "Inexistente"

def função_exemplo():
    return "Inesistente"
dicionario_funcao = defaultdict(função_exemplo)
dicionario_funcao["Produto"] = "Macbook Pro"
dicionario_funcao["Marca"] = "Apple"

print(dicionario_funcao)
print(dicionario_funcao["PREÇO"])
print(dicionario_funcao)

#Criação de dicionário com uma função lambda

dicionario_lambda = defaultdict(lambda: "Não disponivel")
dicionario_lambda["Produto"] = "Macbook Pro"
dicionario_lambda["Marca"] = "Apple"