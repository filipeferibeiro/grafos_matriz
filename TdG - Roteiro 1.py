from grafo import Grafo

while True:

    vertices = input('Informe todos os vertices do Grafo separados por virgula e espaços e não podem conter esses caracteres : "-", "(" e ")". \nEX: J, B, C \n')
    vertices = vertices.replace(" " , "")
    N = vertices.split(',')

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


grafo = Grafo(N,dicionario)

print("\n")

adj = grafo.vet_adj()

print("Os vertices adjacentes são:", adj)

print("O grau do vertice c é:", grafo.grau_vet("c"))

print("As arestas do vertice c é:", grafo.arestas_vet("c"))

print("Este grafo é completo:", grafo.graf_complete())

# print("Este grafo é conexo é:", grafo.conexo())

print("Warshall: ",grafo.warshall())

print("euler: ", grafo.euleriano() )

confirm = 0
for i in range(len(grafo.road)):
    if confirm == 0:
        print("[", grafo.N[grafo.road[-1]], end = "")
        confirm = 1
    print(" -", grafo.N[grafo.road[i]], end = "")
    if i == (len(grafo.road) - 1):
        print(" ]")

'''
a, b, c
a1(a-b), a2(b-c), a3(c-a)

a, b, c, d, e, f, j
as(a-b), agx(a-j), asdf(b-c), gc(b-d), tfg(c-d), poiuytr(d-e), gyu(e-f), rdg(e-j), gtgt(f-b), ftrgn(f-c)
'''