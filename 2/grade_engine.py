
"""
Grade Decision Engine — Day 2 (Control Flow)
- Interactive mode: asks for inputs and prints result
- Demo mode: `python grade_engine.py --demo` runs sample test cases
"""

import sys

def downgrade(grade: str) -> str:
    """Downgrade one step: A→B→C→D→F; F stays F."""
    order = ["A", "B", "C", "D", "F"]
    if grade == "F":
        return "F"
    return order[order.index(grade) + 1]

def compute_grade(score: int, attendance: int, retest: str, cheated: str):
    """
    Pure function for easy testing.
    Inputs:
      - score: 0..100
      - attendance: 0..100
      - retest: 'Y' or 'N'
      - cheated: 'Y' or 'N'
    Returns:
      (messages, final_grade_or_status)
      messages: list of strings that must be printed in order (e.g., ["Grace pass granted"])
      final_grade_or_status: one of {"A","B","C","D","F","Invalid input","Disqualified"}
    """
    msgs = []

    # 1) Validate
    if not (0 <= score <= 100) or not (0 <= attendance <= 100):
        return (msgs, "Invalid input")
    if retest not in {"Y", "N"} or cheated not in {"Y", "N"}:
        return (msgs, "Invalid input")

    # 2) Cheating overrides everything
    if cheated == "Y":
        return (msgs, "Disqualified")

    # 3) Base grade by score
    if score >= 90:
        grade = "A"
    elif score >= 75:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 40:
        grade = "D"
    else:
        grade = "F"

    # 4) Attendance penalty
    if attendance < 75:
        grade = downgrade(grade)

    # 5) Grace pass rule
    if grade == "F" and 38 <= score <= 39 and attendance >= 90 and retest == "Y":
        msgs.append("Grace pass granted")
        grade = "D"

    return (msgs, grade)

def _print_interactive_result(messages, result):
    """Print in the exact required format."""
    if result in {"Invalid input", "Disqualified"}:
        print(result)
        return
    for m in messages:
        print(m)
    print(f"Grade: {result}")

def main(argv=None):
    argv = argv or sys.argv[1:]

    # Demo mode
    if argv and argv[0] == "--demo":
        cases = [
            (92, 80, "N", "N"),
            (92, 60, "N", "N"),
            (39, 95, "Y", "N"),
            (39, 80, "Y", "N"),
            (70, 50, "N", "Y"),
            (120, 80, "N", "N"),
            (75, 74, "N", "N"),
            (60, 75, "N", "N"),
            (40, 74, "N", "N"),
        ]
        for i, (s, a, r, c) in enumerate(cases, 1):
            msgs, res = compute_grade(s, a, r, c)
            print(f"\nCase {i}: score={s}, attendance={a}, retest={r}, cheated={c}")
            _print_interactive_result(msgs, res)
        return

    # Interactive mode
    try:
        score = int(input("Enter the score (0 - 100): ").strip())
        attendance = int(input("Enter the percentage (0 - 100): ").strip())
        retest = input("Need for retest (Y/N): ").strip().upper()
        cheated = input("Cheated? (Y/N): ").strip().upper()
    except ValueError:
        print("Invalid input")
        return

    msgs, res = compute_grade(score, attendance, retest, cheated)
    _print_interactive_result(msgs, res)

if __name__ == "__main__":
    main()
