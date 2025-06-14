import random
from collections import Counter

thoughts_log = []

affirmations = [
    "This will pass. You've handled harder things.",
    "Breathe. You're doing better than you think.",
    "Progress over perfection — one step at a time.",
    "Let go of control. Trust yourself.",
    "You are safe. You are strong. You’ve got this.",
    "This too shall pass. Just breathe.",
    "Even this can become a beautiful lesson."
]

def main():
    print("Welcome to your Brain Dump!")
    print("Just write whatever comes to your mind!")
    print(" ")
    print("Once you're done dumping, type 'summary' to view insights or type 'done' to exit.\n")

    while True:
        thought = input("Thought: ")
        if thought.lower() == 'done':
            print("\nDump complete. Take a breath, you're doing well.")
            break
        elif thought.lower() == 'summary':
            show_summary(thoughts_log)
            continue

        try:
            stress_level = int(input("Stress Level (1-10): "))
            if not 1 <= stress_level <= 10:
                print("Please enter a number between 1 and 10.\n")
                continue
        except ValueError:
            print("Please enter a valid number.\n")
            continue

        thoughts_log.append((thought, stress_level))
        print("Noted.\n")


def show_summary(thoughts):
    if not thoughts:
        print("No data to summarize yet.\n")
        return

    print("\nYour Thought & Stress Summary:\n")

    high_stress = sorted([(th, s) for th, s in thoughts if s > 5], key=lambda x: x[1], reverse=True)
    low_stress = sorted([(th, s) for th, s in thoughts if s <= 5], key=lambda x: x[1], reverse=True)

    print("1. High-Stress Thoughts (>5):")
    if high_stress:
        for i, (th, _) in enumerate(high_stress, 1):
            print(f"   {i}. {th}")
    else:
        print("   None noted.")

    print("\n2. Low-Stress Thoughts (≤5):")
    if low_stress:
        for i, (th, _) in enumerate(low_stress, 1):
            print(f"   {i}. {th}")
    else:
        print("   None noted.")

    if high_stress:
        affirmation = random.choice(affirmations)
        print(f"\n Grounding Affirmation:\n   {affirmation}")

    print("\nUse 'done' to end or keep journaling.\n")


if __name__ == "__main__":
    main()
