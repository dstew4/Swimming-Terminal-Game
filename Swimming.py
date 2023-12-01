import random

class Swimmer:
    def __init__(self, name, speed=5, endurance=5, technique=5, stroke_specialization='freestyle', fatigue=0):
        self.name = name
        self.speed = speed
        self.endurance = endurance
        self.technique = technique
        self.stroke_specialization = stroke_specialization
        self.fatigue = fatigue

    def train(self, days_until_meet):
        print(f"You have {days_until_meet} days until the swim meet")
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
        return days_until_meet - 1  # Decrease the days until the meet

    def compete(self, current_event_stroke):
        # Randomly determine the difficulty of the competition
        win_threshold = random.randint(45, 60)

        # Random performance variability
        performance_variability = random.uniform(0.9, 1.1)

        # Calculate the score, balancing the factors
        base_score = self.speed + self.endurance + self.technique
        fatigue_impact = min(self.fatigue, base_score * 0.5)  # Limiting the impact of fatigue
        score = (base_score - fatigue_impact) * performance_variability

        # Bonus for stroke specialization
        if self.stroke_specialization.lower() == current_event_stroke.lower():
            score += 5

        print(f"Competition score needed to win: {win_threshold}")
        print(f"Your competition score: {score:.2f}")

        if score > win_threshold:
            print("You won your event! Congratulations!")
        else:
            print("Good effort, but not enough to win this time.")

def create_swimmer():
    name = input("Enter your swimmer's name: ")
    stroke_specialization = input("Enter your swimmer's stroke specialization (e.g., freestyle, butterfly): ")
    return Swimmer(name, stroke_specialization=stroke_specialization)

def main():
    swimmer = create_swimmer()
    days_until_meet = 14
    print(f"Welcome to the swimming world, {swimmer.name}!")

    valid_strokes = ['freestyle', 'butterfly', 'backstroke', 'breaststroke']

    while days_until_meet > 0:
        print(f"Days until meet: {days_until_meet}")
        choice = input("Choose an action: Train (t), Compete (c), Exit (e): ").lower()
        if choice == 't':
            days_until_meet = swimmer.train(days_until_meet)
        elif choice == 'c':
            current_event_stroke = input("Enter the stroke for this competition (e.g., freestyle, butterfly): ")
            while current_event_stroke.lower() not in valid_strokes:
                print("Invalid stroke. Please enter a valid stroke type.")
                current_event_stroke = input("Enter the stroke for this competition: ")
            swimmer.compete(current_event_stroke)
            days_until_meet = 21  # Resets the days until the meet
        elif choice == 'e':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

    # Final competition at the end of the countdown
    print("It is time for the main swim meet!")
    main_event_stroke = input("Enter the stroke for the main competition (e.g., freestyle, butterfly): ")
    while main_event_stroke.lower() not in valid_strokes:
        print("Invalid stroke. Please enter a valid stroke type.")
        main_event_stroke = input("Enter the stroke for the main competition: ")
    swimmer.compete(main_event_stroke)

if __name__ == "__main__":
    main()