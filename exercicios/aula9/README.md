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
Utilizando a biblioteca [Numpy](https://numpy.org/), implemente as seguintes
funções:

1. Cálculo da média, desvio padrão e variância para todas as avaliações;
1. Cálculo de média, desvio padrão e variância para cada usuário (armazenar
   esses valores em novas colunas do dataset);
1. Encontrar indivíduos que avaliam filmes de forma mais uniforme, i.e.,
   avaliações estão próximo ao valor da média;
1. Encontrar indivíduos cujas avaliações são mais diversas, i.e., valores de
   avaliação muito negativos e positivos;
1. Encontrar indivíduos que avaliam filmes de forma excessivamente positiva,
   i.e., aqueles cuja média de avaliações está bem acima da média global;
  * Encontrar também os que estão bem abaixo.
  * Uma das formas de encontrar os indivíduos que estão muito longe do
    comportamento médio (**outliers**) é utilizando o método do desvio padrão,
    ou
    [Z-Score](https://blog.dp6.com.br/t%C3%A9cnicas-de-detec%C3%A7%C3%A3o-de-anomalias-3d9e216bf82e).
    Faça o cálculo do **Z-score** e verifique se existem outliers (considerar
    valores de Z maiores do que 3 para identificar esses indivíduos).
1. Implementar função que retorne o resultado da "**distância**" entre duas linhas utilizando o método de [Similaridade do
   Cosseno](https://en.wikipedia.org/wiki/Cosine_similarity);
   * Fazer o mesmo para colunas;
1. Implementar uma função que retorne o resultado da "**distância**" entre duas linhas utilizando o método da [Correlação de
   Pearson](https://pt.wikipedia.org/wiki/Coeficiente_de_correla%C3%A7%C3%A3o_de_Pearson);
   * Fazer o mesmo para colunas;

