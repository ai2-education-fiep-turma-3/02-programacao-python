# Exercícios


### Projeto de Classes 

Para esse conjunto de exercícios vamos utilizar o dataset [MovieLens 100k](https://grouplens.org/datasets/movielens/100k/)


Os conjuntos de dados do MovieLens foram coletados pelo GroupLens Research
Project na Universidade de Minnesota.
 
Este conjunto de dados consiste em:
* 100.000 classificações (1-5) de 943 usuários em 1.682 filmes.
* Cada usuário classificou pelo menos 20 filmes.
* Informações demográficas simples para os usuários (idade, sexo, ocupação, CEP)

Os dados foram coletados por meio do site MovieLens (movielens.umn.edu) durante
o período de sete meses a partir de 19 de setembro, 1997 a 22 de abril de 1998.
Estes dados foram limpos - usuários que tiveram menos de 20 avaliações ou não
tiveram dados demográficos completos informações foram removidas deste conjunto
de dados. Descrições detalhadas de o arquivo de dados pode ser encontrado no
final deste arquivo.

Crie o seguinte conjunto de classes:

1. Classe `Usuário` contendo os dados relativos ao usuário (arquivo `u.user`) e
   com as seguintes responsabilidades:
  * Cálculo do valor médio de avaliações;
1. Classe `Filme` contendo os dados relativos ao filme (arquivo `u.item`) e com
   as seguintes responsabilidades:
  * Cálculo da avaliação média;
1. Classe `Gênero` contendo os dados relacionados ao gênero do filme (arquivo
   `u.genre`)
1. Classe `Profissão` contendo dados relacionados a ocupação dos usuários;
1. Classe `Avaliação` contendo dados das avaliações dos usuários (arquivo
   `u.data`);
1. Classe `SistemaDeRecomendação` com as seguintes responsabilidades:
  * Manter lista de usuários;
  * Manter lista de filmes;
  * Manter Lista de profissões;
  * Manter Lista de gêneros;
  * Adicionar novo usuário;
  * Adicionar novo filme;
  * Adicionar nova avaliação de filme;
