import math

def calculate_a_iterative(k):
    a_prev, b_prev = 1, 1  
    for i in range(2, k + 1):
        a_prev = 0.5 * (math.sqrt(b_prev) + math.sqrt(a_prev))
    return a_prev

k = 10
print(f"Результат для k={k} (итеративно): {calculate_a_iterative(k)}")