import random

class Swimmer:
    def __init__(self, name, speed=5, endurance=5, specialty='freestyle', fiber_type='combo'):
        self.name = name
        self.speed = speed
        self.endurance = endurance
        self.specialty = specialty
        self.fiber_type = fiber_type  # Added to use muscle fiber type effectively

    def train(self):
        print(f"\nCurrent Stats - Speed: {self.speed}, Endurance: {self.endurance}")
        print("Choose your training focus:")
        print("1. Sprint\n2. Distance\n3. Rest")
        training_type = input("Enter your choice: ")

        training_effectiveness = self.calculate_training_effectiveness(training_type)
        
        if training_type == "1":  # Sprint training
            self.speed = min(self.speed + random.randint(1, 3) * training_effectiveness, 10)
            print(f"Focused on sprint training. Speed increased to {self.speed}.")
        elif training_type == "2":  # Distance training
            self.endurance = min(self.endurance + random.randint(1, 3) * training_effectiveness, 10)
            print(f"Focused on distance training. Endurance increased to {self.endurance}.")
        elif training_type == "3":  # Rest
            print("Took a day of rest. Feeling refreshed!")
        else:
            print("Invalid training type. No training done.")

    def calculate_training_effectiveness(self, training_type):
        effectiveness = 1
        if self.fiber_type == "fast" and training_type == "1":
            effectiveness = 1.5  # Increased effectiveness for fast-twitch fiber in sprint training
        elif self.fiber_type == "slow" and training_type == "2":
            effectiveness = 1.5  # Increased effectiveness for slow-twitch fiber in distance training
        # Add more conditions based on specialty and fiber type as needed
        return effectiveness

    def calculate_performance(self, event_stroke, event_distance):
            # Sample performance calculation using the fiber type
            if self.fiber_type == 'fast':
                return self.speed
            elif self.fiber_type == 'slow':
                return self.endurance 
            else:  # 'combo'
                return (self.speed + self.endurance) / 2
        
    def compete(self, event_stroke, event_distance):
        difficulty = self.calculate_difficulty(event_stroke, event_distance)
        performance = self.calculate_performance(event_stroke, event_distance)
        
        print(f"\nEvent: {event_distance}m {event_stroke.capitalize()}")
        print(f"Difficulty to beat: {difficulty}")
        print(f"Your performance score: {performance}")

        if performance > difficulty:
            print("You won your event! Congratulations!")
        else:
            print("Good effort, but not enough to win this time.")

    def calculate_difficulty(self, event_stroke, event_distance):
        # Adjusted base difficulty and scaling factors
        base_difficulty = 40
        speed_factor, endurance_factor = 3, 3

        # Sprint events favor speed
        if event_distance <= 100:
            difficulty = base_difficulty - speed_factor * min(self.speed, 10)
        # Middle distance events balance speed and endurance
        elif event_distance <= 800:
            difficulty = base_difficulty - (speed_factor * min(self.speed, 10) + endurance_factor * min(self.endurance, 10)) / 2
        # Distance events favor endurance
        else:
            difficulty = base_difficulty - endurance_factor * min(self.endurance, 10)

        if event_stroke == self.specialty:
            difficulty -= 5  # Reduce difficulty by 5 for specialty events

        return difficulty

    def display_stats(self):
        print(f"\nSwimmer Stats for {self.name}:")
        print(f"  Speed: {self.speed}")
        print(f"  Endurance: {self.endurance}")
        print(f"  Specialty: {self.specialty}")

def create_swimmer():
    print("Enter your swimmer's name: ")
    name = input()

    specialties = {
        "1": "Freestyle",
        "2": "Butterfly",
        "3": "Backstroke",
        "4": "Breaststroke",
        "5": "Individual Medley"
    }
    print("Choose your swimmer's stroke specialty:")
    for key, value in specialties.items():
        print(f"{key}. {value.capitalize()}")

    specialty_choice = input("Enter the number of your specialty: ")
    while specialty_choice not in specialties:
        print("Invalid choice. Please enter a valid number for the specialty.")
        specialty_choice = input("Enter the number of your specialty: ")
    specialty = specialties[specialty_choice]

    print("Choose your swimmer's muscle fiber type:")
    print("1. Fast Twitch (Sprint)")
    print("2. Combo (Middle Distance)")
    print("3. Slow Twitch (Distance)")
    fiber_types = { "1": "fast", "2": "combo", "3": "slow" }
    fiber_type_choice = input("Enter the number of your muscle fiber type: ")
    fiber_type = fiber_types.get(fiber_type_choice, "combo")

    return Swimmer(name, specialty=specialty, fiber_type=fiber_type)

def display_menu():
    print("\nPoolside Prodigy Menu")
    print("1. Train")
    print("2. Compete")
    print("3. View Stats")
    print("4. Exit")
    print("Enter your choice: ", end='')

def get_competition_choice(valid_strokes, valid_distances):
    print("Available strokes for competition:")
    for index, stroke in enumerate(valid_strokes, 1):
        print(f"{index}. {stroke}")

    stroke_choice = input("Choose the number for the stroke of this competition: ")
    while stroke_choice not in map(str, range(1, len(valid_strokes) + 1)):
        print("Invalid choice. Please enter a valid number for the stroke.")
        stroke_choice = input("Choose the number for the stroke of this competition: ")

    current_event_stroke = valid_strokes[int(stroke_choice) - 1].lower()

    print(f"Available distances for {current_event_stroke.capitalize()}:")
    for distance in valid_distances[current_event_stroke.capitalize()]:
        print(f" - {distance} meters")
    current_event_distance = input("Choose the distance for this competition: ")
    while not current_event_distance.isdigit() or int(current_event_distance) not in valid_distances[current_event_stroke.capitalize()]:
        print("Invalid distance. Please enter a valid distance.")
        current_event_distance = input("Choose the distance for this competition: ")

    return current_event_stroke, int(current_event_distance)


def main():
    swimmer = create_swimmer()
    days_until_meet = 14
    valid_strokes = ['Freestyle', 'Butterfly', 'Backstroke', 'Breaststroke', 'Individual Medley']
    valid_distances = {
        'Freestyle': [50, 100, 200, 400, 800, 1500],
        'Butterfly': [100, 200],
        'Backstroke': [100, 200],
        'Breaststroke': [100, 200],
        'Individual medley': [200, 400]
    }

    while days_until_meet > 0:
        display_menu()
        choice = input().lower()

        if choice == '1':
            swimmer.train()
            days_until_meet -= 1
        elif choice == '2':
            event_stroke, event_distance = get_competition_choice(valid_strokes, valid_distances)
            swimmer.compete(event_stroke, event_distance)
            days_until_meet -= 1
        elif choice == '3':
            swimmer.display_stats()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

    print("\nIt's time for the main meet!")
    main_event_stroke, main_event_distance = get_competition_choice(valid_strokes, valid_distances)
    swimmer.compete(main_event_stroke, main_event_distance)

if __name__ == "__main__":
    main()
