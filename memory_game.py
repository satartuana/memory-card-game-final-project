import random
import time

cards = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D']
random.shuffle(cards)

revealed = ['*'] * 8
moves = 0

def show_board():
    print("\nBoard:")
    print("0 1 2 3 4 5 6 7")
    print(" ".join(revealed))

print("Memory Card Game Started!")

while '*' in revealed:
    show_board()

    try:
        first = int(input("First card (0-7): "))
        second = int(input("Second card (0-7): "))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        continue

    if first < 0 or first > 7 or second < 0 or second > 7:
        print("Please choose numbers between 0 and 7.")
        continue

    if first == second:
        print("Please choose two different cards.")
        continue

    if revealed[first] != '*' or revealed[second] != '*':
        print("One of these cards is already matched.")
        continue

    revealed[first] = cards[first]
    revealed[second] = cards[second]
    show_board()

    moves += 1

    if cards[first] == cards[second]:
        print("Match!")
    else:
        print("No match!")
        time.sleep(1)
        revealed[first] = '*'
        revealed[second] = '*'

print("\nCongratulations! You completed the game.")
print("Total moves:", moves)
input("Press Enter to exit...")
