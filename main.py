import jogo
import algoritmoGenetico as ag

def main():
    numInd = int(input("Qual o tamanho da população: "))
    numInd = int(input("Qual o tamanho da população: "))

    geracao = ag.Geracao(numInd)

    vel_jogo = 500
    for j in range(numInd):
        print (' \n')
        print (' - - - - Geração atual: {} - - - - ' .format(j+1))
        print (' \n')
        
        for i in range(numInd):
            gameState = jogo.jogar(geracao.individuos[i], vel_jogo, scoreMax = 200000, jogoRapido = False)
            geracao.individuos[i].fitness(gameState)

        geracao.selecao(3)
        geracao.reproduzir(10)

    print("melhor individuo!!!")
    
    gameState = jogo.jogar(geracao.individuos[0], vel_jogo, 1)

    return(geracao)

gen = main()
