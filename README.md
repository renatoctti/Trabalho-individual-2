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


### Introdução
O algoritmo `max_min_select` segue o paradigma **"dividir para conquistar"**, dividindo o array em duas partes recursivamente e combinando os resultados para encontrar o mínimo e o máximo de um conjunto de números.

### Contagem de Operações
- Para um único elemento (`left == right`), a complexidade é **O(1)**.
- Para dois elementos (`right == left + 1`), é realizada uma única comparação **O(1)**.
- Para mais de dois elementos:
  - O array é dividido em **duas metades** de tamanho aproximadamente `n/2`.
  - São feitas **duas chamadas recursivas**, cada uma processando `n/2`.
  - Após a recursão, são feitas **duas comparações** para combinar os resultados.

A recorrência que descreve o número de operações é:

\[
T(n) = 2T(n/2) + 2
\]

### Resolvendo a Recorrência
Usamos o **método da árvore de recorrência**:

- Nível 0: \( T(n) \)
- Nível 1: \( 2T(n/2) + 2 \)
- Nível 2: \( 4T(n/4) + 4 \)
- Nível \( k \): \( 2^k T(n/2^k) + 2^k \)

O processo continua até que \( n/2^k = 1 \), ou seja, \( k = \log_2 n \). Substituindo na soma de operações:

\[
T(n) = 2^{\log_2 n} T(1) + 2(2^{\log_2 n} - 1)
\]

Sabemos que \( T(1) = O(1) \), então:

\[
T(n) = O(2^{\log_2 n}) = O(n) + O(n) = O(n)
\]



### 2. Complexidade Assintótica
A complexidade assintótica do algoritmo é **Θ(𝑛)**, pois o número de comparações cresce linearmente em relação ao tamanho da entrada.

Essa abordagem é mais eficiente do que uma comparação ingênua, que requer **2(n - 1) ≈ Θ(𝑛)** comparações, mas ainda se mantém na mesma classe de complexidade **O(n)**.

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
- **\( a = 2 \)** (número de subproblemas)
- **\( b = 2 \)** (fator de redução do tamanho do problema)
- **\( f(n) = O(1) \)** (custo externo relacionado à divisão e combinação dos subproblemas)

### **2. Cálculo de \( \log_b a \) para determinar \( p \):**

\[
 p = \log_2 2 = 1
\]

Os três casos do Teorema Mestre são:

- Se ( f(n) < n log(b) a ), então ( T(n) = O(n^p) ).
- Se ( f(n) = n log(b) a ), então ( T(n) = O(n^p \log n) ).
- Se ( f(n) > n log(b) a ), então T(n) = O(f(n) ).

Aqui:

- 𝑓(𝑛) = Θ(𝑛1 − 𝜖) com 𝜖 > 0, assim temos 𝑓(𝑛) =  Θ(𝑛0) = Θ(1)
- Como \(𝑛0 < \log_b a\) (0 < 1), caímos no **Caso 1**.

Pelo Teorema Mestre:

$$
T(n) = O(n^1) = O(n)
$$

### **Conclusão**
A complexidade assintótica do **MaxMin Select** é **O(n)**, confirmando que o algoritmo processa cada elemento do array apenas uma vez durante sua execução.

## Gráfico de fluxo


### Gráfico do fluxo de ida

![Screenshot_54](https://github.com/user-attachments/assets/2b7f9b55-c15a-4d57-b832-84c505743e31)

### Gráfico do fluxo de retorno

![Screenshot_55](https://github.com/user-attachments/assets/6bbbdeb6-5190-435f-9a7b-9a6d4db4f6fb)







