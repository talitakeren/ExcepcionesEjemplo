def obtener_numero_natural():
    while True:
        try:
            # Solicitar al usuario que ingrese un número
            numero = int(input("Ingrese un número natural: "))
            # Validar que el número sea positivo
            if numero > 0:
                return numero
            else:
                print("Debe ingresar un número natural (mayor a 0).")
        except ValueError:
            # Capturar excepciones si el ingreso no es un número entero
            print("Ingreso inválido. Por favor ingrese un número natural.")


def calcular_divisores(numero):
    divisores = []
    # Iterar desde 1 hasta el número y buscar divisores
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores


def main():
    # Obtener un número natural válido
    numero = obtener_numero_natural()

    # Calcular y mostrar los divisores
    divisores = calcular_divisores(numero)
    print(f"Los divisores de {numero} son: {divisores}")


if __name__ == "__main__":
    main()
