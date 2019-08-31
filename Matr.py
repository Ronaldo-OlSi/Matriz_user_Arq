"""
#recebe uma matriz do usuario

def exibir_matriz(matr):
    for lin in matr:
        print(lin)

M = int(input("Numero das linhas: "))
N = int(input("Numero de colunas: "))

matr = []
for i in range(M):
    lin = []
    for j in range(N):
        E = input("Elementos linha {}, coluna {} ".format(i, j))
        lin.append(float(E))
    matr.append(lin)

exibir_matriz(matr)
"""

# recebe uma matriz de um arquivo

def exibir_matriz(matr):
    for lin in matr:
        print(lin)

arquivo = open("matriz5x5.txt", "r")

matr = []

lin = arquivo.readline()
while lin != "":
    element = lin.split()
    for n in range(len(element)):
        element[n] = float(element[n])
    matr.append(element)

    lin = arquivo.readline()

arquivo.close()

exibir_matriz(matr)

