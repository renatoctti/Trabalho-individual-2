def max_min_select(arr, left, right):
    # Caso base: um único elemento
    if left == right:
        return arr[left], arr[left]
    
    # Caso base: dois elementos
    if right == left + 1:
        if arr[left] < arr[right]:
            return arr[left], arr[right]
        else:
            return arr[right], arr[left]
    
    # Divide o array ao meio
    mid = (left + right) // 2
    min1, max1 = max_min_select(arr, left, mid)
    min2, max2 = max_min_select(arr, mid + 1, right)
    
    # Combina os resultados
    return min(min1, min2), max(max1, max2)

# Função principal para testes
def main():
    test_cases = [
        [3, 1, 8, 2, 5, 9, 4, 7, 6],
        [10, 20, 30, 40, 50],
        [5, 5, 5, 5, 5],
        [100, -100, 50, -50, 0],
        [42],
        [9, 8, 7, 6, 5, 4, 3, 2, 1]
    ]
    
    for i, arr in enumerate(test_cases):
        min_val, max_val = max_min_select(arr, 0, len(arr) - 1)
        print(f"Teste {i + 1}: Array: {arr} -> Mínimo: {min_val}, Máximo: {max_val}")

if __name__ == "__main__":
    main()
