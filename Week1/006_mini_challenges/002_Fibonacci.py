# Create a function to calculate the Fibonacci sequence up to n terms.

def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

n_terms = 10
result = fibonacci(n_terms)
print(f"Fibonacci sequence up to {n_terms} terms: {result}")

