def calcular_velocidade_media(distancia:float, tempo:float):
    #código da nossa função
    velocidade_media = distancia / tempo
    # exibir o resultado
    print(f"A velocidade média é {velocidade_media}/km")

#Solicitar distância e tempo

dist_digitada = float(input("Digete a distancia percorrida: ")) # Distancia = Varieavel
tempo_digitado = float(input("Digite o tempo que levou: "))
calcular_velocidade_media(dist_digitada, tempo_digitado)








