# Write your code here
from Robogotchi.task.robogotchi.Robot import Robot

if __name__ == "__main__":
    print("How will you call your robot?")
    robot = Robot(input())

    while True:

        if robot.overheat >= 100:
            print(f"\nThe level of overheat reached 100, "
                  f"{robot.name} has blown up! Game over. Try again?")
            break

        if robot.rust >= 100:
            print(f"\n{robot.name} is too rusty! Game over. Try again?")
            break

        print(f"\nAvailable interactions with {robot.name}:\n"
              f"exit – Exit\n"
              f"info – Check the vitals\n"
              f"work – Work\n"
              f"play – Play\n"
              f"oil – Oil\n"
              f"recharge – Recharge\n"
              f"sleep – Sleep mode\n"
              f"learn – Learn skills\n\n"
              f"Choose:")

        choice = input().lower()

        if choice == "exit":
            print("\nGame over")
            break
        elif choice != "recharge" and robot.battery <= 0:
            print(f"\nThe level of the battery is 0, "
                  f"{robot.name} needs recharging!")
        elif choice != "play" and robot.boredom >= 100:
            print(f"\n{robot.name} is too bored! "
                  f"{robot.name} needs to have fun!")
        elif choice == "info":
            print(f"\n{robot.name}'s stats are: the battery is {robot.battery},\n"
                  f"overheat is {robot.overheat},\n"
                  f"skill level is {robot.skills},\n"
                  f"boredom is {robot.boredom},\n"
                  f"rust is {robot.rust}.")
        elif choice == "recharge":
            prev_battery, curr_battery, prev_overheat, \
                curr_overheat, prev_boredom, curr_boredom = robot.charge()

            if prev_battery == 100:
                print(f"\n{robot.name} is charged!")
            else:
                print(f"\n{robot.name}'s level of overheat was {prev_overheat}."
                      f" Now it is {curr_overheat}.\n"
                      f"{robot.name}'s level of the battery was {prev_battery}. "
                      f"Now it is {curr_battery}.\n"
                      f"{robot.name}'s level of boredom was {prev_boredom}. "
                      f"Now it is {curr_boredom}.\n"
                      f"{robot.name} is recharged!")
        elif choice == "sleep":
            prev_overheat, curr_overheat = robot.sleep()

            if prev_overheat == 0:
                print(f"\n{robot.name} is cool!")
            else:
                print(f"\n{robot.name}'s level of overheat was {prev_overheat}. "
                      f"Now it is {curr_overheat}.")
                if curr_overheat == 0:
                    print(f"\n{robot.name} is cool")
                else:
                    print(f"\n{robot.name} cooled off!")
        elif choice == "play":
            prev_boredom, curr_boredom, prev_overheat,\
                curr_overheat, prev_rust, curr_rust = robot.play()

            print(f"\n{robot.name}'s level of boredom was {prev_boredom}. "
                  f"Now it is {curr_boredom}.\n"
                  f"{robot.name}'s level of overheat was {prev_overheat}. "
                  f"Now it is {curr_overheat}.")

            if prev_rust != curr_rust:
                print(f"{robot.name}'s level of rust was {prev_rust}. "
                      f"Now it is {curr_rust}.")
            if curr_boredom <= 0:
                print(f"{robot.name} is in a great mood")
        elif choice == "learn":
            prev_skill, curr_skill, prev_overheat, curr_overheat,\
                prev_battery, curr_battery, prev_boredom, curr_boredom = robot.learn()

            if prev_skill >= 100:
                print(f"\nThere's nothing for {robot.name} to learn!")
            else:
                print(f"\n{robot.name}'s level of skill was {prev_skill}. "
                      f"Now it is {curr_skill}.\n"
                      f"{robot.name}'s level of overheat was {prev_overheat}. "
                      f"Now it is {curr_overheat}.\n"
                      f"{robot.name}'s level of the battery was {prev_battery}. "
                      f"Now it is {curr_battery}.\n"
                      f"{robot.name}'s level of boredom was {prev_boredom}. "
                      f"Now it is {curr_boredom}.\n\n"
                      f"{robot.name} has become smarter!")
        elif choice == "work":
            if robot.skills < 50:
                print(f"\n{robot.name} has got to learn before working!")
            else:
                prev_battery, curr_battery, prev_boredom, curr_boredom,\
                    prev_overheat, curr_overheat, prev_rust, curr_rust = robot.work()

                print(f"\n{robot.name}'s level of boredom was {prev_boredom}. "
                      f"Now it is {curr_boredom}.\n"
                      f"{robot.name}'s level of overheat was {prev_overheat}. "
                      f"Now it is {curr_overheat}.\n"
                      f"{robot.name}'s level of the battery was {prev_battery}. "
                      f"Now it is {curr_battery}.")

                if prev_rust != curr_rust:
                    print(f"{robot.name}'s level of rust was {prev_rust}. "
                          f"Now it is {curr_rust}.\n")

                print(f"{robot.name} did well!")
        elif choice == "oil":
            prev_rust, curr_rust = robot.oil()

            if prev_rust <= 0:
                print(f"\n{robot.name} is fine, no need to oil!")
            else:
                print(f"\n{robot.name}'s level of rust was {prev_rust}. "
                      f"Now it is {curr_rust}. {robot.name} is less rusty!")
        else:
            print("\nInvalid input, try again!")
