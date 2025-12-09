def run_quiz():
    # Database of questions, options, and correct answers
    questions = [
        {
            "prompt": "What is the capital of France?",
            "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
            "answer": "C"
        },
        {
            "prompt": "Which data type is used to store True/False values in Python?",
            "options": ["A. int", "B. boolean", "C. string", "D. float"],
            "answer": "B"
        },
        {
            "prompt": "What is 5 + 3 * 2?",
            "options": ["A. 16", "B. 11", "C. 10", "D. 13"],
            "answer": "B"
        }
    ]

    score = 0
    print("--- Welcome to the Quiz Game ---")

    for i, q in enumerate(questions):
        print(f"\nQuestion {i + 1}: {q['prompt']}")
        for option in q['options']:
            print(option)
        
        user_answer = input("Your answer (A/B/C/D): ").upper()

        if user_answer == q['answer']:
            print("Correct! ✅")
            score += 1
        else:
            print(f"Wrong! ❌ The correct answer was {q['answer']}.")

    # Final Score Display
    print("\n--- Quiz Completed ---")
    print(f"You got {score} out of {len(questions)} questions correct.")
    percentage = (score / len(questions)) * 100
    print(f"Your Score: {percentage}%")
    
    if percentage == 100:
        print("Excellent work!")
    elif percentage >= 50:
        print("Good effort!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    run_quiz()