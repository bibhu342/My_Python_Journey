# 🐍 Python Day 3 — Loops (Master Notes)

**Core Objective:**  
Master Python’s looping constructs (`for`, `while`), control statements (`break`, `continue`, `pass`), and pattern-building logic.  
These are fundamental for solving DSA problems, automating repetitive work, and controlling program flow effectively.

---

## Step 1 — For Loop & While Loop

📜 **Problem Statement**  
Execute a block of code multiple times — either for a fixed number of iterations (`for`) or until a condition is no longer true (`while`).

🧮 **Example**
```python
# for loop
for i in range(1, 6):
    print(i)

# while loop
num = 1
while num <= 5:
    print(num)
    num += 1
```

🧠 **Why This Matters**  
- Loops are core to most algorithms and automations.  
- Used heavily in data processing, scraping, and DSA.  
- Helps you iterate through sequences or data structures.

🧰 **Breakdown**  
- `for` loop → known number of iterations  
- `while` loop → condition-driven  
- `range(start, stop)` generates a sequence  
- Always ensure your `while` loop has an exit condition to avoid infinite loops.

🌍 **Real-World Use Cases**  
- Processing rows in a dataset  
- Reading paginated API responses  
- Automation scripts that run until a certain condition is met

---

## Step 2 — Control Statements (`break`, `continue`, `pass`)

📜 **Problem Statement**  
Control the loop execution flow — skip iterations, exit early, or hold a place.

🧮 **Example**
```python
for i in range(1, 6):
    if i == 3:
        continue
    if i == 5:
        break
    print(i)
```

🧠 **Why This Matters**  
- Gives you precise control in loops.  
- Useful in data cleaning, error handling, and search problems.

🧰 **Breakdown**  
- `break` → exits the loop immediately  
- `continue` → skips the current iteration  
- `pass` → does nothing, used as a placeholder

🌍 **Real-World Use Cases**  
- Skipping bad records in datasets (`continue`)  
- Early stopping when threshold reached (`break`)  
- Placeholder for unimplemented features (`pass`)

---

## Step 3 — Pattern Building

📜 **Problem Statement**  
Use loops to print structured shapes or repetitive outputs — key for understanding nested loops and indexing.

🧮 **Example**
```python
# Right triangle
for i in range(1, 6):
    print('*' * i)

# Inverted triangle
for i in range(5, 0, -1):
    print('*' * i)

# Pyramid
rows = 5
for i in range(rows):
    spaces = rows - i - 1
    stars = 2 * i + 1
    print(' ' * spaces + '*' * stars)
```

🧠 **Why This Matters**  
- Trains logical thinking with indices, space-star math, and loops.  
- Foundation for complex DSA problems.

🧰 **Breakdown**  
- Spaces control alignment  
- Stars control content  
- Pyramid = decreasing spaces + increasing stars

🌍 **Real-World Use Cases**  
- Formatting CLI output  
- Generating structured text  
- Strengthening DSA fundamentals for interviews

---

## Step 4 — Mini Challenge 1: Factorial

📜 **Problem Statement**  
Compute factorial of `n` using loops.  
`n! = n × (n-1) × ... × 1`

🧮 **Example**
```python
n = 5
result = 1
for i in range(1, n + 1):
    result *= i
print(result)  # 120
```

🧠 **Why This Matters**  
- Common interview question.  
- Good practice for loop iteration and accumulator pattern.

🧰 **Breakdown**  
- Start with `1` (multiplication identity).  
- Multiply through each iteration.  
- Edge case: `0! = 1`.

🌍 **Real-World Use Cases**  
- Combinatorics, probability, permutations  
- Recursive vs iterative thinking comparison  
- Coding tests & interviews

---

## Step 5 — Mini Challenge 2: Reverse Integer

📜 **Problem Statement**  
Reverse digits of an integer (handle negative numbers and zeros).

🧮 **Example**
```python
num = -1200
sign = -1 if num < 0 else 1
num = abs(num)
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
rev *= sign
print(rev)  # -21
```

🧠 **Why This Matters**  
- Tests understanding of loops, arithmetic, and edge cases.

🧰 **Breakdown**  
- Extract last digit with `% 10`  
- Build reversed number  
- Use `// 10` to remove digits  
- Handle negative sign separately

🌍 **Real-World Use Cases**  
- Data sanitization / formatting  
- Algorithm warm-up for number problems  
- Used in many LeetCode/Easy-Medium questions

---

## Step 6 — Real Data Control Demo

📜 **Problem Statement**  
Demonstrate `break` and `continue` on a **sales dataset**.

🧮 **Example**
```python
data = [1200, 5000, 2600, 3100, 5000, 7800, 10000, 4200]
for value in data:
    if value == 5000:
        continue  # skip this record
    if value == 10000:
        print(f"Found target: {value}")
        break
    print(f"Processed: {value}")
```

🧠 **Why This Matters**  
This is how you apply loops to **real-world data**, not just toy problems.

🧰 **Breakdown**  
- Skip unwanted values with `continue`  
- Stop when a condition is met with `break`  
- Prevent unnecessary computation

🌍 **Real-World Use Cases**  
- Skipping nulls or flagged records in datasets  
- Breaking search when found  
- Optimizing loop performance

---

## ✅ End-of-Day Outcomes

- ✅ Confident with `for` and `while` loops  
- ✅ Can use `break`, `continue`, `pass` correctly  
- ✅ Understand pattern logic (space vs stars)  
- ✅ Solved 2 classic loop problems (Factorial & Reverse Integer)  
- ✅ Practiced loop control with real data

---
