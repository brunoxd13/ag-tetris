import jogo
import algoritmoGenetico as ag
import matplotlib.pyplot as plt

def main():
    qtdPop = int(input("Quantidade Gerações: "))
    qtInd = int(input("Quantidade de individuos: "))
    mutacao = float(input("Mutação:"))
    chanceCO = float(input("CrossOver:"))

    geracao = ag.Geracao(qtInd)

    best_individuos = []
    score_medias_geracoes = []


    vel_jogo = 500
    for j in range(qtdPop):
        print (' \n')
        print (' - - - - Geração atual: {} - - - - ' .format(j+1))
        print (' \n')

        for i in range(qtInd):
            gameState = jogo.jogar(geracao.individuos[i], vel_jogo, scoreMax = 200000, jogoRapido = False)
            geracao.individuos[i].fitness(gameState)
            print("Individuo: "+ (i + 1).__str__() + " score:" + geracao.individuos[i].score.__str__())
        geracao.selecao(3, best_individuos, score_medias_geracoes)

        geracao.reproduzir(qtInd, chanceCO, mutacao)

    print("melhor individuo!!!")

    gameState = jogo.jogar(geracao.individuos[0], vel_jogo, 1)

    print("Melhores Individuos:")
    print(best_individuos)

    plt.plot(best_individuos)
    plt.ylabel("Fitness Melhores Individuos")
    plt.xlabel("Gerações")
    plt.show()

    print("Melhores Medias Fitness Gerações:")
    print(score_medias_geracoes)

    plt.plot(score_medias_geracoes)
    plt.ylabel("Media Fitness Geração")
    plt.xlabel("Gerações")
    plt.show()



    return(geracao)

gen = main()

