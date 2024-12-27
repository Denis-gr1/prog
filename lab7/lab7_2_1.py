import math

def calculate_a_recursive(k, a_prev=1, b_prev=1):
    if k == 1:
        return a_prev
    b_k_minus_1 = b_prev
    a_k_minus_1 = a_prev
    return 0.5 * (math.sqrt(b_k_minus_1) + math.sqrt(calculate_a_recursive(k - 1, a_k_minus_1, b_k_minus_1)))

k = 32
print(f"Результат для k={k} (рекурсия): {calculate_a_recursive(k)}")
