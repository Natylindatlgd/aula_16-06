def verificar_erro_comentario():
    comentario = input("Digite seu comentário para o blog: ")
    contem_erro = "erro" in comentario.lower()
    comprimento = len(comentario)

    if contem_erro:
        print("O comentário contém a palavra 'erro'.")
    else:
        print("O comentário não contém a palavra 'erro'.")

    print(f"O comprimento total do comentário é: {comprimento} caracteres.")

if __name__ == "__main__":
    verificar_erro_comentario()