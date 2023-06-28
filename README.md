# Polígonos com Turtle

Este é um script em Python que utiliza o módulo `turtle` para desenhar várias formas e desenhos usando um sistema de gráficos de tartaruga.

## Instalação

1. Certifique-se de ter o Python instalado em seu sistema.
2. Clone este repositório ou baixe o arquivo `turtle_drawing.py`.

## Uso

Para usar o script, siga estes passos:

1. Importe os módulos necessários:

   ```python
   import math
   from turtle import Turtle, mainloop
   ```

2. Defina as seguintes funções:

   - `square(t: Turtle)`: Desenha um quadrado usando o objeto turtle fornecido.
   - `polygon(t: Turtle, n: int, length: float)`: Desenha um polígono com `n` lados de comprimento `length`.
   - `circle(t: Turtle, r: float)`: Desenha um círculo com um raio `r` fornecido.
   - `arc(t: Turtle, r: float, angle: float)`: Desenha um arco com um raio `r` e ângulo `angle` fornecidos.
   - `polyline(t: Turtle, n: int, length: float, angle: float)`: Desenha `n` segmentos de linha com comprimento `length` e ângulo de `angle` graus entre eles.
   - `petal(t: Turtle, r: float, angle: float)`: Desenha uma pétala usando dois arcos.
   - `flower(t: Turtle, n: int, r: float, angle: float)`: Desenha uma flor com `n` pétalas usando a função `petal`.

3. Crie um objeto turtle:

   ```python
   my_turtle = Turtle()
   ```

4. Descomente as chamadas de função desejadas para desenhar formas ou desenhos:

   ```python
   square(my_turtle)
   polygon(my_turtle, 12, 50)
   circle(my_turtle, 200)
   flower(my_turtle, 12, 200, 45)
   ```

5. Execute o script:

   ```shell
   python turtle_drawing.py
   ```

6. A janela de gráficos da tartaruga aparecerá e você verá as formas ou desenhos sendo desenhados.

7. Feche a janela manualmente quando terminar.

## Licença

Este script está licenciado sob a [Licença MIT](LICENSE).

Sinta-se à vontade para modificá-lo e usá-lo de acordo com suas necessidades. Contribuições são bem-vindas!

## Agradecimentos

Ao escritor Allen B. Downey, e seu projeto no formato de livro 'Pense em Python'.

Aos mantenedores do projeto [Green Tea Press](https://greenteapress.com/wp/) que possibilita maior acessibilidade á conteúdos de qualidade.

O módulo de gráficos da tartaruga é baseado no trabalho original de Seymour Papert e na linguagem de programação LOGO.


## Referências:
  - Pense em Python, por Allen B. Downey
  - [Repositório](http://thinkpython2.com/code/flower.py)
