#*******************AGENTE BASEADO EM OBJETIVO***************************************
import numpy as np
import matplotlib.pyplot as plt
import random

#cria as paredes da matriz
matriz = np.ones((6,6), dtype=np.int0)

#lista para guardar as posicoes onde estao as sujeiras
listaPosicoesCaminhar = [] 

#controla a quantidade de sujeira restante na sala
qtdSujeira = 0

#guarda a quantidade de pontos do agente
pontos = 0

#varialvel pra guardar as mensagens de acao do agente
msgAgente = ''

#cria a parte por onde o agente vai se movimentar (suja o ambiente)
def sujarAmbiente ():
  
  global listaPosicoesCaminhar

  for c in range(1,5):
    for l in range(1,5):

      #num pode ser 0, 1 ou 2. Se for 1, ele vira 2. Se for 0 ou 2, eh colocado na posicao na matriz
      num = random.randrange(0,2)

      if num == 1 or num == 2:
        posicao = [c,l]
        listaPosicoesCaminhar.append(posicao)

      if num == 1:
        num = 2
        matriz[c][l] = num
      else:
        matriz[c][l] = num

      #se uma sujeira eh adicionada no ambiente, atualizada a variavel global que guarda a quantidade de sujeira que o ambiente possui
      if num == 2:
        global qtdSujeira
        local = qtdSujeira + 1
        qtdSujeira = local


#funcao para checar se o ambiente todo esta limpo
def checkObj ():
  global qtdSujeira
  
  if qtdSujeira == 0:
    return True
  else:
    return False


