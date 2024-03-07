import random

def roll_dice(num_rolls, num_sides):
    """
    Simulate rolling dice.
    
    Args:
    - num_rolls (int): Number of rolls.
    - num_sides (int): Number of sides on the dice.
    """
    print(f"Rolling {num_rolls} dice with {num_sides} sides:")
    for i in range(1, num_rolls + 1):
        result = random.randint(1, num_sides)
        print(f"Roll {i}: {result}")

def main():
    print("Welcome to the Dice Rolling Simulator!")
    num_rolls = int(input("Enter the number of rolls: "))
    num_sides = int(input("Enter the number of sides on the dice: "))
    roll_dice(num_rolls, num_sides)

if __name__ == "__main__":
    main()
