# Função para calcular velocidade média
def calcular_velocidade_media(distancia: float, tempo: float, unidade_media="km/h"):
    if tempo == 0:
        return 0
    velocidade_media = distancia / tempo
    return f"{velocidade_media:.2f} {unidade_media}"


# Função para converter temperatura
def converter_temperatura(temperatura: float, unidade_medida="celsius"):
    if unidade_medida.lower() == "celsius":
        return temperatura * 1.8 + 32
    elif unidade_medida.lower() == "fahrenheit":
        return (temperatura - 32) / 1.8
    else:
        return "Unidade inválida"


# Função para exibir menu
def exibir_menu():
    print("\nMenu")
    print("1 - Calcular a velocidade média")
    print("2 - Converter temperatura")
    print("3 - Sair")


# Função principal
def aluno_de_fisica():
    op = 0

    while op != 3:
        exibir_menu()
        op = int(input("Informe a opção desejada: "))

        if op == 1:
            distancia_percorrida = float(input("Informe a distância: "))
            tempo_viagem = float(input("Informe o tempo de viagem: "))
            print(f"A velocidade média é {calcular_velocidade_media(distancia_percorrida, tempo_viagem)}")

        elif op == 2:
            temperatura = float(input("Informe a temperatura que deseja converter: "))
            medida = input("A temperatura está em Celsius ou Fahrenheit? ")
            resultado = converter_temperatura(temperatura, medida)
            print(f"O resultado da conversão é {resultado}")

        elif op == 3:
            print("Saindo...")

        else:
            print("Opção inválida")


# Executar programa
aluno_de_fisica()