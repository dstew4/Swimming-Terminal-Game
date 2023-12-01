import random

class Swimmer:
    def __init__(self, name, speed=5, endurance=5, technique=5, stroke=5, fatigue=0):
        self.name = name
        self.speed = speed
        self.endurance = endurance
        self.technique = technique
        self.stroke = stroke
        self.fatigue = fatigue

    def train(self):
        print("What type of training do you want to do?")
        print("1. Sprint\n2. Distance\n3. Drills\n4. Recovery")
        training_type = input("Choose your training type (1-4): ")

        if training_type == "1":
            self.speed += random.randint(0, 2)
            self.fatigue += random.randint(1, 3)
        elif training_type == "2":
            self.endurance += random.randint(0, 2)
            self.fatigue += random.randint(1, 3)
        elif training_type == "3":
            self.technique += random.randint(0, 2)
            self.fatigue += random.randint(1, 3)
        elif training_type == "4":
            fatigue_reduction = random.randint(1, 3)
            self.fatigue = max(0, self.fatigue - fatigue_reduction)  # Prevent negative fatigue
        else:
            print("Invalid training type. No training done.")

        print(f"Training complete. Stats: Speed: {self.speed}, Endurance: {self.endurance}, Technique: {self.technique}, Fatigue: {self.fatigue}")

    def compete(self):
        return self.speed + self.endurance + self.technique

def create_swimmer():
    name = input("Enter your swimmer's name: ")
    return Swimmer(name)

def main():
    swimmer = create_swimmer()
    print(f"Welcome to the swimming world, {swimmer.name}!")

    while True:
        choice = input("Choose an action: Train (t), Compete (c), Exit (e): ").lower()
        if choice == 't':
            swimmer.train()
        elif choice == 'c':
            score = swimmer.compete()
            print(f"You competed with a score of {score}!")
        elif choice == 'e':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()