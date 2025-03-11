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

