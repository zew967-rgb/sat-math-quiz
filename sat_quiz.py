"""
Digital SAT Math - Section 2, Module 1 Quiz Runner
Chạy bài kiểm tra SAT Math trực tiếp trên Terminal với chấm điểm và giải chi tiết.
"""

import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "sat_math_test.json"

def run_quiz():
    if not DATA_FILE.exists():
        print(f"Error: {DATA_FILE} not found!")
        return

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        questions = json.load(f)

    score = 0
    total = len(questions)

    print("=" * 60)
    print("      DIGITAL SAT MATH - SECTION 2, MODULE 1")
    print(f"      Total questions: {total}")
    print("=" * 60)

    for q in questions:
        print(f"\n[Câu {q['id']}] ({q['type'].upper()})")
        print(q["question"])

        if q["options"]:
            for opt_key, opt_val in q["options"].items():
                print(f"  {opt_key}) {opt_val}")

        user_ans = input("\n👉 Nhập đáp án của bạn: ").strip()

        is_correct = False
        if q["type"] == "multiple_choice":
            if user_ans.upper() == q["correct_answer"].upper():
                is_correct = True
        else:
            # So khớp số
            try:
                if float(user_ans) == float(q["correct_answer"]):
                    is_correct = True
            except ValueError:
                if user_ans.strip() == q["correct_answer"].strip():
                    is_correct = True

        if is_correct:
            print("✅ ĐÚNG!")
            score += 1
        else:
            print(f"❌ SAI! Đáp án đúng: {q['correct_answer']}")

        print(f"💡 Lời giải: {q['explanation']}")
        print("-" * 50)

    print("\n" + "=" * 60)
    print(f"KẾT QUẢ CUỐI CÙNG: {score}/{total} ({round(score/total*100, 1)}%)")
    print("=" * 60)

if __name__ == "__main__":
    run_quiz()
