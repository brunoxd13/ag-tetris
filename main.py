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
            gameState = jogo.jogar(geracao.individuos[i], vel_jogo, scoreMax = 200000, jogoRapido = True)
            geracao.individuos[i].fitness(gameState)
            print("Individuo: "+ (i + 1).__str__() + " score:" + geracao.individuos[i].score.__str__())
        geracao.selecao(3, best_individuos, score_medias_geracoes)

        geracao.reproduzir(qtInd, chanceCO, mutacao)

    print("melhor individuo!!!")

    gameState = jogo.jogar(geracao.individuos[0], vel_jogo, 1)

    print("Melhores Individuos:")
    print(best_individuos)
    plt.subplot(211)

    plt.title('Fitness Melhores Individuos por Geração')
    plt.plot(best_individuos)
    plt.ylabel("Fitness Melhores Individuos")
    plt.xlabel("Gerações")

    plt.subplot(212)
    print("Medias Fitness por Gerações:")
    print(score_medias_geracoes)
    plt.title('Médias de Fitness de Individuos por Geração')
    plt.plot(score_medias_geracoes)
    plt.ylabel("Media Fitness Geração")
    plt.xlabel("Gerações")
    plt.subplots_adjust(top=0.94, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                        wspace=0.35)

    plt.show()



    return(geracao)

gen = main()

