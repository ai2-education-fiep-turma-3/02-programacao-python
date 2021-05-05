# Exercícios


### Projeto de Classes 

Crie o seguinte conjunto de classes, atributos e responsabilidades:

1. `FormaGeometrica`:
  * Atributos `x` e `y` que marcam a posição inicial da forma geométrica
  * Método `desenhe()` que deve mostrar o texto: `Desenho da Forma Geométrica`


1. `Forma2D`
  * Superclasse: `FormaGeometrica`;

1. `Forma3D`
  * Superclasse: `FormaGeometrica`

1. `Poligono`
  * Superclasse: `Forma2D`

1. `Quadrado`
  * Superclasse: `Retangulo`

1. `Retangulo`
  * Superclasse: `Poligono`

1. `Circulo`
  * Superclasse: `Forma2D`

1. `Esfera`
  * Superclasse: `Forma3D`

1. `Cubo`
  * Superclasse: `Forma3D`

1. `Cilindro`
  * Superclasse: `Forma3D`


Implemente operações que calculem a **área**, **perímetro** e **volume** das
formas quando cabível.

Para todas as subclassses de `FormaGeometrica` reimplemente o método `desenhe`.
Esse método deve escrever o nome da classe, a posição inicial/central da
forma e área, perímetro e volume; Lembre-se que, para figuras 3D , é necessária
a adição de um novo atributo, que guardará a coordenada na terceira dimensão.


Criar uma nova classe chamada `Quadro`. Essa classe deve ter, como atributo,
uma lista de figuras geométricas chama `figuras_geometricas`. 

Implemente o método `desenhe()` na classe `Quadro`. Esse método deve chamar a
função `desenhe()` de todos os objetos contidos na lista armazenada em `Quadro`

Adicionar métdos para \textbf{incluir} uma nova figura e \textbf{remover} uma
figura armazenada em uma dada posição da lista. 

### Extra

Pense e discuta com colegas sobre as dificuldades que teriam para implementar
um método `remover` na classe `Quadro`, para o qual apenas fosse passado o
objeto que se quer remover. Como seria possível implementar isso sem precisar
perguntar as instâncias contidas na lista `figuras_geometricas` a qual tipo
elas pertencem? 

**Dica**: dar uma olhada na técnica [Double
Dispatch](https://en.wikipedia.org/wiki/Double_dispatch)


