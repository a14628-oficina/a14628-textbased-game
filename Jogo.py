# Introdução do jogo e explicação da missão para o jogador
print("Bem-vindo à floresta! Tens de encontrar um tesouro perdido!")
print("Estás numa floresta e precisas de encontrar o tesouro.")
print("A tua missão é encontrar o tesouro perdido e voltar para casa.")
print("Boa sorte!")
print("Vamos começar!")

# Primeira escolha: o jogador encontra uma encruzilhada e precisa decidir para onde ir
print("Entraste na floresta e encontraste uma encruzilhada. Tens duas opções:")
print("1. Ir para a esquerda")
print("2. Ir para a direita")

# Armazena a escolha do jogador
escolha = input("Qual é a tua escolha? (1 ou 2): ")

# Se o jogador escolheu a primeira opção
if escolha == "1":
    # Segunda escolha: o jogador encontra um rio e precisa decidir como atravessá-lo
    print("Encontraste um rio e precisas de atravessá-lo.")
    print("1. Nadar")
    print("2. Usar uma ponte")
    escolha = input("Qual é a tua escolha? (1 ou 2): ")

    # Caso o jogador escolha nadar, o jogo termina
    if escolha == "1":
        print("Não conseguiste atravessar o rio e morreste.")
        print("Fim de jogo.")
    # Caso o jogador escolha a ponte, ele atravessa com sucesso
    elif escolha == "2":
        print("Usaste uma ponte e atravessaste o rio com sucesso.")
        print("Agora estás numa caverna e tens duas opções:")
        print("1. Entrar na caverna")
        print("2. Ir para o lado oposto")
        escolha = input("Qual é a tua escolha? (1 ou 2): ")

        # Caso o jogador escolha entrar na caverna
        if escolha == "1":
            print("Encontraste um monstro!!")
            print("1. Lutar")
            print("2. Fugir")
            escolha = input("Qual é a tua escolha? (1 ou 2): ")

            # Caso o jogador escolha lutar com o monstro, ele vence e encontra o tesouro
            if escolha == "1":
                print("Ganhaste a luta e encontraste o tesouro perdido!!")
                print("Parabéns!!")
            # Caso o jogador escolha fugir, o jogo termina sem recompensa
            elif escolha == "2":
                print("Fugiste e voltaste para casa sem nada.")
                print("Fim de jogo.")
        # Se o jogador escolhe ir para o lado oposto
        elif escolha == "2":
            print("Decidiste evitar a caverna e explorar outro caminho.")
            print("Encontraste um monstro!!")
            print("1. Lutar")
            print("2. Fugir")
            escolha = input("Qual é a tua escolha? (1 ou 2): ")

            # Caso o jogador escolha lutar, ele perde por estar fraco
            if escolha == "1":
                print("Morreste para o monstro, pois estavas muito fraco!")
            # Caso o jogador escolha fugir, o jogo termina sem recompensa
            elif escolha == "2":
                print("Fugiste e voltaste para casa sem nada.")
            print("Fim de jogo.")

# Se o jogador escolhe a segunda opção na encruzilhada
elif escolha == "2":
    print("Encontraste um castelo abandonado!!")
    print("1. Entrar")
    print("2. Voltar")
    escolha = input("Qual é a tua escolha? (1 ou 2): ")

    # Caso o jogador escolha entrar no castelo
    if escolha == "1":
        print("Encontraste uma princesa presa no castelo!!")
        print("1. Salvar a princesa")
        print("2. Não salvar a princesa")
        escolha = input("Qual é a tua escolha? (1 ou 2): ")

        # Caso o jogador escolha salvar a princesa, ele retorna com ela e vence o jogo
        if escolha == "1":
            print("Salvaste a princesa e voltaste para casa com ela.")
            print("Fim de jogo!")
        # Caso o jogador escolha não salvar a princesa, o jogo termina sem recompensa
        elif escolha == "2":
            print("Ignoraste a princesa e voltaste para casa sozinho.")
            print("Fim de jogo.")
