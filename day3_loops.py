"""
Day 3 — Loops
Mini Project: Loop Utilities + Patterns

Usage:
  python day3_loops.py            # interactive mode
  python day3_loops.py --demo     # run demo cases (no input needed)

Includes:
- Factorial (iterative) with edge handling
- Reverse Integer (handles negatives, trailing zeros)
- Pattern printing: right triangle, inverted triangle, pyramid
- Control statements demo (break / continue) on a toy dataset
"""

import sys

# ---------- Core Utilities ----------

def factorial(n: int) -> int:
    """Return n! using an iterative loop.
    Raises:
        ValueError: if n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def reverse_integer(num: int) -> int:
    """Return the integer formed by reversing the digits of num.
    Preserves the sign; strips leading zeros in the reversed output.
    Examples: 123 -> 321, -1200 -> -21
    """
    sign = -1 if num < 0 else 1
    num = abs(num)
    rev = 0
    while num > 0:
        rev = rev * 10 + (num % 10)
        num //= 10
    return sign * rev


# ---------- Pattern Printing ----------

def pattern_right_triangle(rows: int) -> None:
    """Print a right triangle of asterisks with given rows."""
    for i in range(1, rows + 1):
        print("*" * i)


def pattern_inverted_triangle(rows: int) -> None:
    """Print an inverted right triangle of asterisks with given rows."""
    for i in range(rows, 0, -1):
        print("*" * i)


def pattern_pyramid(rows: int) -> None:
    """Print a centered pyramid of asterisks with given rows."""
    for i in range(rows):
        spaces = rows - i - 1
        stars = 2 * i + 1
        print(" " * spaces + "*" * stars)


# ---------- Control Statements Demo ----------

def control_demo_break_continue(values: list[int]) -> None:
    """Demonstrate break/continue on a toy dataset.
    - Skip (continue) values equal to 5000
    - Stop (break) if value equals 10000
    Prints processed values until rule triggers.
    """
    print("Processing values with rules: skip 5000, stop at 10000")
    for v in values:
        if v == 5000:
            # Skip this record
            continue
        if v == 10000:
            # Found target; stop processing further
            print(f"Hit stop value: {v} (breaking loop)")
            break
        print(f"Processed: {v}")


# ---------- I/O Helpers ----------

def read_int(prompt: str) -> int:
    """Read an integer from input with basic validation."""
    raw = input(prompt).strip()
    try:
        return int(raw)
    except ValueError:
        raise ValueError("Invalid integer")


def read_positive_int(prompt: str) -> int:
    """Read a positive integer (>= 0 for factorial, >=1 for rows)."""
    n = read_int(prompt)
    return n


# ---------- Interactive Mode ----------

def interactive() -> None:
    """Interactive loop utilities console."""
    print("=== Day 3: Loops — Utilities & Patterns ===")
    print("Options:")
    print("  1) Factorial")
    print("  2) Reverse Integer")
    print("  3) Pattern: Right Triangle")
    print("  4) Pattern: Inverted Triangle")
    print("  5) Pattern: Pyramid")
    print("  6) Control Statements Demo (break/continue)")
    print("  q) Quit\n")

    while True:
        choice = input("Choose an option (1-6 or q): ").strip().lower()
        if choice == "q":
            print("Bye.")
            return

        try:
            if choice == "1":
                n = read_positive_int("Enter n (>= 0): ")
                print(f"{n}! = {factorial(n)}\n")

            elif choice == "2":
                n = read_int("Enter an integer: ")
                print(f"Reversed: {reverse_integer(n)}\n")

            elif choice == "3":
                rows = read_positive_int("Rows (>=1): ")
                if rows < 1:
                    print("Rows must be >= 1\n")
                    continue
                pattern_right_triangle(rows)
                print()

            elif choice == "4":
                rows = read_positive_int("Rows (>=1): ")
                if rows < 1:
                    print("Rows must be >= 1\n")
                    continue
                pattern_inverted_triangle(rows)
                print()

            elif choice == "5":
                rows = read_positive_int("Rows (>=1): ")
                if rows < 1:
                    print("Rows must be >= 1\n")
                    continue
                pattern_pyramid(rows)
                print()

            elif choice == "6":
                # Example dataset: sales amounts
                data = [1200, 5000, 2600, 3100, 5000, 7800, 10000, 4200]
                control_demo_break_continue(data)
                print()

            else:
                print("Invalid choice. Try again.\n")

        except Exception as e:
            print(f"Error: {e}\n")


# ---------- Demo Mode ----------

def demo() -> None:
    """Run demo cases for quick verification (no user input)."""
    print("== Demo: Factorial ==")
    for n in (0, 1, 5):
        try:
            print(f"{n}! = {factorial(n)}")
        except Exception as e:
            print(f"Error: {e}")

    print("\n== Demo: Reverse Integer ==")
    for num in (1234, -1200, 5, 1000):
        print(f"reverse({num}) = {reverse_integer(num)}")

    print("\n== Demo: Patterns (rows=5) ==")
    print("- Right Triangle -")
    pattern_right_triangle(5)
    print("\n- Inverted Triangle -")
    pattern_inverted_triangle(5)
    print("\n- Pyramid -")
    pattern_pyramid(5)

    print("\n== Demo: Control Statements ==")
    control_demo_break_continue([1200, 5000, 2600, 10000, 4200])


# ---------- Entrypoint ----------

def main() -> None:
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        demo()
    else:
        interactive()


if __name__ == "__main__":
    main()
