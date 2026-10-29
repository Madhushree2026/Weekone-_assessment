

# Q16. .
a, b = 7, 12
a, b = a + b, a  
a, b = 7, 12
a = a + b
b = a - b
a = a - b
print("Arithmetic swap:", a, b)
a, b = 7, 12
a = a ^ b
b = a ^ b
a = a ^ b
print("XOR swap:", a, b)
a, b = 7, 12
a, b = b, a
print("Tuple swap (most Pythonic):", a, b)

# Q17. 
price = float(input("Q17 Item price: ₹"))
quantity = int(input("Q17 Quantity: "))
subtotal = price * quantity
gst = subtotal * 0.18
delivery = 40 if subtotal < 500 else 0
total = subtotal + gst + delivery
print(f"Subtotal:     ₹{subtotal:.2f}")
print(f"GST (18%):    ₹{gst:.2f}")
print(f"Delivery:     ₹{delivery:.2f}")
print("------------------------")
print(f"Total:        ₹{total:.2f}")

# Q18. 
value = float(input("Q18 Temperature value: "))
unit = input("Q18 Unit (C/F): ").strip().upper()
if unit == "C":
    print(f"{value:.2f}°C = {(value * 9 / 5 + 32):.2f}°F")
elif unit == "F":
    print(f"{value:.2f}°F = {((value - 32) * 5 / 9):.2f}°C")
else:
    print("Error: unit must be C or F.")

# Q19. 
n = abs(int(input("Q19 Enter a 4-digit number: ")))
digit_sum = (n // 1000) + ((n // 100) % 10) + ((n // 10) % 10) + (n % 10)
print("Sum of digits:", digit_sum)

# Q20. 
raw = input("Q20 Enter a value: ")
try:
    value = int(raw)
    kind = "int"
except ValueError:
    try:
        value = float(raw)
        kind = "float"
    except ValueError:
        value = raw
        kind = "str"
print("Value:", value)
print("Type:", kind)

# Q21. 
income = float(input("Q21 Annual income (₹): "))
remaining = max(0, income)
tax = 0
slabs = [(300000, 0.00), (400000, 0.05), (300000, 0.10),
         (200000, 0.15), (300000, 0.20)]
labels = ["First ₹3,00,000", "Next ₹4,00,000", "Next ₹3,00,000",
          "Next ₹2,00,000", "Next ₹3,00,000", "Above ₹15,00,000"]
print("Tax breakdown:")
for i, (limit, rate) in enumerate(slabs):
    taxable = min(remaining, limit)
    slab_tax = taxable * rate
    tax += slab_tax
    print(f"{labels[i]} at {rate*100:.0f}%: ₹{slab_tax:.2f}")
    remaining -= taxable
    if remaining <= 0:
        break
if remaining > 0:
    slab_tax = remaining * 0.30
    tax += slab_tax
    print(f"{labels[5]} at 30%: ₹{slab_tax:.2f}")
print(f"Total tax: ₹{tax:.2f}")

# Q22. 
pan = input("Q22 Enter PAN: ").strip()
reason = ""
if len(pan) != 10:
    reason = "length must be exactly 10"
elif not pan[:5].isalpha() or not pan[:5].isupper():
    reason = "first 5 characters must be uppercase letters"
elif not pan[5:9].isdigit():
    reason = "characters 6–9 must be digits"
elif not pan[9].isalpha() or not pan[9].isupper():
    reason = "last character must be an uppercase letter"
if reason:
    print("Invalid PAN —", reason)
else:
    print("Valid PAN")

# Q23.
units = float(input("Q23 Units consumed: "))
if units < 0:
    print("Units cannot be negative.")
else:
    remaining = units
    energy = min(remaining, 50) * 4.10
    remaining = max(0, remaining - 50)
    energy += min(remaining, 50) * 5.55
    remaining = max(0, remaining - 50)
    energy += min(remaining, 100) * 7.10
    remaining = max(0, remaining - 100)
    energy += remaining * 8.15
    fixed = 110
    tax = (energy + fixed) * 0.06
    print(f"Energy charges: ₹{energy:.2f}")
    print(f"Fixed charge:   ₹{fixed:.2f}")
    print(f"Government tax: ₹{tax:.2f}")
    print(f"Total bill:     ₹{energy + fixed + tax:.2f}")

# Q24. 
runs = int(input("Q24 Runs scored: "))
balls = int(input("Q24 Balls faced: "))
if balls == 0:
    print("Cannot calculate strike rate when balls faced is zero.")
else:
    sr = runs / balls * 100
    if sr > 150:
        category = "Explosive (T20 finisher)"
    elif sr > 100:
        category = "Aggressive (Top order T20)"
    elif sr >= 75:
        category = "Steady (ODI anchor)"
    else:
        category = "Defensive (Test match)"
    print(f"Strike rate: {sr:.2f}; Category: {category}")

# Q25. 
weight = float(input("Q25 Weight in kg: "))
height_cm = float(input("Q25 Height in cm: "))
if height_cm <= 0 or weight <= 0:
    print("Weight and height must be positive.")
else:
    bmi = weight / (height_cm / 100) ** 2
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 23:
        category = "Normal"
    elif bmi < 25:
        category = "Overweight"
    elif bmi < 30:
        category = "Obese Class I"
    else:
        category = "Obese Class II"
    print(f"BMI: {bmi:.2f}; Category: {category}")

# Q26.
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" " if j < i else "")
    print()

