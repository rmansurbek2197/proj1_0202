# 1
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# 2
def sum_even_between(a, b):
    return sum(i for i in range(a, b + 1) if i % 2 == 0)

# 3
def avg_min_max(lst):
    return (min(lst) + max(lst)) / 2

# 4
def is_palindrome(text):
    return text == text[::-1]

# 5
def sum_digits(n):
    return sum(int(d) for d in str(abs(n)))
