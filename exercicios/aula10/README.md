# Exercícios


### Projeto de Classes 

Para esse conjunto de exercícios vamos utilizar o conjunto de dados
disponibilizado no dataset [MovieLens
100k](https://grouplens.org/datasets/movielens/100k/)


O conjunto de dados do MovieLens foi coletados pelo GroupLens Research Project
na Universidade de Minnesota.
 
Este conjunto de dados consiste em:
* 100.000 classificações (1-5) de 943 usuários em 1.682 filmes.
* Cada usuário classificou pelo menos 20 filmes.

O dataset original está espalhado em diversos arquivos. No [link](https://www.dropbox.com/s/5r6qfsfb2r2ou5c/ml-100k.csv.zip?dl=0), você tem
acesso a uma versão condensada em uma tabela dos dados das avaliações de filmes
feitas pelos usuários.
Utilizando a biblioteca [Pandas](https://pandas.pydata.org/), implemente
funções que realizem as seguintes tarefas:

#### Considerando os dados de avaliação dos usuários

1. Cálculo da média, desvio padrão e variância para o dataset de avaliações
   completo;
1. Cálculo de média, desvio padrão e variância para cada usuário (armazenar
   esses valores em novas colunas do dataset);
1. Encontrar indivíduos que avaliam filmes de forma mais uniforme, i.e.,
   avaliações estão próximo ao valor da média do indivíduo;
1. Encontrar indivíduos cujas avaliações são mais diversas, i.e., valores de
   avaliação muito negativos e positivos;
1. Encontrar indivíduos que avaliam filmes de forma excessivamente positiva,
   i.e., aqueles cuja média de avaliações está bem acima da média global;
  * Encontrar também os que estão bem abaixo.
  * Uma das formas de encontrar os indivíduos que estão muito longe do

#### Considerando os dados sobre filmes

1. Criar [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html?highlight=dataframe#pandas.DataFrame) que contenha informações sobre filmes:
| movie id | movie title | release date | video release date | IMDb URL |  unknown | Action | Adventure | Animation | Children's | Comedy | Crime | Documentary | Drama | Fantasy | Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi | Thriller | War | Western |
--------------------------------------------------------------------------------
|1|Toy Story (1995)|01-Jan-1995||http://us.imdb.com/M/title-exact?Toy%20Story%20(1995)|0|0|0|1|1|1|0|0|0|0|0|0|0|0|0|0|0|0|0|
|2|GoldenEye (1995)|01-Jan-1995||http://us.imdb.com/M/title-exact?GoldenEye%20(1995)|0|1|1|0|0|0|0|0|0|0|0|0|0|0|0|0|1|0|0|
|3|Four Rooms (1995)|01-Jan-1995||http://us.imdb.com/M/title-exact?Four%20Rooms%20(1995)|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|1|0|0|
|...|

1. Identificar qual gênero de filme possui o maior número de exemplos;
1. Verificar se existem dados faltando

1. Criar novo
   [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html?highlight=dataframe#pandas.DataFrame) que condense informações sobre o gênero do filme:

| movie id | movie title | release date | video release date | IMDb URL | genre|
--------------------------------------------------------------------------------
|1|Toy Story (1995)|01-Jan-1995||http://us.imdb.com/M/title-exact?Toy%20Story%20(1995)|Animation,Children's,Comedy|
|2|GoldenEye (1995)|01-Jan-1995||http://us.imdb.com/M/title-exact?GoldenEye%20(1995)|Action,Adventure,Thriller|
|3|Four Rooms (1995)|01-Jan-1995||http://us.imdb.com/M/title-exact?Four%20Rooms%20(1995)|Thriller|

...

1. Adicionar colunas que armazenem dados para o total de avaliações, a soma das
   avaliações, média, valor máximo (e mínimo), desvio padrão e variância;
1. Mostrar filmes com maior (e menor) número de avaliações;
1. Normalização é uma das tarefas mais importantes quando estamos preparando um
   dataset para utilizar algoritmos de Machine Learning. Implementar as
   seguintes estratégias de normalização:
   * [Normalização min-max](https://en.wikipedia.org/wiki/Feature_scaling#Rescaling_(min-max_normalization))
   * [Normalização pela média](https://en.wikipedia.org/wiki/Feature_scaling#Mean_normalization)
   * [Normalização Z-score](https://en.wikipedia.org/wiki/Feature_scaling#Standardization_(Z-score_Normalization))

