# Exercícios



### Jupyter Notebooks/Markdown 



#### Exercício 1:

Reproduza o seguinte
[README](assets/markdown.pdf)
utilizando `markdown` no Jupyter notebook.


#### Exercício 2:

O `markdown` não possibilita que redimensionemos a imagem usando a sintaxe
`![image_alt](image_path)`.  Pesquise uma maneira de inserir a seguinte imagem
e redimensioná-la no jupyter notebook. 


#### Exercício 3:

Como escrever (utilizando uma célula `markdown`) em texto simples os símbolos
utilizados pela sintaxe ( `*, #, _ **`)?

Imagem exemplo:
![](assets/lorem.png)

#### Exercício 4:

Instale o a ferramente `matplotlib` usando o `conda` utilizando uma célula do
`jupyter notebook`.  **Dica 1:** insira `-y` no final do comando de instalação
para que ele não espere sua confirmação para instalação.

**Dica 2:** Pode ser necessário reiniciar o `kernel` para que o pacote
instalado seja identificado pelo `jupyter`. Para fazê-lo: aba superior **Kernel
->  Restart**.

Execute o seguinte trecho de código no `jupyter notebook`:



```
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

plt.show()

```

Se precisar, instale utilizando `conda` os pacotes que estiverem faltando no
ambiente.

Obs.: Em módulos futuros, será explicado como utilizar a lib `matplotlib`.

#### Exercício 5

Utilize o repositório [profiles](https://github.com/ai2-education-fiep-turma-3/resident-profiles), criar um novo diretório no formato `nome-sobrenome` (utilizar último sobrenome - não utilizar letras maiúsculas). Criar um novo `README.md` no seu diretório contendo o seu perfil (como uma espécie de mini CV) utilizando `Markdown`.



### Python warmup

Para esse conjunto de exercícios vamos utilizar o dataset [MovieLens 100k](https://grouplens.org/datasets/movielens/100k/)


Os conjuntos de dados do MovieLens foram coletados pelo GroupLens Research Project na Universidade de Minnesota.
 
Este conjunto de dados consiste em:
* 100.000 classificações (1-5) de 943 usuários em 1.682 filmes.
* Cada usuário classificou pelo menos 20 filmes.
* Informações demográficas simples para os usuários (idade, sexo, ocupação, CEP)

Os dados foram coletados por meio do site MovieLens (movielens.umn.edu) durante o período de sete meses a partir de 19 de setembro, 1997 a 22 de abril de 1998. Estes dados foram limpos - usuários que tiveram menos de 20 avaliações ou não tiveram dados demográficos completos informações foram removidas deste conjunto de dados. Descrições detalhadas de o arquivo de dados pode ser encontrado no final deste arquivo.

Utilizando esse Dataset responda as seguintes perguntas. Você deverá utilizar somente as bibliotecas padrões do python, i.e., nenhuma nova biblioteca deve ser adicionada para implementar suas soluções (**isso é um warmup de python!**)
#### Encontrar:
1. O(s) usuário(s) mais crítico(s) na avaliação de filmes.
    * Encontrar aquele id cujas notas são, em média, as menores;
1. O(s) filme(s) mais mal avaliado(s) pelos usuários.
1. O(s) filme(s) mais bem avaliado(s) pelos usuários.
1. Média de avaliação para cada gênero de filmes;
1. Avaliação média de filmes por ano. 
    * Listar qual o ano com a melhor média de avaliação de filmes;
1. Qual a ocupação mais propensa a dar más avaliações a filmes;
    * Encontrar a média de avaliação para cada ocupação de usuário e mostrar os menores e maiores valores
