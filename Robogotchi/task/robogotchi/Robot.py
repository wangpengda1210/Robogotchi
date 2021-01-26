from random import Random


class Robot:

    def __init__(self, name):
        self.name = name
        self.battery = 100
        self.overheat = 0
        self.skills = 0
        self.boredom = 0
        self.rust = 0

    def oil(self):
        prev_rust = self.rust

        self.rust = max(0, self.rust - 20)

        return prev_rust, self.rust

    def random_event(self):
        prev_rust = self.rust

        random = Random().randint(0, 3)

        if random == 1:
            print(f"\nOh no, {self.name} stepped into a puddle!")
            self.rust = min(self.rust + 10, 100)
        elif random == 2:
            print(f"\nOh, {self.name} encountered a sprinkler!")
            self.rust = min(self.rust + 30, 100)
        elif random == 3:
            print(f"\nGuess what! {self.name} fell into the pool!")
            self.rust = min(self.rust + 50, 100)

        return prev_rust, self.rust

    def learn(self):
        prev_skill = self.skills
        prev_overheat = self.overheat
        prev_battery = self.battery
        prev_boredom = self.boredom

        if prev_skill < 100:
            self.skills = min(self.skills + 10, 100)
            self.battery = max(self.battery - 10, 0)
            self.overheat = min(self.overheat + 10, 100)
            self.boredom = min(self.boredom + 5, 100)

        return prev_skill, self.skills, prev_overheat, self.overheat,\
            prev_battery, self.battery, prev_boredom, self.boredom

    def work(self):
        prev_battery = self.battery
        prev_boredom = self.boredom
        prev_overheat = self.overheat

        self.battery = max(self.battery - 10, 0)
        self.boredom = min(self.boredom + 10, 100)
        self.overheat = min(self.overheat + 10, 100)

        prev_rust, curr_rust = self.random_event()

        return prev_battery, self.battery, prev_boredom,\
            self.boredom, prev_overheat, self.overheat, prev_rust, curr_rust

    def charge(self):
        prev_battery = self.battery
        prev_overheat = self.overheat
        prev_boredom = self.boredom

        if prev_battery < 100:
            self.battery = min(self.battery + 10, 100)
            self.overheat = max(self.overheat - 5, 0)
            self.boredom = min(self.boredom + 5, 100)

        return prev_battery, self.battery, prev_overheat, \
            self.overheat, prev_boredom, self.boredom

    def sleep(self):
        prev_overheat = self.overheat

        self.overheat = max(self.overheat - 20, 0)

        return prev_overheat, self.overheat

    def play(self):
        print("\nWhich game would you like to play?")

        while True:
            game_name = input().lower()

            if game_name == "rock-paper-scissors":
                win_count, lose_count, draw_count = self.play_prs()
                break
            elif game_name == "numbers":
                win_count, lose_count, draw_count = self.play_numbers()
                break
            else:
                print("\nPlease choose a valid option: Numbers or Rock-paper-scissors?\n")

        print(f"\nYou won: {win_count},"
              f"\nThe robot won: {lose_count},"
              f"\nDraws: {draw_count}.")

        prev_boredom = self.boredom
        prev_overheat = self.overheat

        self.boredom = max(self.boredom - 20, 0)
        self.overheat += 10

        prev_rust, curr_rust = self.random_event()

        return prev_boredom, self.boredom, prev_overheat,\
            self.overheat, prev_rust, curr_rust

    def play_numbers(self):
        numbers_win_count = 0
        numbers_lose_count = 0
        numbers_draw_count = 0
        random = Random()

        while True:
            correct_number = random.randint(0, 1000000)
            print("\nWhat is your number?")

            command = input()
            if command == "exit game":
                break
            else:
                try:
                    number = int(command)

                    if number < 0:
                        print("\nThe number can't be negative!")
                        continue
                    elif number > 1000000:
                        print("\nInvalid input! The number can't be bigger than 1000000.")
                        continue

                    robot_number = random.randint(0, 1000000)

                    print(f"\nThe robot entered the number {robot_number}.\n"
                          f"The goal number is {correct_number}.")
                    if abs(robot_number - correct_number) < abs(number - correct_number):
                        print("The robot won!")
                        numbers_lose_count += 1
                    elif abs(robot_number - correct_number) == abs(number - correct_number):
                        print("It's a draw!")
                        numbers_draw_count += 1
                    else:
                        print("You won!")
                        numbers_win_count += 1

                except ValueError:
                    print("\nA string is not a valid input!")

        return numbers_win_count, numbers_lose_count, numbers_draw_count

    def play_prs(self):
        prs_win_count = 0
        prs_lose_count = 0
        prs_draw_count = 0
        random = Random()
        winning_conditions = {"paper": "rock", "rock": "scissors", "scissors": "paper"}
        choices = ["paper", "rock", "scissors"]

        while True:
            print("\nWhat is your move?")
            move = input().lower()

            if move == "exit game":
                break

            if move not in choices:
                print("No such option! Try again!")
            else:
                num = random.randint(0, 2)
                robot_move = choices[num]
                print(f"Robot chose {robot_move}")

                if move == robot_move:
                    print("It's a draw!")
                    prs_draw_count += 1
                elif winning_conditions[move] == robot_move:
                    print("You won!")
                    prs_win_count += 1
                else:
                    print("Robot won!")
                    prs_lose_count += 1

        return prs_win_count, prs_lose_count, prs_draw_count
