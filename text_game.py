import random

class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{item} has been added to your inventory.")

    def show_inventory(self):
        if self.inventory:
            print("Your inventory contains:", ", ".join(self.inventory))
        else:
            print("Your inventory is empty.")

    def __str__(self):
        return f"Character: {self.name}, Health: {self.health}, Inventory: {self.inventory}"

def create_character():
    name = input("Enter your character's name: ")
    return Character(name)

def story_start(character):
    print(f"{character.name}, you wake up in a dark forest.")
    print("You see a path to your left and right.")
    decision_1(character)

def decision_1(character):
    choice = input("Do you want to go left or right? (left/right): ").strip().lower()
    if choice == "left":
        path_left(character)
    elif choice == "right":
        path_right(character)
    else:
        print("Invalid choice, please type 'left' or 'right'.")
        decision_1(character)

def path_left(character):
    print(f"{character.name}, you walk down the left path and encounter a wild animal!")
    print("You can choose to fight or run.")
    choice = input("Do you want to fight or run? (fight/run): ").strip().lower()
    if choice == "fight":
        fight_animal(character)
    elif choice == "run":
        run_away(character)
    else:
        print("Invalid choice, please type 'fight' or 'run'.")
        path_left(character)

def path_right(character):
    print(f"{character.name}, you walk down the right path and find a treasure chest.")
    print("You can choose to open it or leave it.")
    choice = input("Do you want to open the chest or leave it? (open/leave): ").strip().lower()
    if choice == "open":
        open_chest(character)
    elif choice == "leave":
        leave_chest(character)
    else:
        print("Invalid choice, please type 'open' or 'leave'.")
        path_right(character)

def fight_animal(character):
    print(f"{character.name}, you fight bravely and defeat the animal!")
    character.health -= 20
    print(f"Your health is now {character.health}.")
    print("You continue your journey and find a puzzle blocking your path.")
    puzzle_1(character)

def run_away(character):
    print(f"{character.name}, you run away safely.")
    print("You continue your journey and find a puzzle blocking your path.")
    puzzle_1(character)

def open_chest(character):
    print(f"{character.name}, you open the chest and find a magical sword!")
    character.add_to_inventory("Magical Sword")
    print("You continue your journey and find a puzzle blocking your path.")
    puzzle_1(character)

def leave_chest(character):
    print(f"{character.name}, you leave the chest and continue your journey.")
    print("You find a puzzle blocking your path.")
    puzzle_1(character)

def puzzle_1(character):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    correct_answer = num1 + num2

    print("To proceed, you must solve the puzzle:")
    print(f"What is {num1} + {num2}?")
    answer = input("Your answer: ").strip()
    
    if answer == str(correct_answer):
        print("Correct! You may proceed.")
        puzzle_2(character)
    else:
        print("Incorrect. Try again.")
        puzzle_1(character)

def puzzle_2(character):
    print("You encounter another puzzle. Solve this riddle to proceed:")
    print("I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?")
    answer = input("Your answer: ").strip().lower()
    if answer == "echo" or answer == "air" or answer == "wind":
        print("Correct! You may proceed.")
        puzzle_3(character)
    else:
        print("Incorrect. Try again.")
        puzzle_2(character)

def puzzle_3(character):
    print("You encounter a third puzzle. Solve this logic puzzle to proceed:")
    print("You see three doors. One leads to freedom, but the other two lead to certain death. You can ask one question to one of the guards to determine which door leads to freedom. What do you ask?")
    answer = input("Your answer: ").strip().lower()
    if answer == "if i were to ask the other guard which door leads to freedom, what would he say?":
        print("Correct! You have solved the puzzle and can proceed on your journey.")
        # Continue the story or end the game...
    else:
        print("Incorrect. Try again.")
        puzzle_3(character)

def main():
    print("Welcome to the Text-Based Game!")
    character = create_character()
    print(f"Character created: {character}")

    story_start(character)

    while True:
        command = input("Enter a command (type 'help' for a list of commands): ").strip().lower()
        if command == "quit":
            print("Thanks for playing!")
            break
        elif command == "help":
            print("Available commands: 'help', 'quit', 'inventory'")
        elif command == "inventory":
            character.show_inventory()
        else:
            print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
