# Recursividad múltiple

def fibonacci(n):

    if n == 0 or n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n -1)

# O(2**n)