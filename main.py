import jogo
import algoritmoGenetico as ag

def main():

    numInd = 10
    geracao = ag.Geracao(numInd)

    vel_jogo = 500
    for j in range(numInd):
        print (' \n')
        print (' - - - - Geração atual: {} - - - - ' .format(j+1))
        print (' \n')
        
        for i in range(10):
            gameState = jogo.jogar(geracao.individuos[i], vel_jogo, scoreMax = 200000, jogoRapido = False)
            
            print(gameState)
            [230, [66, 5, 0, 0], 3470, False]
            geracao.individuos[i].fitness(gameState)
            geracao.selecao(1)

            print("melhor individuo da geração!!!")

        geracao.selecao(3)
        geracao.reproduzir(10)

    geracao.selecao(1)
    print("melhor individuo!!!")

    gameState = jogo.jogar(geracao.individuos[0], vel_jogo, 1)    

    return(geracao)


gen = main()