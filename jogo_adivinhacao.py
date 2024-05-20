import random

def jogo_adivinhacao():
    print('**********************************' )
    print('Bem vindo ao jogo de  adivinhacao')
    print('**********************************' )

    numero_secreto = random.randrange(1,101)
    tentativas = 0
    pontos = 1000

    # print(numero_secreto)
    print('escolha o nivel')
    print('(1)Facil, (2)Medio, (3)Dificil', )

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        tentativas = 20
    elif (nivel == 2):
        tentativas = 10
    else:
        tentativas = 5     

    for rodada in range(1,tentativas + 1):
        print(f'tentativa {rodada} de {tentativas}')
        chute = int(input('digite um numero entre 1 e 100: '))
        print('voce digitou', chute)

        if (chute < 1 or chute > 100):
            print('digite um numero entre 1 a 100')
            continue
    
        acertou = chute == numero_secreto
        maior   = chute >  numero_secreto
        menor   = chute <  numero_secreto


        if (acertou):
            print(f'voce acertou e fez {pontos}')
        else:
            if (maior):
                print ('voce errou, seu chute foi maior que o numero secreto')
            elif (menor):
                print ('voce errou, seu chute foi menor que o numero secreto')
            pontos_perdidos =abs(numero_secreto - chute)
            pontos = pontos_perdidos
    

    print('fim de jogo')

    if (__name__ == "__main__"):
        jogo_adivinhacao()