#funcao que retorna uma reacao do agente
def agenteObjetivo (matriz, c, l, status, checar):

  #checa se o todo o ambiente esta limpo
  if checar:
    return 'Devo parar!'

  #variaveis globais
  global msgAgente
  global pontos
  global listaPosicoesCaminhar

  #limpa se estiver sujo
  if status == 2:

    #remove a posicao inicial da lista se estiver suja
    if c == 1 and l == 1:
      posicao = [1,1]
      listaPosicoesCaminhar.remove(posicao)

    #conta um ponto pela limpeza
    localPontos = pontos + 1
    pontos = localPontos

    #concatena na variavel global msgAgente a acao aspirar
    localMsg = msgAgente + '\nAção: Aspirar. + 1 ponto para o agente!'
    msgAgente = localMsg

    #chama a funcao limpar
    limpar(matriz, c, l)
    posicao = [c,l] 

    #retorna a posicao atual que foi limpa
    return posicao

  #contador para controlar a entrada nos ifs (vai sempre primeiro para sujeira mais proxima)
  contador = 0
  
  #while para ficar em loop ate achar a sujeira mais proxima
  while True:
    
  #coluna e linha, comecando em + 1 e - 1
    for p in listaPosicoesCaminhar:

      #pega a posicao da sujeira na lista
      coluna = p[0]
      linha = p[1]


      #verifica a distancia da sujeira em relacao com a posicao atual, montando a mensagem das acoes e contando os pontos
      #os ifs com menor diferenca (distancia) seram executados primeiro se tiver a possibilidade
      #caso nao, um if mais distante eh verificado ate achar o correspondente

      #coluna + 1 até linha + 3

      if (coluna - c) == 1: #verifica se a distancia da coordenada atual em comparacao com a da sujeira eh == 1
                            #se for == 1, tenta todas as possibilidades de diferença (0 a 3 e de -1 a -3) para a outra coordenada que compoe a posicao 
        #linha +
        if (linha - l) == 0 and contador == 0: #verifica se a distancia de uma coordenada a outra eh == 0 e verifica a prioridade (contador == 0 -> mais alta prioridade)
          
          #Caso entre nesse if aqui, a distancia da sujeira mais proxima eh de 1 quadrado, ou seja, ele vai se movimentar uma vez, neste caso, para baixo
          #Com esse movimento, vai estar no quadrado da sujeira

          #concatena a acao na variavel global que guarda as acoes do agente
          localMsg = msgAgente + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
          msgAgente = localMsg
        
          #concatena os pontos realizados aqui na variavel global que guarda os pontos do agente
          localPontos = pontos + 1
          pontos = localPontos

          #remove da lista esta posicao (que é onde esta a sujeira)
          listaPosicoesCaminhar.remove(p)

          #retorna esta posicao para ser limpa e usada como posicao atual para o proxima rodada se houver
          return p

        #e assim segue o código...


        elif (linha - l) == 1 and contador == 1:
          localMsg = (msgAgente + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 2
          pontos = localPontos
          exibir(matriz, coluna, linha - 1)
          listaPosicoesCaminhar.remove(p)
          return p

        elif (linha - l) == 2 and contador == 3:
          localMsg = (msgAgente + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 3
          pontos = localPontos
          exibir(matriz, coluna, linha - 2)
          exibir(matriz, coluna, linha - 1)
          listaPosicoesCaminhar.remove(p)
          return p

        elif (linha - l) == 3 and contador == 4:
          localMsg = (msgAgente + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 4
          pontos = localPontos
          exibir(matriz, coluna, linha - 3)
          exibir(matriz, coluna, linha - 2)
          exibir(matriz, coluna, linha - 1)
          listaPosicoesCaminhar.remove(p)
          return p

        #linha -
        elif (linha - l) == -1 and contador == 1:
          localMsg = (msgAgente + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 2
          pontos = localPontos
          exibir(matriz, coluna, linha + 1)
          listaPosicoesCaminhar.remove(p)
          return p

        elif (linha - l) == -2 and contador == 3:
          localMsg = (msgAgente + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 3
          pontos = localPontos
          exibir(matriz, coluna, linha + 2)
          exibir(matriz, coluna, linha + 1)
          listaPosicoesCaminhar.remove(p)
          return p

        elif (linha - l) == -3 and contador == 4:
          localMsg = (msgAgente + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 4
          pontos = localPontos
          exibir(matriz, coluna, linha + 3)
          exibir(matriz, coluna, linha + 2)
          exibir(matriz, coluna, linha + 1)
          listaPosicoesCaminhar.remove(p)
          return p


      #coluna - 1 até linha + 3
      if (coluna - c) == -1:

        #linha +
        if (linha - l) == 0 and contador == 0:
          localMsg = msgAgente + '\nAção: Andar Acima. + 1 ponto para o agente!'
          msgAgente = localMsg
          localPontos = pontos + 1
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          return p

        elif (linha - l) == 1 and contador == 1:
          localMsg = (msgAgente + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 2
          pontos = localPontos
          exibir(matriz, coluna, linha - 1)
          listaPosicoesCaminhar.remove(p)
          return p

        elif (linha - l) == 2 and contador == 3:
          localMsg = (msgAgente + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 3
          pontos = localPontos
          exibir(matriz, coluna, linha - 2)
          exibir(matriz, coluna, linha - 1)
          listaPosicoesCaminhar.remove(p)
          return p

        elif (linha - l) == 3 and contador == 4:
          localMsg = (msgAgente + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 4
          pontos = localPontos
          exibir(matriz, coluna, linha - 3)
          exibir(matriz, coluna, linha - 2)
          exibir(matriz, coluna, linha - 1)
          listaPosicoesCaminhar.remove(p)
          return p
      
        #linha -
        elif (linha - l) == -1 and contador == 1:
          localMsg = (msgAgente + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 2
          pontos = localPontos
          exibir(matriz, coluna, linha + 1)
          listaPosicoesCaminhar.remove(p)
          return p

        elif (linha - l) == -2 and contador == 3:
          localMsg = (msgAgente + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 3
          pontos = localPontos
          exibir(matriz, coluna, linha + 2)
          exibir(matriz, coluna, linha + 1)
          listaPosicoesCaminhar.remove(p)
          return p

        elif (linha - l) == -3 and contador == 4:
          localMsg = (msgAgente + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 4
          pontos = localPontos
          exibir(matriz, coluna, linha + 3)
          exibir(matriz, coluna, linha + 2)
          exibir(matriz, coluna, linha + 1)
          listaPosicoesCaminhar.remove(p)
          return p

      #linha + 1 até coluna + 3
      if (linha - l) == 1:

        #coluna +
        if (coluna - c) == 0 and contador == 0:
          localMsg = msgAgente + '\nAção: Andar Direita. + 1 ponto para o agente!'
          msgAgente = localMsg
          localPontos = pontos + 1
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)   
          return p
        
        elif (coluna - c) == 1 and contador == 1:
          localMsg = (msgAgente + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 2
          pontos = localPontos
          exibir(matriz, coluna - 1, linha)
          listaPosicoesCaminhar.remove(p)   
          return p
        
        elif (coluna - c) == 2 and contador == 3:
          localMsg = (msgAgente + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 3
          pontos = localPontos
          exibir(matriz, coluna - 2, linha)
          exibir(matriz, coluna - 1, linha)
          listaPosicoesCaminhar.remove(p)   
          return p
        
        elif (coluna - c) == 3 and contador == 4:
          localMsg = (msgAgente + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 4
          pontos = localPontos
          exibir(matriz, coluna - 3, linha)
          exibir(matriz, coluna - 2, linha)
          exibir(matriz, coluna - 1, linha)
          listaPosicoesCaminhar.remove(p)   
          return p

        #coluna -
        elif (coluna - c) == -1 and contador == 1:
          localMsg = (msgAgente + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 2
          pontos = localPontos
          exibir(matriz, coluna + 1, linha)
          listaPosicoesCaminhar.remove(p)   
          return p
        
        elif (coluna - c) == -2 and contador == 3:
          localMsg = (msgAgente + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 3
          pontos = localPontos
          exibir(matriz, coluna + 2, linha)
          exibir(matriz, coluna + 1, linha)
          listaPosicoesCaminhar.remove(p)   
          return p
        
        elif (coluna - c) == -3 and contador == 4:
          localMsg = (msgAgente + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 4
          pontos = localPontos
          exibir(matriz, coluna + 3, linha)
          exibir(matriz, coluna + 2, linha)
          exibir(matriz, coluna + 1, linha)
          listaPosicoesCaminhar.remove(p)   
          return p

      #linha - 1 até coluna + 3
      if (linha - l) == -1:

        #coluna +
        if (coluna - c) == 0 and contador == 0:
          localMsg = msgAgente + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
          msgAgente = localMsg
          localPontos = pontos + 1
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)   
          return p
        
        elif (coluna - c) == 1 and contador == 1:
          localMsg = (msgAgente + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 2
          pontos = localPontos
          exibir(matriz, coluna - 1, linha)
          listaPosicoesCaminhar.remove(p)   
          return p
        
        elif (coluna - c) == 2 and contador == 3:
          localMsg = (msgAgente + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 3
          pontos = localPontos
          exibir(matriz, coluna - 2, linha)
          exibir(matriz, coluna - 1, linha)
          listaPosicoesCaminhar.remove(p)   
          return p
        
        elif (coluna - c) == 3 and contador == 4:
          localMsg = (msgAgente + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 4
          pontos = localPontos
          exibir(matriz, coluna - 3, linha)
          exibir(matriz, coluna - 2, linha)
          exibir(matriz, coluna - 1, linha)
          listaPosicoesCaminhar.remove(p)   
          return p

        #coluna -
        elif (coluna - c) == -1 and contador == 1:
          localMsg = (msgAgente + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 2
          pontos = localPontos
          exibir(matriz, coluna + 1, linha)
          listaPosicoesCaminhar.remove(p)   
          return p
        
        elif (coluna - c) == -2 and contador == 3:
          localMsg = (msgAgente + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 3
          pontos = localPontos
          exibir(matriz, coluna + 2, linha)
          exibir(matriz, coluna + 1, linha)
          listaPosicoesCaminhar.remove(p)   
          return p
        
        elif (coluna - c) == -3 and contador == 4:
          localMsg = (msgAgente + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 4
          pontos = localPontos
          exibir(matriz, coluna + 3, linha)
          exibir(matriz, coluna + 2, linha)
          exibir(matriz, coluna + 1, linha)
          listaPosicoesCaminhar.remove(p)   
          return p

    #coluna e linha, comecando em + 2 e - 2

      #coluna + 2 até linha + 3
      if (coluna - c) == 2:

        #linha +
        if (linha - l) == 0 and contador == 1:
          localMsg = (msgAgente + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 2
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna - 1, linha)
          return p

        elif (linha - l) == 1 and contador == 3:
          localMsg = (msgAgente + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 3
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna - 1, linha - 1)
          exibir(matriz, coluna - 1, linha)
          return p

        elif (linha - l) == 2 and contador == 4:
          localMsg = (msgAgente + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 4
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna - 1, linha - 2)
          exibir(matriz, coluna - 1, linha - 1)
          exibir(matriz, coluna - 1, linha)
          return p

        elif (linha - l) == 3 and contador == 5:
          localMsg = (msgAgente + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 5
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna - 1, linha - 3)
          exibir(matriz, coluna - 1, linha - 2)
          exibir(matriz, coluna - 1, linha - 1)
          exibir(matriz, coluna - 1, linha)
          return p

        #linha -
        elif (linha - l) == -1 and contador == 3:
          localMsg = (msgAgente + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 3
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna - 1, linha + 1)
          exibir(matriz, coluna - 1, linha)
          return p

        elif (linha - l) == -2 and contador == 4:
          localMsg = (msgAgente + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 4
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna - 1, linha + 2)
          exibir(matriz, coluna - 1, linha + 1)
          exibir(matriz, coluna - 1, linha)
          return p

        elif (linha - l) == -3 and contador == 5:
          localMsg = (msgAgente + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 5
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna - 1, linha + 3)
          exibir(matriz, coluna - 1, linha + 2)
          exibir(matriz, coluna - 1, linha + 1)
          exibir(matriz, coluna - 1, linha)
          return p

      #coluna - 2 até linha + 3
      if (coluna - c) == -2:

        #linha +
        if (linha - l) == 0 and contador == 1:
          localMsg = (msgAgente + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 2
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna + 1, linha)
          return p

        elif (linha - l) == 1 and contador == 3:
          localMsg = (msgAgente + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 3
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna + 1, linha - 1)
          exibir(matriz, coluna + 1, linha)
          return p

        elif (linha - l) == 2 and contador == 4:
          localMsg = (msgAgente + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 4
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna + 1, linha - 2)
          exibir(matriz, coluna + 1, linha - 1)
          exibir(matriz, coluna + 1, linha)
          return p

        elif (linha - l) == 3 and contador == 5:
          localMsg = (msgAgente + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 5
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna + 1, linha - 3)
          exibir(matriz, coluna + 1, linha - 2)
          exibir(matriz, coluna + 1, linha - 1)
          exibir(matriz, coluna + 1, linha)
          return p

        #linha -
        elif (linha - l) == -1 and contador == 3:
          localMsg = (msgAgente + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 3
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna + 1, linha + 1)
          exibir(matriz, coluna + 1, linha)
          return p

        elif (linha - l) == -2 and contador == 4:
          localMsg = (msgAgente + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 4
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna + 1, linha + 2)
          exibir(matriz, coluna + 1, linha + 1)
          exibir(matriz, coluna + 1, linha)
          return p

        elif (linha - l) == -3 and contador == 5:
          localMsg = (msgAgente + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 5
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna + 1, linha + 3)
          exibir(matriz, coluna + 1, linha + 2)
          exibir(matriz, coluna + 1, linha + 1)
          exibir(matriz, coluna + 1, linha)
          return p
      
      #linha + 2 e coluna até 3
      if (linha - l) == 2:

        #coluna +
        if (coluna - c) == 0 and contador == 1:
          localMsg = (msgAgente + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 2
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna, linha - 1)
          return p

        elif (coluna - c) == 1 and contador == 3:
          localMsg = (msgAgente + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 3
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna - 1, linha - 1)
          exibir(matriz, coluna, linha - 1)
          return p

        elif (coluna - c) == 2 and contador == 4:
          localMsg = (msgAgente + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 4
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna - 2, linha - 1)
          exibir(matriz, coluna - 1, linha - 1)
          exibir(matriz, coluna, linha - 1)
          return p

        elif (coluna - c) == 3 and contador == 5:
          localMsg = (msgAgente + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 5
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna - 3, linha - 1)
          exibir(matriz, coluna - 2, linha - 1)
          exibir(matriz, coluna - 1, linha - 1)
          exibir(matriz, coluna, linha - 1)
          return p

        #coluna -
        elif (coluna - c) == -1 and contador == 3:
          localMsg = (msgAgente + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 3
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna + 1, linha - 1)
          exibir(matriz, coluna, linha - 1)
          return p

        elif (coluna - c) == -2 and contador == 4:
          localMsg = (msgAgente + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 4
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna + 2, linha - 1)
          exibir(matriz, coluna + 1, linha - 1)
          exibir(matriz, coluna, linha - 1)
          return p

        elif (coluna - c) == -3 and contador == 5:
          localMsg = (msgAgente + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 5
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna + 3, linha - 1)
          exibir(matriz, coluna + 2, linha - 1)
          exibir(matriz, coluna + 1, linha - 1)
          exibir(matriz, coluna, linha - 1)
          return p
      
      #linha - 2 e coluna até 3
      if (linha - l) == -2:

        #coluna +
        if (coluna - c) == 0 and contador == 1:
          localMsg = (msgAgente + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 2
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna, linha + 1)
          return p

        elif (coluna - c) == 1 and contador == 3:
          localMsg = (msgAgente + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 3
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna - 1, linha + 1)
          exibir(matriz, coluna, linha + 1)
          return p

        elif (coluna - c) == 2 and contador == 4:
          localMsg = (msgAgente + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 4
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna - 2, linha + 1)
          exibir(matriz, coluna - 1, linha + 1)
          exibir(matriz, coluna, linha + 1)
          return p

        elif (coluna - c) == 3 and contador == 5:
          localMsg = (msgAgente + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 5
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna - 3, linha + 1)
          exibir(matriz, coluna - 2, linha + 1)
          exibir(matriz, coluna - 1, linha + 1)
          exibir(matriz, coluna, linha + 1)
          return p

        #coluna -
        elif (coluna - c) == -1 and contador == 3:
          localMsg = (msgAgente + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 3
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna + 1, linha + 1)
          exibir(matriz, coluna, linha + 1)
          return p

        elif (coluna - c) == -2 and contador == 4:
          localMsg = (msgAgente + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 4
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna + 2, linha + 1)
          exibir(matriz, coluna + 1, linha + 1)
          exibir(matriz, coluna, linha + 1)
          return p

        elif (coluna - c) == -3 and contador == 5:
          localMsg = (msgAgente + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 5
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna + 3, linha + 1)
          exibir(matriz, coluna + 2, linha + 1)
          exibir(matriz, coluna + 1, linha + 1)
          exibir(matriz, coluna, linha + 1)
          return p

    #coluna e linha, comecando em + 3 e - 3

      #coluna + 3 até linha + 3
      if (coluna - c) == 3:

        #linha +
        if (linha - l) == 0 and contador == 3:
          localMsg = (msgAgente + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 3
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna - 2, linha)
          exibir(matriz, coluna - 1, linha)
          return p

        elif (linha - l) == 1 and contador == 4:
          localMsg = (msgAgente + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 4
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna - 2, linha - 1)
          exibir(matriz, coluna - 2, linha)
          exibir(matriz, coluna - 1, linha)
          return p
        
        elif (linha - l) == 2 and contador == 5:
          localMsg = (msgAgente + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 5
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna - 2, linha - 2)
          exibir(matriz, coluna - 2, linha - 1)
          exibir(matriz, coluna - 2, linha)
          exibir(matriz, coluna - 1, linha)
          return p
        
        elif (linha - l) == 3 and contador == 6:
          localMsg = (msgAgente + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 6
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna - 2, linha - 3)
          exibir(matriz, coluna - 2, linha - 2)
          exibir(matriz, coluna - 2, linha - 1)
          exibir(matriz, coluna - 2, linha)
          exibir(matriz, coluna - 1, linha)
          return p

        #linha -
        elif (linha - l) == -1 and contador == 4:
          localMsg = (msgAgente + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 4
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna - 2, linha + 1)
          exibir(matriz, coluna - 2, linha)
          exibir(matriz, coluna - 1, linha)
          return p
        
        elif (linha - l) == -2 and contador == 5:
          localMsg = (msgAgente + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 5
          pontos = localPontos 
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna - 2, linha + 2)
          exibir(matriz, coluna - 2, linha + 1)
          exibir(matriz, coluna - 2, linha)
          exibir(matriz, coluna - 1, linha)
          return p
        
        elif (linha - l) == -3 and contador == 6:
          localMsg = (msgAgente + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 6
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna - 2, linha + 3)
          exibir(matriz, coluna - 2, linha + 2)
          exibir(matriz, coluna - 2, linha + 1)
          exibir(matriz, coluna - 2, linha)
          exibir(matriz, coluna - 1, linha)
          return p

      #coluna - 3 até linha + 3
      if (coluna - c) == -3:

        #linha +
        if (linha - l) == 0 and contador == 3:
          localMsg = (msgAgente + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 3
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna + 2, linha)
          exibir(matriz, coluna + 1, linha)
          return p

        elif (linha - l) == 1 and contador == 4:
          localMsg = (msgAgente + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 4
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna + 2, linha - 1)
          exibir(matriz, coluna + 2, linha)
          exibir(matriz, coluna + 1, linha)
          return p
        
        elif (linha - l) == 2 and contador == 5: 
          localMsg = (msgAgente + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 5
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna + 2, linha - 2)
          exibir(matriz, coluna + 2, linha - 1)
          exibir(matriz, coluna + 2, linha)
          exibir(matriz, coluna + 1, linha)
          return p
        
        elif (linha - l) == 3 and contador == 6:
          localMsg = (msgAgente + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 6
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna + 2, linha - 3)
          exibir(matriz, coluna + 2, linha - 2)
          exibir(matriz, coluna + 2, linha - 1)
          exibir(matriz, coluna + 2, linha)
          exibir(matriz, coluna + 1, linha)
          return p

        #linha -
        elif (linha - l) == -1 and contador == 4:
          localMsg = (msgAgente + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 4
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna + 2, linha + 1)
          exibir(matriz, coluna + 2, linha)
          exibir(matriz, coluna + 1, linha)
          return p
        
        elif (linha - l) == -2 and contador == 5:
          localMsg = (msgAgente + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 5
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna + 2, linha + 2)
          exibir(matriz, coluna + 2, linha + 1)
          exibir(matriz, coluna + 2, linha)
          exibir(matriz, coluna + 1, linha)
          return p
        
        elif (linha - l) == -3 and contador == 6:
          localMsg = (msgAgente + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!') 
          msgAgente = localMsg
          localPontos = pontos + 6
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna + 2, linha + 3)
          exibir(matriz, coluna + 2, linha + 2)
          exibir(matriz, coluna + 2, linha + 1)
          exibir(matriz, coluna + 2, linha)
          exibir(matriz, coluna + 1, linha)
          return p
      
      #linha + 3 até linha + 3
      if (linha - l) == 3:

        #coluna +
        if (coluna - c) == 0 and contador == 3:
          localMsg = (msgAgente + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!') 
          msgAgente = localMsg
          localPontos = pontos + 3
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna, linha - 2)
          exibir(matriz, coluna, linha - 1)
          return p

        elif (coluna - c) == 1 and contador == 4:
          localMsg = (msgAgente + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!') 
          msgAgente = localMsg
          localPontos = pontos + 4
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna - 1, linha - 2)
          exibir(matriz, coluna, linha - 2)
          exibir(matriz, coluna, linha - 1)
          return p

        elif (coluna - c) == 2 and contador == 5:
          localMsg = (msgAgente + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!')
          msgAgente = localMsg 
          localPontos = pontos + 5
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna - 2, linha - 2)
          exibir(matriz, coluna - 1, linha - 2)
          exibir(matriz, coluna, linha - 2)
          exibir(matriz, coluna, linha - 1)
          return p

        elif (coluna - c) == 3 and contador == 6:
          localMsg = (msgAgente + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 6
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna - 3, linha - 2)
          exibir(matriz, coluna - 2, linha - 2)
          exibir(matriz, coluna - 1, linha - 2)
          exibir(matriz, coluna, linha - 2)
          exibir(matriz, coluna, linha - 1)
          return p

          #coluna -
        elif (coluna - c) == -1 and contador == 4:
          localMsg = (msgAgente + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 4
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna + 1, linha - 2)
          exibir(matriz, coluna, linha - 2)
          exibir(matriz, coluna, linha - 1)
          return p

        elif (coluna - c) == -2 and contador == 5:
          localMsg = (msgAgente + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 5
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna + 2, linha - 2)
          exibir(matriz, coluna + 1, linha - 2)
          exibir(matriz, coluna, linha - 2)
          exibir(matriz, coluna, linha - 1)
          return p

        elif (coluna - c) == -3 and contador == 6:
          localMsg = (msgAgente + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Direita. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 6
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna + 3, linha - 2)
          exibir(matriz, coluna + 2, linha - 2)
          exibir(matriz, coluna + 1, linha - 2)
          exibir(matriz, coluna, linha - 2)
          exibir(matriz, coluna, linha - 1)
          return p

      #linha - 3 até linha + 3
      if (linha - l) == -3:

        #coluna +
        if (coluna - c) == 0 and contador == 3:
          localMsg = (msgAgente + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 3
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna, linha + 2)
          exibir(matriz, coluna, linha + 1)
          return p

        elif (coluna - c) == 1 and contador == 4:
          localMsg = (msgAgente + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 4
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna - 1, linha + 2)
          exibir(matriz, coluna, linha + 2)
          exibir(matriz, coluna, linha + 1)
          return p

        elif (coluna - c) == 2 and contador == 5:
          localMsg = (msgAgente + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 5
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna - 2, linha + 2)
          exibir(matriz, coluna - 1, linha + 2)
          exibir(matriz, coluna, linha + 2)
          exibir(matriz, coluna, linha + 1)
          return p

        elif (coluna - c) == 3 and contador == 6:
          localMsg = (msgAgente + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!'
                                + '\nAção: Andar Abaixo. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 6
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna - 3, linha + 2)
          exibir(matriz, coluna - 2, linha + 2)
          exibir(matriz, coluna - 1, linha + 2)
          exibir(matriz, coluna, linha + 2)
          exibir(matriz, coluna, linha + 1)
          return p

          #coluna -
        elif (coluna - c) == -1 and contador == 4:
          localMsg = (msgAgente + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 4
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna + 1, linha + 2)
          exibir(matriz, coluna, linha + 2)
          exibir(matriz, coluna, linha + 1)
          return p

        elif (coluna - c) == -2 and contador == 5:
          localMsg = (msgAgente + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 5
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna + 2, linha + 2)
          exibir(matriz, coluna + 1, linha + 2)
          exibir(matriz, coluna, linha + 2)
          exibir(matriz, coluna, linha + 1)
          return p

        elif (coluna - c) == -3 and contador == 6:
          localMsg = (msgAgente + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Esquerda. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!'
                                + '\nAção: Andar Acima. + 1 ponto para o agente!')
          msgAgente = localMsg
          localPontos = pontos + 6
          pontos = localPontos
          listaPosicoesCaminhar.remove(p)
          exibir(matriz, coluna + 3, linha + 2)
          exibir(matriz, coluna + 2, linha + 2)
          exibir(matriz, coluna + 1, linha + 2)
          exibir(matriz, coluna, linha + 2)
          exibir(matriz, coluna, linha + 1)
          return p
    
    contador = contador + 1


#funcao para limpar uma posicao no ambiente
def limpar (matriz, c, l):

    #limpa a posicao (2 = sujo e 0 = limpo)
    matriz [c][l] = 0

    #atualiza a variavel global que guarda a quantidade de sujeira restante
    global qtdSujeira
    local = qtdSujeira - 1
    qtdSujeira = local   


#caminha por todo o ambiente, o limpando e exibindo cada movimento
def funcaoMapear (matriz, c, l, status):

  #reacao do agente
  reacao = agenteObjetivo (matriz, c, l, status, checkObj())

  #se reacao receber 'Devo parar!', ele cai fora do loop e a aplicacao para
  if reacao == 'Devo parar!':
    return

  #chama a funcao para printar a matriz atual
  exibir(matriz, reacao[0], reacao[1])

  #chama novamente a funcaoMapear para continuar mapeando o ambiente ate estiver limpo
  funcaoMapear(matriz, reacao[0], reacao[1], matriz[reacao[0]][reacao[1]])


def exibir(matriz, c , l):
       
  # Altera o esquema de cores do ambiente
  plt.imshow(matriz, 'gray')
  plt.nipy_spectral()
    
  # Coloca o agente no ambiente
  plt.plot([l],[c], marker='o', color='r', ls='')
  
  plt.show(block=False)
    
  # Pausa a execução do código por 0.5 segundos para facilitar a visualização
  plt.pause(0.5)    
  plt.clf()

#suja o ambiente
sujarAmbiente()

#printa a posicao inicial do agente e o ambiente com toda a sujeira (ambiente inicial)
exibir(matriz, 1 , 1)

#inicia o mapeamento
funcaoMapear(matriz, 1, 1, matriz[1][1])

#printa as acoes do agente e total de pontos que ele fez
print(msgAgente + '\nPontos = ' + str(pontos))