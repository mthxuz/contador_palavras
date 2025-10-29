def contar_palavras(texto):
    palavras = texto.split()
    return len(palavras)

if __name__ == "__main__":
    texto = input("Digite um texto: ")
    total = contar_palavras(texto)
    print(f"Total de palavras: {total}")