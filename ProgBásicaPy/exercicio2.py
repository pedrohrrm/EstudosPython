tempo = float(input('Digite o tempo que foi gasto na viagem:'))
velocidade = float(input('Digite a velocidade média:'))

distancia = tempo * velocidade
litrosUsados = distancia/12

print('Velocidade média:', velocidade)
print('Tempo gasto na viagem:', tempo)
print('Distancia percorrida:', distancia)
print('Quantidade de litros:', round(litrosUsados,1))