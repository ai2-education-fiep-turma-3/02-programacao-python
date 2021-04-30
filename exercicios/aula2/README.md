# Exercícios





### Sistemas de Recomendação

Para esse conjunto de exercícios vamos utilizar o dataset [MovieLens 100k](https://grouplens.org/datasets/movielens/100k/)


Os conjuntos de dados do MovieLens foram coletados pelo GroupLens Research Project na Universidade de Minnesota.
 
Este conjunto de dados consiste em:
* 100.000 classificações (1-5) de 943 usuários em 1.682 filmes.
* Cada usuário classificou pelo menos 20 filmes.
* Informações demográficas simples para os usuários (idade, sexo, ocupação, CEP)

Os dados foram coletados por meio do site MovieLens (movielens.umn.edu) durante o período de sete meses a partir de 19 de setembro, 1997 a 22 de abril de 1998. Estes dados foram limpos - usuários que tiveram menos de 20 avaliações ou não tiveram dados demográficos completos informações foram removidas deste conjunto de dados. Descrições detalhadas de o arquivo de dados pode ser encontrado no final deste arquivo.

Utilizando esse Dataset, implemente as seguintes funcionalidades. Você deverá utilizar somente as bibliotecas padrões do python, i.e., nenhuma nova biblioteca deve ser adicionada para implementar suas soluções. Faça a organização do seu código em módulos, realizando `import`s para reutilizar o código.
#### Funcionalidade:
1. Implementar o algoritmo de [Similaridade do
   Cosseno](https://pt.wikipedia.org/wiki/Similaridade_por_cosseno);
1. Implementar um Sistema de Recomendações, usando a técnica de Filtros
   Colaborativos baseados no usuário;
1. Implementar um Sistema de Recomendações, usando a técnica de Filtros
   Colaborativos baseados na similaridade entre os itens (filmes);
1. Implementar a [Medida de Correlação de
   Pearson](https://pt.wikipedia.org/wiki/Coeficiente_de_correla%C3%A7%C3%A3o_de_Pearson)
   como medida de similaridade;
