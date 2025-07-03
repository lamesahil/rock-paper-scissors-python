#ROCK PAPER SCISSOR
import random
choices = {1: "ROCK", 2: "PAPER", 3: "SCISSOR"}

user_score = 0
comp_score = 0
rounds = 0

while True:
    print("\n🎮 ROCK PAPER SCISSORS 🎮")
    print("1 for ROCK")
    print("2 for PAPER")
    print("3 for SCISSOR")

    try:
        user = int(input("Enter your choice (1/2/3): "))
        if user not in [1, 2, 3]:
            print("❌ Invalid input! Choose 1, 2, or 3 only.")
            continue
    except:
        print("❌ Please enter a number only.")
        continue

    comp = random.randint(1, 3)

    print(f"\n🧑 You chose: {choices[user]}")
    print(f"💻 Computer chose: {choices[comp]}")

    if user == comp:
        print("⚖️ It's a DRAW!")
    elif (user == 1 and comp == 3) or (user == 2 and comp == 1) or (user == 3 and comp == 2):
        print("🎉 You WON this round!")
        user_score += 1
    else:
        print("💀 You LOST this round!")
        comp_score += 1

    rounds += 1
    print(f"\n📊 Score after {rounds} round(s): You {user_score} - {comp_score} Computer")

    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again != 'y':
        print("\n🏁 Final Scoreboard:")
        print(f"✅ You: {user_score} | 💻 Computer: {comp_score}")
        if user_score > comp_score:
            print("🏆 YOU WON THE GAME!")
        elif user_score < comp_score:
            print("💻 COMPUTER WON THE GAME!")
        else:
            print("🤝 GAME TIED!")
        break