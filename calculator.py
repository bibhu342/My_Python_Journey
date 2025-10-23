
"""
Day 1 — Getting Started & Syntax
Mini Project: Console Calculator

Usage:
  python day1_calculator.py           # interactive mode
  python day1_calculator.py --demo    # run demo cases (no input needed)
"""

import sys

def compute(a: float, b: float, op: str):
    """Return result of a <op> b. Supports + - * / % ** ."""
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        return a / b
    elif op == "%":
        if b == 0:
            raise ZeroDivisionError("Modulo by zero")
        return a % b
    elif op == "**":
        return a ** b
    else:
        raise ValueError(f"Unsupported operator: {op}")

def read_number(prompt: str) -> float:
    """Read a float from input with basic validation."""
    raw = input(prompt).strip()
    try:
        return float(raw)
    except ValueError:
        raise ValueError("Invalid number")

def interactive():
    """Interactive calculator loop."""
    print("=== Day 1: Console Calculator ===")
    print("Operators: +  -  *  /  %  **   (type 'q' to quit)\n")

    while True:
        op = input("Operator (+ - * / % ** or q): ").strip()
        if op.lower() == "q":
            print("Bye.")
            return

        try:
            a = read_number("First number: ")
            b = read_number("Second number: ")
            result = compute(a, b, op)
            print(f"Result: {result}\n")
        except ZeroDivisionError as zde:
            print(f"Error: {zde}\n")
        except ValueError as ve:
            print(f"Error: {ve}\n")

def demo():
    """Run a few demo calculations without user input."""
    cases = [
        (10, 5, "+"),
        (10, 5, "-"),
        (10, 5, "*"),
        (10, 5, "/"),
        (10, 0, "/"),   # expect division-by-zero error
        (10, 3, "%"),
        (2, 8, "**"),
        (7, 2, "x"),    # unsupported op
    ]
    for i, (a, b, op) in enumerate(cases, 1):
        print(f"Case {i}: {a} {op} {b} =", end=" ")
        try:
            print(compute(a, b, op))
        except Exception as e:
            print(f"Error: {e}")

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        demo()
    else:
        interactive()

if __name__ == "__main__":
    main()
