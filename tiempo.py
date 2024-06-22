from time import time

# Lista para almacenar los tiempos y nombres de los jugadores
Ranking = []

def inicio():
    global inicio_tiempo
    inicio_tiempo = time()

def terminado():
    global tiempo_pasado
    tiempo_pasado = time() - inicio_tiempo
    if tiempo_pasado > 60:
        minutos = int(tiempo_pasado // 60)
        segundos = tiempo_pasado % 60
        print("Tiempo transcurrido: {} minutos y {:.2f} segundos.".format(minutos, segundos))
    else:
        print("Tiempo transcurrido: {:.2f} segundos.".format(tiempo_pasado))

def Ordenar():
    global Ranking
    Ranking.sort(key=lambda x: int(x.split(':')[0]))  # Ordena por el número antes del ':'
    print("Ranking ordenado:")
    for i, jugador in enumerate(Ranking[:5], 1):  # Muestra solo los primeros 5 jugadores
        print("{}. {}".format(i, jugador))

# Ejemplo de uso
def main():
    inicio()
    iniciar = input("Nombre del Jugador: ")
    terminar = input("Terminar: ")

    # Agregar jugador con su tiempo al Ranking
    tiempo_jugador = time() - inicio_tiempo
    Ranking.append("{:.2f} segundos : {}".format(tiempo_jugador, iniciar))

    terminado()
    Ordenar()

if __name__ == "__main__":
    main()
