# Algoritmo de Seleção Simultânea do Maior e do Menor Elementos (MaxMin Select) em Python

## Introdução
Este projeto implementa o algoritmo **MaxMin Select**, que encontra simultaneamente o maior e o menor elemento de um array utilizando a abordagem de **divisão e conquista**. O método reduz o número de comparações necessárias em relação a abordagens ingênuas.

# Descrição do Projeto: MaxMin Select

## Introdução

Este projeto implementa o algoritmo **MaxMin Select**, que encontra simultaneamente o maior e o menor elemento de um array utilizando a abordagem de **divisão e conquista**. O método reduz o número de comparações necessárias em relação a abordagens ingênuas.

## Explicação do Algoritmo

O algoritmo segue os seguintes passos:

1. **Caso Base**:

   - Se a lista contiver apenas um único elemento, ele será ao mesmo tempo o maior e o menor valor, pois não há mais elementos para comparação.
   - Se a lista contiver exatamente dois elementos, basta compará-los diretamente para identificar qual é o menor e qual é o maior. Esta comparação é feita de forma direta e retorna o resultado imediatamente.

2. **Divisão do Problema**:

   - Se a lista contém mais de dois elementos, ela é dividida em duas partes aproximadamente iguais. Isso reduz o tamanho do problema em cada nível da recursão, facilitando a solução dos subproblemas.

3. **Resolução Recursiva**:

   - O algoritmo é chamado recursivamente para encontrar os valores mínimos e máximos em cada uma das duas metades da lista. Ou seja, ele divide o problema original em partes menores e resolve cada uma separadamente.
   - Esse processo continua até que cada subproblema seja reduzido a um caso base, onde a comparação direta pode ser feita.

4. **Combinação dos Resultados**:

   - Após resolver os subproblemas menores, os resultados são combinados.
   - O menor valor final da lista completa será o menor entre os valores mínimos encontrados nas duas metades.
   - O maior valor final da lista completa será o maior entre os valores máximos encontrados nas duas metades.
   - Essa combinação dos resultados permite que o algoritmo retorne a resposta correta sem precisar comparar todos os elementos diretamente.

## Dependências

Este projeto não requer bibliotecas externas, apenas Python 3.

## Versão Pyhton

Versão 3.13.2

## Como executar o projeto

1. Certifique-se de ter o **Python 3** instalado.

2. Clone este repositório:
 ```bash
 git clone https://github.com/renatoctti/Trabalho-individual-2.git
 ```
   
3. O código testa automaticamente diversas combinações de numeros e retorna os resultados. Para rodar o codigo execute o script com o seguinte comando:

```bash
python main.py
```

## Explicacao da implementação Linha a Linha
```python
# Função principal que encontra o menor e maior elemento usando divisão e conquista
def max_min_select(arr, left, right):
```
- A função recebe como entrada um array `arr` e os índices `left` (início) e `right` (fim).

```python
    # Caso base: um único elemento
    if left == right:
        return arr[left], arr[left]
```
- Se houver apenas um elemento, ele é retornado como sendo tanto o menor quanto o maior.

```python
    # Caso base: dois elementos
    if right == left + 1:
        if arr[left] < arr[right]:
            return arr[left], arr[right]
        else:
            return arr[right], arr[left]
```
- Se houver dois elementos, eles são comparados diretamente.

```python
    # Divide o array ao meio
    mid = (left + right) // 2
```
- O array é dividido ao meio, calculando o índice `mid`.

```python
    min1, max1 = max_min_select(arr, left, mid)
    min2, max2 = max_min_select(arr, mid + 1, right)
```
- O algoritmo é chamado recursivamente para a primeira e a segunda metade.

```python
    # Combina os resultados
    return min(min1, min2), max(max1, max2)
```
- O menor valor global é o menor entre `min1` e `min2`.
- O maior valor global é o maior entre `max1` e `max2`.

# Análise da Complexidade Assintótica

## Método de Contagem de Operações
O algoritmo **MaxMin Select** reduz o número de comparações necessárias para encontrar o maior e o menor elemento de uma lista. Vamos analisar o número de operações realizadas em cada etapa do algoritmo.

### 1. Contagem de Comparações

- **Caso Base:**
  - Quando `n = 1`, não há comparações.
  - Quando `n = 2`, ocorre **1 comparação**.

- **Divisão Recursiva:**
  - O array é dividido em duas partes de tamanho `n/2`.
  - O algoritmo é chamado **duas vezes**, uma para cada metade.

- **Combinação dos Resultados:**
  - Depois de obter os menores e maiores valores das duas metades, precisamos de **duas comparações** para encontrar o menor global e o maior global.

Portanto, a relação de recorrência do número de comparações é:
```
C(n) = C(n/2) + C(n/2) + 2
```
O que resulta em:
```
C(n) = 2C(n/2) + 2
```
Expandindo a recorrência:
```
C(n) = 2[2C(n/4) + 2] + 2 = 4C(n/4) + 4 + 2
C(n) = 8C(n/8) + 8 + 4 + 2
...
C(n) = 2^k C(n / 2^k) + 2^k - 2
```
Como `n / 2^k = 1` quando `k = log_2 n`, temos:
```
C(n) = 2^(log_2 n) C(1) + 2^(log_2 n) - 2
```
Sabendo que `2^(log_2 n) = n`, então:
```
C(n) = n - 1 + 2n - 2 = 3n/2 - 2
```

### 2. Complexidade Assintótica
A complexidade assintótica do algoritmo é **O(n)**, pois o número de comparações cresce linearmente em relação ao tamanho da entrada.

Essa abordagem é mais eficiente do que uma comparação ingênua, que requer **2(n - 1) ≈ O(n)** comparações, mas ainda se mantém na mesma classe de complexidade **O(n)**.

## Utilizando o Teorema Mestre

### Recorrência do Algoritmo MaxMin Select
O algoritmo segue a recorrência:

\[
T(n) = 2T(n/2) + O(1)
\]

Para encontrar a complexidade assintótica, aplicamos o **Teorema Mestre**, que resolve recorrências da forma:

\[
T(n) = aT(n/b) + f(n)
\]

### **1. Identificação dos valores de \(a\), \(b\) e \(f(n)\):**
Comparando com a equação do Teorema Mestre:
- **\( a = 2 \)** (o problema é dividido em duas partes)
- **\( b = 2 \)** (cada parte tem metade do tamanho)
- **\( f(n) = O(1) \)** (custo constante para combinar os resultados)

### **2. Cálculo de \( \log_b a \) para determinar \( p \):**

\[
 p = \log_2 2 = 1
\]

### **3. Determinação do Caso do Teorema Mestre**
Os três casos do Teorema Mestre são:
1. Se \( f(n) = O(n^c) \) com \( c < p \), então \( T(n) = O(n^p) \).
2. Se \( f(n) = O(n^p) \), então \( T(n) = O(n^p \log n) \).
3. Se \( f(n) = O(n^c) \) com \( c > p \), então \( T(n) = O(f(n)) \).

Aqui:
- \( f(n) = O(1) \), ou seja, \( c = 0 \).
- Como \( c < p \) (0 < 1), caímos no **Caso 1**.

### **4. Solução Assintótica \( T(n) \):**

Pelo Teorema Mestre:
\[
T(n) = O(n^1) = O(n)
\]

### **Conclusão**
A complexidade assintótica do **MaxMin Select** é **O(n)**, confirmando que o algoritmo processa cada elemento do array apenas uma vez durante sua execução.

## Gráfico de fluxo





![Screenshot_52](https://github.com/user-attachments/assets/2ababbf8-f989-4475-aab0-7bd8adf5fcb9)


