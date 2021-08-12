def inicializaMatriz():

    for i in range(vertices):
        newLine = []

        for j in range(vertices):
            newLine.append(0)
        grafo.append(newLine)

def exibeMatriz():

    for i in range(vertices):

        for j in range(vertices):
            print(grafo[i][j], end = " ")
        print("")

def addAresta(line, column):

    grafo[line- 1][column - 1] += 1


def add():
    resposta = 's'
    while resposta == 's':

        addLine = int(input("Digite a linha para adiconar aresta: "))
        addColumn = int(input("Digite a coluna para adiconar aresta: "))

        if(addLine and addColumn > vertices):
            print("Numero invalido")
        else:
            addAresta(addLine, addColumn)
            exibeMatriz()

        resposta = input("Deseja adicionar mais vertices? [s/n] ")


def maiorGrauVertice():

    for i in range(vertices):

        for j in range(vertices):
            if(grafo[i][j] >  grafo[i][j + 1]):
                maior = grafo[i][j]
            else:
                maior = grafo[i][j + 1]
    return maior


def menorGrauVertice():

    for i in range(vertices):

        for j in range(vertices):
            if(grafo[i][j] <  grafo[i][j + 1]):
                menor = grafo[i][j]
            else:
                menor = grafo[i][j + 1]
    return menor


grafo = []
vertices = int(input("Digite a quantidade de vertices desejada: "))
print("Quantidade de vertices escolhida foi: ", vertices)

print("----Inicializando Matriz----")

inicializaMatriz()
exibeMatriz()
print("----Matriz Inicializada----")

question = 's'
while question == 's':


    print("----Hora de adicionar os  vertices----")
    add()
    question = input("Deseja continuar adicionando? [s/n] ")


print("----Exibindo Grafo----")
exibeMatriz()

print("----Maior Grau----")
maiorVertice = maiorGrauVertice()
print("Maior grau do Grafo: ", maiorVertice)


print("----Menor Grau----")
menorVertice = menorGrauVertice()
print("Menor grau do Grafo: ", menorVertice)
