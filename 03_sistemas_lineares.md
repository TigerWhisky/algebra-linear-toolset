# Sistemas de Equações Lineares

Um sistema linear pode ser escrito na forma matricial:

\[
A\mathbf{x} = \mathbf{b}
\]

## Métodos Implementados

### Eliminação de Gauss
Transforma a matriz aumentada \([A|b]\) numa matriz triangular superior e depois faz substituição regressiva.

### Metodo Gauss-Jordan
Continua o processo até obter a matriz identidade (forma reduzida por linhas).

## Casos Especiais

- Sistema determinado (solução única)
- Sistema indeterminado (infinitas soluções)
- Sistema impossível (sem solução)

Código em `src/systems.py`.
