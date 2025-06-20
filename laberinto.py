laberinto = [
    [1, 1, 1, 3, 0, 1, 1, 1, 4],
    [3, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 3, 1, 1],
    [3, 0, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 3, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 4],
    [1, 1, 3, 1, 0, 1, 1, 1, 1],
]

inicio = (8, 0)
fin = (0, 0)

# Orden de movimiento: arriba, derecha, abajo, izquierda

movimientos = [(-1, 0), (0, 1), (1, 0), (0, -1)]

camino = [[0 for _ in range(9)] for _ in range(9)]

def buscar_camino(x, y, puntos):
    if (x, y) == fin:
        if puntos >= 23:
            camino[x][y] = 1
            return True
        return False

    valor = laberinto[x][y]
    laberinto[x][y] = -1 
    camino[x][y] = 1

    for dx, dy in movimientos:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 9 and 0 <= ny < 9:
            siguiente = laberinto[nx][ny]
            if siguiente != 0 and siguiente != -1:
                if buscar_camino(nx, ny, puntos + siguiente):
                    return True

    laberinto[x][y] = valor  
    camino[x][y] = 0
    return False

def mostrar_matriz(m):
    for fila in m:
        print(" ".join(str(c) for c in fila))


print("Laberinto original:")
mostrar_matriz(laberinto)


if buscar_camino(inicio[0], inicio[1], 1):
    print("\n¡Camino encontrado con 23 o más puntos!")
    print("Camino recorrido (1 = pasó por ahí):")
    mostrar_matriz(camino)
else:
    print("\nNo se encontró un camino válido con 23 puntos.")

