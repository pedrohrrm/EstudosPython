def leitura ():
    tempo = float(input('Digite o tempo gasto com a viagem: '))
    velocidade = float(input('Digite a velocidade média: '))
    return tempo, velocidade

def calcularDistancia(tempo, velocidade):
    return tempo*velocidade

def calcularLitros(distancia):
    return distancia/12

def imprime( velocidade, tempo, distancia, litros):
    print('velocidade:', velocidade)
    print('Tempo: ', tempo)
    print('Distancia: ', distancia)
    print('Litros: ', litros)

t, v = leitura()
d = calcularDistancia(t, v)
l = calcularLitros(d)
imprime(v, t, d, l)
