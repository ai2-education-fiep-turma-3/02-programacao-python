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

    def avaliar_filme(self, filme, nota):
        avaliacao = Avaliacao(self, filme, nota)
        self.adicionar_avaliacao(avaliacao)
        filme.adicionar_avaliacao(avaliacao)

    def as_numpy_array(self, tamanho):
        vetor_usuario = np.zeros(tamanho)
        for avaliacao in self.avaliacoes:
            #vetor_usuario[avaliacao.filme.id_filme-1] = avaliacao.nota
            vetor_usuario[int(avaliacao.filme.id_filme)-1] = int(avaliacao.nota)
        return vetor_usuario

class Filme:
    def __init__(self, id_filme, titulo, data_lancamento, url_imdb, generos):
        self.id_filme = id_filme
        self.titulo = titulo
        self.data_lancamento = data_lancamento
        self.url_imdb = url_imdb
        self.generos = generos
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
          self.usuarios = dict()           #self.usuarios = []
          self.filmes = dict()             #self.filmes = []
          self.generos = dict()            #self.generos = []


    def carregar_de_arquivos(self, diretorio):
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
                               campos[4]) # Utilizar *campos
                self.usuarios[usuario.id_usuario] = usuario
        except Exception as e:
            print(e)
            print(f"Erro na Abertura do arquivo {localizacao_arquivo}")
            sys.exit(1)

    def carregar_generos_do_arquivo(self, localizacao_arquivo):
        try:
            arquivo = open(localizacao_arquivo, 'r')
            for linha in arquivo:
                campos = linha.split("|")
                if(len(campos) == 2):
                    genero = Genero(campos[1], campos[0])
                    self.generos[genero.id_genero] = genero
        except Exception as e:
            print(e)
            print(f"Erro na Abertura do arquivo {localizacao_arquivo}")
            sys.exit(1)

    def carregar_filmes_do_arquivo(self, localizacao_arquivo):
        try:
            # Primeira tentativa sem o iso-8859-1
            # rodar o comando file -i u.item para descobrir encoding
            arquivo = open(localizacao_arquivo, 'r', encoding='iso-8859-1')
            for linha in arquivo:
                campos = linha.split("|")
                campos_generos = campos[5:-1]
                generos = []
                for i in range(len(campos_generos)):
                    if campos_generos[i] == 1:
                        generos.append(self.generos[i])

                filme = Filme(campos[0], campos[1], campos[2], campos[4], 
                              generos)
                self.filmes[filme.id_filme] = filme
        except Exception as e:
            print(e)
            print(f"Erro na Abertura do arquivo {localizacao_arquivo}")
            sys.exit(1)

    def carregar_avaliacoes_do_arquivo(self, localizacao_arquivo):
        try:
            arquivo = open(localizacao_arquivo, 'r', encoding='iso-8859-1')
            for linha in arquivo:
                campos = linha.split("\t")
                usuario = self.usuarios[campos[0]]
                filme = self.filmes[campos[1]]
                nota = campos[2]
                usuario.avaliar_filme(filme,nota)

        except Exception as e:
            print(e)
            print(f"Erro na Abertura do arquivo {localizacao_arquivo}")
            sys.exit(1)
    
    def total_usuarios(self):
        return len(self.usuarios)

    def total_filmes(self)
        return len(self.filmes)


rs = SistemaDeRecomendacao()
rs.carregar_de_arquivos("/tmp/movielens-100k/ml-100k")



# No Jupyter Console Utilizar 
# %loadext autoreload
# %autoreload 2


# Testes

# Leitura
# cat u.data | grep -e "^1\t" | wc -l
# len(rs.usuarios["1"].avaliacoes)

# Inspeção da Leitura
# cat u.data | grep -e "^3\t" | head -n5
# for i in range(5):
#     nota = rs.usuarios["3"].avaliacoes[i].nota
#     filme_id = rs.usuarios["3"].avaliacoes[i].filme.id_filme
#     print(f"{filme_id}\t{nota}")

# Recuperando numpy_array
# cat u.data | grep -e "^1\t" | grep -e "\t1\t"
# usuario_array = rs.usuarios["1"].as_numpy_array(rs.total_filmes)
# np.where(usuario_array != 0)
# usuario_array[0]


