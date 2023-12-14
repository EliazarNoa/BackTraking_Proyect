def comprobar(reinas, n, k):
    for i in range(k):
        if reinas[i] == reinas[k] or abs(k - i) == abs(reinas[k] - reinas[i]):
            return False
    return True

def Nreinas(reinas, n, k):
    global x
    if k == n:
        x += 1
        print(f"Solucion {x} : {reinas}")
    else:
        for i in range(n):
            reinas[k] = i
            if comprobar(reinas, n, k):
                Nreinas(reinas, n, k + 1)

if __name__ == "__main__":
    x = 0
    k = 0
    cant = int(input("Ingresar la cantidad de reinas: "))
    reinas = [-1] * cant

    Nreinas(reinas, cant, k)