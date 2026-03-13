#Importação do OrderedDict

from collections import OrderedDict

#Criação

dicionario_ordenado = OrderedDict()
print(dicionario_ordenado)

#Adicionando chave e valores
dicionario_ordenado["Nome"] ="Iphone"
dicionario_ordenado["Marca"] ="Apple"
dicionario_ordenado["Modelo"] = "13 ProMax"

#Percorrendo para verificar a ordem

for chave,valor in dicionario_ordenado.items():
    print(f"{chave} -- {valor} ")

#Alterando um novo item 

dicionario_ordenado["Marca"] ="Samsung"
print()

#Percorrendo para verificar a ordem
for chave,valor in dicionario_ordenado.items():
    print(f"{chave} -- {valor} ")

#Renovando um item

dicionario_ordenado.pop("Marca")
print()

#Percorrendo para verificar a ordem

for chave,valor in dicionario_ordenado.items():
    print(f"{chave} -- {valor} ")
