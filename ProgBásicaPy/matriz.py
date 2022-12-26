import numpy as np
matriz = np.array([[2,3,1],[4,5,7]])
matriz.shape
print(matriz[1])

for i in range(matriz.shape[0]):
    print(matriz[i])
    for j in range(matriz.shape[1]):
        print(matriz[i],[j])