import sys

def cifrar_cesar(texto, desplazamiento):
    resultado = ""

    for caracter in texto:
        if caracter.isalpha():
            base = ord('a') if caracter.islower() else ord('A')
            nuevo = chr((ord(caracter) - base + desplazamiento) % 26 + base)
            resultado += nuevo
        else:
            resultado += caracter

    return resultado

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 cifrado.py 'texto' desplazamiento")
        sys.exit(1)

    texto = sys.argv[1]
    desplazamiento = int(sys.argv[2])

    cifrado = cifrar_cesar(texto, desplazamiento)

    print(f"Texto original: {texto}")
    print(f"Desplazamiento: {desplazamiento}")
    print(f"Texto cifrado: {cifrado}")
