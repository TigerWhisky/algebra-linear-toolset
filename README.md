# Algebra Linear Toolset

Ferramenta educativa completa de **Álgebra Linear** desenvolvida em Python puro (sem dependências obrigatórias) e com suporte opcional a NumPy.

Este repositório foi criado para demonstrar compreensão sólida dos conceitos fundamentais de Álgebra Linear e a sua implementação computacional.

## Objetivos

- Implementar operações com vetores e matrizes do zero
- Resolver sistemas de equações lineares (Eliminação de Gauss e Gauss-Jordan)
- Calcular determinantes e matrizes inversas
- Calcular valores e vetores próprios
- Fornecer documentação clara e exemplos práticos

## Estrutura

| Pasta / Ficheiro       | Conteúdo                                      |
|------------------------|-----------------------------------------------|
| `src/`                 | Implementações principais                     |
| `docs/`                | Explicações teóricas                          |
| `examples/`            | Exemplos de utilização                        |
| `requirements.txt`     | Dependências opcionais                        |

## Instalação

```bash
# Clonar o repositório
git clone https://github.com/TEU_USER/algebra-linear-toolset.git
cd algebra-linear-toolset

# (Opcional) Instalar NumPy para comparações
pip install -r requirements.txt

#Utilização Rápida

Pythonfrom src.vector import Vector
from src.matrix import Matrix
from src.systems import solve_system
from src.determinants import determinant
from src.eigenvalues import power_method

# Vetores
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
print(v1 + v2)
print(v1.dot(v2))

# Matrizes
A = Matrix([
    [2, 1, 1],
    [1, 3, 2],
    [1, 0, 0]
])
print(A.transpose())
print(A * A)

# Sistema linear
b = Vector([1, 2, 3])
x = solve_system(A, b)
print(x)

Conceitos Implementados
Vetores (soma, produto escalar, norma, ângulo)
Matrizes (soma, multiplicação, transposta, potência)
Eliminação de Gauss e Gauss-Jordan
Determinante (método de Laplace e eliminação)
Matriz inversa
Valores e vetores próprios (método da potência)

# Acrescentada uma secção de tests 

O projeto inclui uma bateria completa de testes unitários.

# Instalar dependências de teste
pip install -r requirements.txt

# Correr todos os testes
pytest

# Correr com mais detalhe
pytest -v