# Q27.
n = 5
for row in range(1, n + 1):
    print(" " * (n - row), end="")
    for j in range(1, row + 1):
        print(j, end=" ")
    for j in range(row - 1, 0, -1):
        print(j, end=" " if j > 1 else "")
    print()
for row in range(n - 1, 0, -1):
    print(" " * (n - row), end="")
    for j in range(1, row + 1):
        print(j, end=" ")
    for j in range(row - 1, 0, -1):
        print(j, end=" " if j > 1 else "")
    print()

# Q28.
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Q29. 
rows = 5
triangle = []
for i in range(rows):
    row = [1] * (i + 1)
    for j in range(1, i):
        row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    triangle.append(row)
for row in triangle:
    print(" ".join(str(v) for v in row).center(rows * 2))

# Q30. 
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print(chr(ord("A") + j), end=" " if j < i - 1 else "")
    print()

# Q31. 
armstrong = []
for number in range(1, 10000):
    digits = []
    temp = number
    while temp > 0:
        digits.append(temp % 10)
        temp //= 10
    power = len(digits)
    total = 0
    for digit in digits:
        total += digit ** power
    if total == number:
        armstrong.append(number)
print("Armstrong numbers:", ", ".join(str(x) for x in armstrong))
print("Count:", len(armstrong))

# Q32. 
n = int(input("Q32 Number of Fibonacci terms: "))
a, b, total = 0, 1, 0
terms = []
for _ in range(max(0, n)):
    terms.append(a)
    total += a
    a, b = b, a + b
print("Terms:", terms)
print("Sum:", total)

# Q33. 
n = int(input("Q33 Enter N: "))
def is_prime(value):
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 1
    return True
print(n, "is prime:", is_prime(n))
prime_sum = 0
for value in range(2, n + 1):
    if is_prime(value):
        prime_sum += value
print("Sum of primes from 2 to N:", prime_sum)

# Q34. 
original = int(input("Q34 Enter an integer: "))
if original < 0:
    print("Reversed:", "-" + str(-original))  # display only; reversal logic uses arithmetic
    print("Not palindrome")
else:
    temp = original
    reversed_num = 0
    while temp > 0:
        reversed_num = reversed_num * 10 + temp % 10
        temp //= 10
    print("Reversed:", reversed_num)
    print("Palindrome" if original == reversed_num else "Not palindrome")

