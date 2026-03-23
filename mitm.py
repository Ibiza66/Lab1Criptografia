def descifrar_cesar(texto):
    print("\nPosibles descifrados:\n")

    for desplazamiento in range(26):
        resultado = ""

        for caracter in texto:
            if caracter.isalpha():
                base = ord('a') if caracter.islower() else ord('A')
                nuevo = chr((ord(caracter) - base - desplazamiento) % 26 + base)
                resultado += nuevo
            else:
                resultado += caracter

        print(f"Desplazamiento {desplazamiento}: {resultado}")

if __name__ == "__main__":
    texto = input("Texto cifrado: ")
    descifrar_cesar(texto)
