import jogo_adivinhacao
import jogo_forca

def escolhendo_jogos():
    print('**********************************' )
    print('Bem vindo, escolha o jogo')
    print('**********************************' )


    print('(1)adivinhacao (2)Forca')
    jogo = int(input('Qual jogo? '))

    if(jogo ==1):
        print('Jogando adivinhacao')
        jogo_adivinhacao.jogo_adivinhacao()
    elif( jogo == 2):
        print('Jogando forca')
        jogo_forca.jogo_forca()

if (__name__ == "__main__"):
     escolhendo_jogos()    