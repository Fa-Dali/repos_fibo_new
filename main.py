def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Пример использования
n = 10
print(f"Число Фибоначчи на позиции {n}: {fibonacci_iterative(n)}")