# Q35. 
a = int(input("Q35 First positive integer: "))
b = int(input("Q35 Second positive integer: "))
if a <= 0 or b <= 0:
    print("Enter positive integers only.")
else:
    x, y = a, b
    while y != 0:
        x, y = y, x % y
    hcf = x
    lcm = (a * b) // hcf
    print("HCF:", hcf)
    print("LCM:", lcm)

# Q36. 
sentence = input("Q36 Enter a sentence: ")
vowels = consonants = digits = spaces = special = 0
for ch in sentence:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        special += 1
print("Total characters:", len(sentence))
print("Total words:", len(sentence.split()))
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)

# Q37. 
marks = list(map(float, input("Q37 Enter 10 marks separated by spaces: ").split()))
if len(marks) != 10:
    print("Please enter exactly 10 marks.")
else:
    maximum = minimum = marks[0]
    total = 0
    for mark in marks:
        if mark > maximum:
            maximum = mark
        if mark < minimum:
            minimum = mark
        total += mark
    average = total / len(marks)
    above = 0
    for mark in marks:
        if mark > average:
            above += 1
    highest = None
    second_highest = None
    for mark in marks:
        if highest is None or mark > highest:
            if mark != highest:
                second_highest = highest
            highest = mark
        elif mark != highest and (second_highest is None or mark > second_highest):
            second_highest = mark
    if second_highest is None:
        second_highest = "Not available"
    print("Maximum:", maximum)
    print("Minimum:", minimum)
    print("Average:", average)
    print("Above average:", above)
    print("Second-highest distinct mark:", second_highest)

# Q38. 
review = input("Q38 Enter review: ").lower()
words = review.split()
frequency = {}
for word in words:
    cleaned = ""
    for ch in word:
        if ch.isalnum():
            cleaned += ch
    if cleaned:
        frequency[cleaned] = frequency.get(cleaned, 0) + 1
items = list(frequency.items())
for i in range(len(items)):
    for j in range(i + 1, len(items)):
        if items[j][1] > items[i][1]:
            items[i], items[j] = items[j], items[i]
print("Frequencies:", items)
if items:
    print("Most frequent:", items[0][0], "Count:", items[0][1])

# Q39.
states = {"Karnataka": "Bengaluru", "Maharashtra": "Mumbai",
          "Tamil Nadu": "Chennai", "Kerala": "Thiruvananthapuram",
          "Telangana": "Hyderabad"}
while True:
    print("\\n1 Add  2 Update  3 Delete  4 Search  5 Display sorted  6 Exit")
    choice = input("Choose: ").strip()
    if choice == "1":
        state = input("State: ").strip()
        capital = input("Capital: ").strip()
        states[state] = capital
    elif choice == "2":
        state = input("State to update: ").strip()
        if state in states:
            states[state] = input("New capital: ").strip()
        else:
            print("Not found")
    elif choice == "3":
        state = input("State to delete: ").strip()
        if state in states:
            del states[state]
        else:
            print("Not found")
    elif choice == "4":
        state = input("State to search: ").strip()
        print(states.get(state, "Not found"))
    elif choice == "5":
        for state in sorted(states):
            print(state, ":", states[state])
    elif choice == "6":
        break
    else:
        print("Invalid option")

# Q40. 
section_a = {"Python", "Java", "C++", "SQL"}
section_b = {"Java", "JavaScript", "Python", "Go", "SQL"}
print("Both:", section_a & section_b)
print("Only A:", section_a - section_b)
print("Only B:", section_b - section_a)
print("All unique:", section_a | section_b)
print("Exclusive to one:", section_a ^ section_b)

# Q41. 
prices = (3845, 3902, 3878, 3955, 4012, 3998, 4055)
days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
maximum = max(prices)
minimum = min(prices)
print("Maximum:", maximum, days[prices.index(maximum)])
print("Minimum:", minimum, days[prices.index(minimum)])
print("Average:", sum(prices) / len(prices))
largest_gain = None
gain_days = None
volatility = 0
for i in range(1, len(prices)):
    change = prices[i] - prices[i - 1]
    volatility += abs(change)
    if largest_gain is None or change > largest_gain:
        largest_gain = change
        gain_days = (days[i - 1], days[i])
