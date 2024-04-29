import random
# Definir conjuntos de palavras
ANIMAIS = ["GATO", "CACHORRO", "ELEFANTE"]
FRUTAS = ["MACA", "BANANA", "UVA"]
OBJETOS = ["CADERNO", "CANETA", "TELEVISAO"]
# Lista de conjuntos
palavras = {
    "ANIMAIS": ANIMAIS,
    "FRUTAS": FRUTAS,
    "OBJETOS": OBJETOS
}
def selecionar_palavra():
    categoria = random.choice(list(palavras.keys()))
    palavra = random.choice(palavras[categoria])
    return categoria, palavra
def desenhar_forca(tentativas_erradas):
    if tentativas_erradas == 0:
        print(" -------")
        print("|       ")
        print("|       ")
        print("|       ")
        print("|       ")
        print("----------")
    elif tentativas_erradas == 1:
        print(" -------")
        print("|     |")
        print("|       ")
        print("|       ")
        print("|       ")
        print("----------")
    # Adicione mais casos para as tentativas erradas restantes
# Início do jogo
print("Bem-vindo ao jogo da forca!")
categoria, palavra = selecionar_palavra()
print(f"Dica: Categoria '{categoria}'")
palavra_revelada = "_" * len(palavra)
tentativas_erradas = 0
while True:
    print("\nPalavra: ", " ".join(palavra_revelada))
    palpite = input("Digite uma letra ou a palavra inteira: ").upper()
    if len(palpite) == 1:  # Palpite é uma letra
        if palpite in palavra:
            indices = [i for i, letter in enumerate(palavra) if letter == palpite]
            for idx in indices:
                palavra_revelada = palavra_revelada[:idx] + palpite + palavra_revelada[idx+1:]
        else:
            tentativas_erradas += 1
            desenhar_forca(tentativas_erradas)
    else:  # Palpite é a palavra inteira
        if palpite == palavra:
            print("Parabéns! Você acertou a palavra.")
            break
        else:
            tentativas_erradas += 1
            desenhar_forca(tentativas_erradas)
    if "_" not in palavra_revelada:
        print("Parabéns! Você completou a palavra.")
        break
    if tentativas_erradas == 10:
        print("Você excedeu o número máximo de tentativas. A palavra era:", palavra)
        break
