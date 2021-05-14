import sys
import numpy as np

class Usuario:
    def __init__(self, id_usuario, idade, genero, ocupacao, cep):
        self.id_usuario = id_usuario
        self.idade = idade
        self.genero = genero
        self.ocupacao = ocupacao
        self.cep = cep
        self.avaliacoes = []

    def adicionar_avaliacao(self, avaliacao):
        self.avaliacoes.append(avaliacao)
        # self.avaliacoes[avaliacao.filme.id_filme] = avaliacao

    def avaliar_filme(self, filme, nota):
        avaliacao = Avaliacao(self, filme, nota)
        self.adicionar_avaliacao(avaliacao)
        filme.adicionar_avaliacao(avaliacao)
        # filme.avaliacoes.append(avaliacao)
        # filme.avaliacoes[usuario.id_usuario] = avaliacao
    
    def as_numpy_array(self, tamanho):
        vetor_usuario = np.zeros(tamanho)
        for avaliacao in self.avaliacoes:
            vetor_usuario[int(avaliacao.filme.id_filme)-1] = int(avaliacao.nota)

        return vetor_usuario
    
    def similaridade(self, outro_usuario,tamanho, algoritmo_de_similaridade):
        return algoritmo_de_similaridade.calcula(self.as_numpy_array(tamanho), 
                                         outro_usuario.as_numpy_array(tamanho))


class Filme:
    def __init__(self, id_filme, titulo, data_lancamento, url_imdb, generos):
        self.id_filme = id_filme
        self.titulo = titulo
        self.data_lancamento = data_lancamento
        self.url_imdb = url_imdb
        self.generos = generos # Lista de Genero
        self.avaliacoes = []

    def adicionar_avaliacao(self, avaliacao):
        self.avaliacoes.append(avaliacao)

class Genero:
    def __init__(self, id_genero, nome):
        self.id_genero = id_genero
        self.nome = nome
        

class Avaliacao:
    def __init__(self, usuario, filme, nota):
        self.usuario = usuario
        self.filme = filme
        self.nota = nota

class SistemaDeRecomendacao:
    def __init__(self):
        self.usuarios = dict() # self.usuarios['1']
        self.filmes = dict()
        self.generos = dict()

    def carregar_do_diretorio(self, diretorio):
        self.carregar_usuarios_do_arquivo(f"{diretorio}/u.user")
        self.carregar_generos_do_arquivo(f"{diretorio}/u.genre")
        self.carregar_filmes_do_arquivo(f"{diretorio}/u.item")
        self.carregar_avaliacoes_do_arquivo(f"{diretorio}/u.data")

    def carregar_usuarios_do_arquivo(self, localizacao_arquivo):
        try:
            arquivo = open(localizacao_arquivo, 'r')
            for linha in arquivo:
                campos = linha.split("|")
                usuario = Usuario(campos[0], campos[1], campos[2], campos[3],
                                  campos[4])
                #self.usuarios.append(usuario)
                self.usuarios[usuario.id_usuario] = usuario 
        except Exception as e:
            print(e)
            sys.exit(1)

    def carregar_generos_do_arquivo(self, localizacao_arquivo):
        try:
            arquivo = open(localizacao_arquivo, 'r')
            for linha in arquivo:
                campos = linha.split("|")
                # Assume que não existe linha em branco no fim do arquivo
                genero = Genero(id_genero=campos[1].rstrip(), nome=campos[0])
                #self.generos.append(genero)
                self.generos[genero.id_genero] = genero
        except Exception as e:
            print(e)
            sys.exit(1)

    def carregar_filmes_do_arquivo(self, localizacao_arquivo):
        try:
            arquivo = open(localizacao_arquivo, 'r', encoding='iso-8859-1')
            for linha in arquivo:
                campos = linha.split("|")
                generos = []
                campos_generos = campos[5:-1]
                # Carrega Genero baseado na posição no Slice campos[5:-1]
                for i in range(len(campos_generos)):
                    if campos_generos[i] == "1":
                        generos.append(self.generos[str(i)])

                filme = Filme(campos[0], campos[1], campos[2], campos[4], 
                              generos)
                self.filmes[filme.id_filme] = filme

        except Exception as e:
            print(e)
            sys.exit(1)

    def carregar_avaliacoes_do_arquivo(self, localizacao_arquivo):
        try:
            arquivo = open(localizacao_arquivo, 'r')
            for linha in arquivo:
                campos = linha.split("\t")
                usuario = self.usuarios[campos[0]]
                filme = self.filmes[campos[1]]
                nota = int(campos[2])
                usuario.avaliar_filme(filme, nota)

        except Exception as e:
            print(e)
            sys.exit(1)



sr = SistemaDeRecomendacao()
sr.carregar_do_diretorio("/home/rmcobe/movielens-100k/ml-100k")

