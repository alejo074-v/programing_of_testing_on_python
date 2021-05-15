"""# Ley de la suma

def f(n):
    for i in range(n):
        print(i)

    for i in range(n):
        print(i)

# O(n) + O(n) = O(n + n) = O(2n) = O(n) 

# Ley de la suma

def f(n):
    for i in range(n):
        print(i)

    for i in range(n * n):
        print(i)

# O(n) = O(n * n) = O(n + n2) = O(n2) """


# Ley de la suma

def f(n):
    for i in range(n):

        for j in range(n):
            print(i, j)

# O(n) = O(n * n) = O(n + n2) = O(n2) 