from grafo import Grafo

while True:

    vertices = input('Informe todos os vertices do Grafo separados por virgula e espaços e não podem conter esses caracteres : "-", "(" e ")". \nEX: J, B, C \n')
    vertices = vertices.replace(" " , "")
    N = vertices.split(',')
    print(N)

    if "-" in vertices or "(" in vertices or ")" in vertices:
        print('Você utilizou caracteres proibidos\nTente Novamente\n')
    elif N == ['']:
        print('Não é possivél criar grafos sem vertices\nTente Novamente\n')
    else:
        break

while True:

    função_g = input('Informe as arestas seguido dos vértices que ela conecta. \nEX: a1(J-C), a2(C-E), a3(C-E)\n')
    A = função_g.split(', ')

    if '(' not in função_g or ')' not in função_g:
        print('Você não utilizou a formatação correta, utilize como informado.')
    else:
        break

dicionario = {}



for x in A:
    g = x.split('(')
    dicionario[g[0]] = g[1][0:-1]

print(dicionario)

grafo = Grafo(N,dicionario)

print("\n")

adj = grafo.vet_adj()

print(adj)

print(grafo.grau_vet("c"))

print(grafo.arestas_vet("c"))

print(grafo.graf_complete())

print('asdasda\n\n\n\n')

print(grafo.conexo())


'''
a, b, c
a1(a-b), a2(b-c), a3(c-a)
'''