

# Q1. `==` compares values; `is` checks whether two references point to the same object.
x = [1, 2]
y = [1, 2]
print(x == y)  # True: same contents
print(x is y)  # False: different list objects

# Q2. Mutable: list, set, dict. Immutable: tuple, str, int, float, bool, frozenset.
# Immutability helps prevent accidental changes and makes values safer to share or use as dictionary keys (when hashable).

# Q3. Output: False
print(0.1 + 0.2 == 0.3)
# Binary floating-point cannot represent some decimal fractions exactly, so the computed values differ slightly.

# Q4. Choose a tuple for:
# 1) Fixed coordinates such as (latitude, longitude), because the pair should not change.
# 2) Fixed records such as (name, age), when the collection is intended to stay unchanged.
# 3) Dictionary keys, when all tuple elements are immutable/hashable and the key should remain stable.

# Q5. A list may need to check elements one by one, so membership is O(n).
# A dictionary uses a hash to calculate where a key should be stored; lookup is O(1) on average.

# Q6. range() creates an integer sequence-like range object, commonly used in loops.
# numpy.arange() creates a NumPy array and can use steps such as 0.5, though floating-point steps may have rounding issues.
# range() does not support fractional steps; range(0, 5, 1) yields integers 0–4.
# np.arange(0, 2, 0.5) yields [0.  0.5 1.  1.5].

# Q7.
a = [1, 2, 3]
x = [4, 5]
b = a.copy()
b.append(x)
print(b)  # [1, 2, 3, [4, 5]]
b = a.copy()
b.extend(x)
print(b)  # [1, 2, 3, 4, 5]
b = a.copy()
b.insert(1, x)
print(b)  # [1, [4, 5], 2, 3]

# Q8.
a, *b, c = [10, 20, 30, 40, 50]
print(a, b, c)  # 10 [20, 30, 40] 50
# For [10, 20], a=10, b=[], c=20.
# For [10], unpacking raises ValueError because two required targets (a and c) need values.

# Q9. With (-7, 2):
print(-7 / 2)   # -3.5: true division
print(-7 // 2)  # -4: floor division rounds down
print(-7 % 2)   # 1: remainder consistent with floor division
print(-7 ** 2)  # -49 due to operator precedence; use (-7) ** 2 for 49
# For the operator ** applied to the pair (-7, 2), (-7) ** 2 is 49.

# Q10. NumPy is faster for large numerical workloads because:
# 1) arrays store same-type values in compact, contiguous memory;
# 2) vectorized operations run in optimized compiled code rather than Python loops;
# 3) NumPy reduces per-element Python object and interpreter overhead.
