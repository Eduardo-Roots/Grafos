# -*- coding: utf-8 -*-

def inicializaMatriz():
    for i in range(vertices):
        newLine = []

        for j in range(vertices):
            newLine.append(0)
        grafo.append(newLine)

def exibeMatriz():
    for i in range(vertices):
        for j in range(vertices):
            print("\t\t", grafo[i][j], end = "\t")
        print("\n\n")

def addAresta(line, column):

    grafo[line- 1][column - 1] += 1


def add(resp):
    if(resp != 's'):
        print("\nOk, parei de adicionar!\n\n")
        return
    elif((resp == 's') or (resp == 'S')):
        addLine = int(input("Digite em qual linha queres adicionar aresta: "))
        addColumn = int(input("Digite em qual coluna queres adicionar aresta: "))

        if(addLine and addColumn > vertices):
            print("Numero invalido")
        else:
            addAresta(addLine, addColumn)
            exibeMatriz()

        resp = input("Deseja adicionar mais vertices? [s _] ")
        print(resp)
       
def maiorGrauVertice():
    maior = grafo[0][0]
    for i in range(vertices):
        for j in range(vertices):
            if(maior >  grafo[i][j]):
                maior = grafo[i][j]
    return maior

def menorGrauVertice():
    menor = grafo[0][0]
    for i in range(vertices):
        for j in range(vertices):
            if(menor <  grafo[i][j]):
                menor = grafo[i][j]
    return menor


grafo = []
vertices = int(input("Digite a quantidade de vertices: "))
print("\nQuantidade de vertices: ", vertices)

print("\t----------------------------Matriz Gerada:---------------------------\n")

inicializaMatriz()
exibeMatriz()

print("\t----------------------------------------------------------------------")

question = 's'
while question == 's':


    print("\n\n\t----Hora de adicionar os  vertices----\n")
    add('s')
    question = input("Deseja continuar adicionando? [s/n] ")
    if((question != 's') or (question != 'S') or (question != 'n') or (question != 'N')):
       print("Opção Inválida!!!")
    else:
       add(question)

print("----Exibindo Grafo----")
exibeMatriz()

print("----Grau Máximo----")
maiorVertice = maiorGrauVertice()
print("Maior grau do Grafo: ", maiorVertice)

print("----Grau Mínimo----")
menorVertice = menorGrauVertice()
print("Menor grau do Grafo: ", menorVertice)