print("Biggest single-day gain:", largest_gain, "between", gain_days[0], "and", gain_days[1])
print("Total volatility:", volatility)

# Q42. 
numbers = [3, 5, 2, 3, 8, 5, 9, 2, 1, 7, 8, 4, 6, 6, 10, 3, 11, 12, 1, 13]
unique = set(numbers)
repeated = []
once = []
for value in numbers:
    count = 0
    for other in numbers:
        if value == other:
            count += 1
    if count > 1 and value not in repeated:
        repeated.append(value)
    elif count == 1:
        once.append(value)
print("Unique set:", unique)
print("Numbers appearing more than once:", repeated)
print("Numbers appearing exactly once:", once)

# Q43. 
sentence = input("Q43 Enter sentence: ")
cleaned = ""
for ch in sentence.lower():
    if ch.isalnum():
        cleaned += ch
print("Palindrome" if cleaned == cleaned[::-1] else "Not palindrome")

# Q44. 
sentence = input("Q44 Enter sentence: ")
result = ""
new_word = True
for ch in sentence:
    if ch.isspace():
        result += ch
        new_word = True
    elif new_word:
        result += ch.upper()
        new_word = False
    else:
        result += ch.lower()
print(result)

# Q45. 
message = input("Q45 Message: ")
shift = int(input("Q45 Shift: ")) % 26
encrypted = ""
for ch in message:
    if "A" <= ch <= "Z":
        encrypted += chr((ord(ch) - ord("A") + shift) % 26 + ord("A"))
    elif "a" <= ch <= "z":
        encrypted += chr((ord(ch) - ord("a") + shift) % 26 + ord("a"))
    else:
        encrypted += ch
print("Encrypted:", encrypted)

# Q46.
def calculate_gst(amount, gst_rate=18, gst_inclusive=False):
    rate = gst_rate / 100
    if gst_inclusive:
        total_amount = amount
        base_amount = amount / (1 + rate)
        gst_amount = total_amount - base_amount
    else:
        base_amount = amount
        gst_amount = amount * rate
        total_amount = base_amount + gst_amount
    return (round(base_amount, 2), round(gst_amount, 2), round(total_amount, 2))
print(calculate_gst(1000))
print(calculate_gst(1180, gst_inclusive=True))
print(calculate_gst(500, gst_rate=5))

# Q47.
def power(base, exp):
    if exp == 0:
        return 1
    if exp < 0:
        return 1 / power(base, -exp)
    return base * power(base, exp - 1)
print(power(2, 10))
print(power(5, 0))
print(power(3, -2))

# Q48. 
import numpy as np
identity = np.eye(5)
print("Identity matrix:\\n", identity)
scaled = identity * 10
print("Multiplied by 10:\\n", scaled)
transposed = scaled.T
print("Transpose:\\n", transposed)
# An identity matrix is symmetric, so its transpose equals itself; scaling it preserves this property.
print("Diagonal sum:", np.trace(scaled))
print("Sum of all elements:", np.sum(scaled))

# Q49. 
sales = np.array([12000, 18500, 14200, 22100, 19800, 35200, 28400])
days = np.array(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
average = np.mean(sales)
print("Total weekly sales:", np.sum(sales))
print("Daily average:", average)
print("Maximum sales day:", days[np.argmax(sales)])
print("Days above average:", np.sum(sales > average))
print("Monday to Sunday growth (%):", (sales[-1] - sales[0]) / sales[0] * 100)
print("Day-on-day % changes:", (sales[1:] - sales[:-1]) / sales[:-1] * 100)

# Q50. 
border = np.ones((5, 5), dtype=int)
border[1:-1, 1:-1] = np.zeros((3, 3), dtype=int)
print(border)
