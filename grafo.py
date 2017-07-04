import copy
class VerticeInvalidoException(Exception):
    pass

class ArestaInvalidaException(Exception):
    pass

class Grafo:

    QTDE_MAX_SEPARADOR = 1
    SEPARADOR_ARESTA = '-'

    def __init__(self, N=[], A={}):
        '''
        Constrói um objeto do tipo Grafo. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param N: Uma lista dos vértices (ou nodos) do grafo.
        :param V: Uma dicionário que guarda as arestas do grafo. A chave representa o nome da aresta e o valor é uma string que contém dois vértices separados por um traço.
        '''
        self.N = N
        self.Matriz = []
        for i in range(len(N)):
            linha = []
            for j in range(len(N)):
                linha.append(0)
            self.Matriz.append(linha)

        for v in N:
            if not(Grafo.verticeValido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

        self.N = N

        for a in A:
            if not(self.arestaValida(A[a])):
                raise ArestaInvalidaException('A aresta' + A[a] + ' é inválida')

        self.A = A

        for i in A:
            for j in range(len(N)):
                if N[j] in A[i]:
                   A[i] = A[i].replace(N[j], str(j))

        for i in A:
            if self.Matriz[int(A[i][0])][int(A[i][2])] == '-':
                self.Matriz[int(A[i][2])][int(A[i][0])] += 1
            else:
                self.Matriz[int(A[i][0])][int(A[i][2])] += 1

        for i in range(len(N)):
            if i == 0:
                print(' ', end=' ')
            print(N[i], end=' ')

        for i in range(len(self.Matriz)):
            print('\n')
            for j in range(len(self.Matriz[i])):
                if j == 0:
                    print(N[i], end=' ')
                print(self.Matriz[i][j], end=' ')


    def arestaValida(self, aresta=''):
        '''
        Verifica se uma aresta passada como parâmetro está dentro do padrão estabelecido.
        Uma aresta é representada por um string com o formato a-b, onde:
        a é um substring de aresta que é o nome de um vértice adjacente à aresta.
        - é um caractere separador. Uma aresta só pode ter um único caractere como esse.
        b é um substring de aresta que é o nome do outro vértice adjacente à aresta.
        Além disso, uma aresta só é válida se conectar dois vértices existentes no grafo.
        :param aresta: A aresta que se quer verificar se está no formato correto.
        :return: Um valor booleano que indica se a aresta está no formato correto.
        '''

        # Não pode haver mais de um caractere separador
        if aresta.count(Grafo.SEPARADOR_ARESTA) != Grafo.QTDE_MAX_SEPARADOR:
            return False

        # Índice do elemento separador
        i_traco = aresta.index(Grafo.SEPARADOR_ARESTA)

        # O caractere separador não pode ser o primeiro ou o último caractere da aresta
        if i_traco == 0 or aresta[-1] == Grafo.SEPARADOR_ARESTA:
            return False

        if not(self.existeVertice(aresta[:i_traco])) or not(self.existeVertice(aresta[i_traco+1:])):
            return False

        return True

    @classmethod
    def verticeValido(self, vertice=''):
        '''
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio e nem conter o caractere separador.
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        '''
        return vertice != '' and vertice.count(Grafo.SEPARADOR_ARESTA) == 0

    def existeVertice(self, vertice=''):
        '''
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        '''
        return Grafo.verticeValido(vertice) and self.N.count(vertice) > 0

    def existeAresta(self, aresta=''):
        '''
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        '''
        existe = False
        if Grafo.arestaValida(self, aresta):
            for k in self.A:
                if aresta == self.A[k]:
                    existe = True

        return existe

    def adicionaVertice(self, v):
        if self.verticeValido(v):
            self.N.append(v)
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adicionaAresta(self, nome, a):
        if self.arestaValida(a):
            self.A[nome] = a
        else:
            ArestaInvalidaException('A aresta ' + self.A[a] + ' é inválida')

    def vet_adj(self):
        adj_list = []
        for i in range(len(self.Matriz)):
            for j in range(len(self.Matriz[i])):
                if self.Matriz[i][j] == 0:
                    adj_list.append(str(self.N[i] + "-" + self.N[j]))
        return adj_list

    def vet_adj_self(self):
        for i in range(len(self.Matriz)):
            if self.Matriz[i][i] == 0:
                return True
        return False

    def ars_paralelas(self):
        for i in range(len(self.Matriz)):
            for j in range(len(self.Matriz[i])):
                if self.Matriz[i][j] > 1:
                    return True
        return False

    def grau_vet(self, vertice):
        if vertice not in self.N:
            return False
        grau = 0
        for i in range(len(self.N)):
            if self.N[i] == vertice:
                vertice = i
                break
        for i in range(len(self.Matriz)):
            if self.Matriz[i][vertice] != "-" and self.Matriz[i][vertice] > 0:
                grau += self.Matriz[i][vertice]
            if self.Matriz[vertice][i] != "-" and self.Matriz[vertice][i] > 0:
                grau += self.Matriz[vertice][i]
        return grau

    def arestas_vet(self, vertice):
        if vertice not in self.N:
            return False
        arestas = []
        for i in range(len(self.N)):
            if self.N[i] == vertice:
                vertice = i
                break
        for i in range(len(self.Matriz)):
            if self.Matriz[i][vertice] != "-" and self.Matriz[i][vertice] > 0:
                for j in range(self.Matriz[i][vertice]):
                    arestas.append(str(self.N[i] + "-" + self.N[vertice]))
            if self.Matriz[vertice][i] != "-" and self.Matriz[vertice][i] > 0:
                for k in range(self.Matriz[vertice][i]):
                    arestas.append(str(self.N[vertice] + "-" + self.N[i]))
        return arestas

    def graf_complete(self):
        cont = 0
        for i in range(len(self.Matriz)):
            for j in range(len(self.Matriz[i])):
                if self.Matriz[i][j] == 0:
                    cont += 1
        if cont > len(self.N):
            return False

        return True

    def conexo(self, i = 0):
        if i <= (len(self.Matriz) - 2):
            if 1 not in self.Matriz[i]:
                coluna = self.coluna()
                if coluna == True:
                    return True
                else:
                    return False

            a = self.conexo(i+1)
            if a == True:
                return True
            else:
                return False

        else:
            return True

    def coluna(self, j = 1):
        lista = []
        for x in range(len(self.Matriz)):
            if self.Matriz[x][j] == 1:
                lista.append(1)
        if lista == []:
            return False
        elif j == len(self.Matriz):
            return True
        else:
            a = self.coluna(j + 1)
            if a == True:
                return True
            else:
                return False

    def warshall(self):
        n = len(self.Matriz)
        war_matriz = copy.deepcopy(self.Matriz)

        for i in range(n):
            for j in range(n):
                if war_matriz[j][i] > 0:
                    war_matriz[j][i] = 1
                    for k in range(n):
                        war_matriz[j][k] = max(war_matriz[j][k], war_matriz[i][k])

    def __str__(self):
        '''
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato padrão.
        :return: Uma string que representa o grafo
        '''
        grafo_str = ''

        for v in range(len(self.N)):
            grafo_str += self.N[v]
            if v < (len(self.N) - 1):  # Só coloca a vírgula se não for o último vértice
                grafo_str += ", "

        grafo_str += '\n'

        for i, a in enumerate(self.A):
            grafo_str += self.A[a]
            if not(i == len(self.A) - 1): # Só coloca a vírgula se não for a última aresta
                grafo_str += ", "

        return grafo_str