# Exercícios


### Projeto de Classes 

Continuando o projeto de classes que representam formas geométricas, fazer as
seguintes modificações:

1. Utilizar a estratégia de *Double Dispatching*  para implementar o método
   `remover` sem que seja necessário realizar perguntas sobre o tipo de objetos
   conforme visto em aula.
   * Usar a mesma estratégia para implementar o método `contem()`, que
     verifica se uma forma geométrica já está na lista da classe `Quadro`.

1. Transformar a classe `FormaGeometrica` em uma classe abstrata, definindo o
   método `desenhe()` como abstrato;
  * Fazer o mesmo com as classes `Forma2D`, `Forma3D` e `Poligono`, definindo
    os métodos que calculem a àrea, perímetro e volume como abstratos quando
    couber.

1. Implementar código que lance as seguintes Exceções:
  * No método de remoção que recebe um índice, como parâmetro, verificar se
    esse índice é um valor válido. Caso não seja, lançar uma exceção que
    notifique que se trata de um valor inválido. Verificar também o tipo do
    parâmetro recebido e, caso não seja do tipo inteiro, lançar uma exceção de
    tipo.
  * Implemente uma Exceção personalizada que notifique o usuário que uma forma
    não foi encontrada.
  * Implementar uma Exceção personalizada que notifique o usuário que uma dada
    forma não foi removida da lista, quando o método `remover`, do exercício do
    **ítem 1** for chamado
  * Alterar o construtor da classe `Quadro` para receber como parâmetro o
    tamanho máximo de objetos que podem estar contidos na mesma;
      * Lançar uma Exceção personalizada que notifique o usuário que este está
        tentando adicionar mais formas geométricas do que o que é comportado
        pela classe `Quadro`.
 
