

# Q11. 
matrix1 = [[0] * 3 for _ in range(3)]
matrix2 = [[0] * 3] * 3
matrix1[0][0] = 99
matrix2[0][0] = 99
print(matrix1)
print(matrix2)


# Q12.
x = [1, 2, 3]
y = x
x = x + [4]
print("x =", x)
print("y =", y)
a = [1, 2, 3]
b = a
a += [4]
print("a =", a)
print("b =", b)

# Q13. 
for i in range(5):
    pass
print(i)
for j in range(0):
    pass
print(j)  # NameError: j was never assigned because the loop had no iterations.

# Q14.
print("10" + "20")
print(10 + 20)
print("10" * 3)
print(10 * "3")
try:
    print("10" + 20)
except TypeError as e:
    print("TypeError:", e)
print(int("10") + 20)

# Q15.
print(0 or 5)
print(5 or 0)
print(None or "hello")
print(0 and 5)
print(5 and 10)
print([] or "default")
print([0] or "default")

