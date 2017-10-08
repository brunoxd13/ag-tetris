import jogo
import algoritmoGenetico as ag

def main():
    qtdPop = int(input("Quantidade Gerações: "))
    qtInd = int(input("Quantidade de individuos: "))
    mutacao = float(input("Mutação:"))
    chanceCO = float(input("CrossOver:"))

    geracao = ag.Geracao(qtInd)

    vel_jogo = 500
    for j in range(qtdPop):
        print (' \n')
        print (' - - - - Geração atual: {} - - - - ' .format(j+1))
        print (' \n')

        for i in range(qtInd):
            gameState = jogo.jogar(geracao.individuos[i], vel_jogo, scoreMax = 200000, jogoRapido = False)
            geracao.individuos[i].fitness(gameState)
            print("Individuo: "+ (i + 1).__str__() + " score:" + geracao.individuos[i].score.__str__())

        geracao.selecao(3)
        geracao.reproduzir(qtInd, chanceCO, mutacao)

    print("melhor individuo!!!")

    gameState = jogo.jogar(geracao.individuos[0], vel_jogo, 1)

    return(geracao)

gen = main()

