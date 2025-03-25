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
        [12, 5, 19, 3, 8, 25, 7, 15, 10],
        [60, 45, 30, 75, 90],
        [11, 11, 11, 11, 11],
        [200, -150, 75, -25, 50],
        [99],
        [14, 13, 12, 11, 10, 9, 8, 7, 6]
    ]
    
    for i, arr in enumerate(test_cases):
        min_val, max_val = max_min_select(arr, 0, len(arr) - 1)
        print(f"Teste {i + 1}: Array: {arr} -> Mínimo: {min_val}, Máximo: {max_val}")

if __name__ == "__main__":
    main()