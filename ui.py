from datetime import datetime

from habit import *
from analytics import *

def main():
    while(True):
        print("\nChoose an option:")
        print("1) List all habits")
        print("2) Create a habit")
        print("3) Complete a habit")
        print("4) Delete a habit")
        print("5) List habits by period")
        print("6) Show longest streak for habit")
        print("7) Show longest streak for all habits")
        print("8) Exit")

        choice = input("\nEnter choice: ")

        try:
            # List all Habits
            if choice == "1":
                query = Analytics()
                habbitList = query.getHabitList()
                count = 0

                print("\nCurrent habits:\n")
                for h in habbitList:
                    print(f"{count}) {h.name} ({h.period})")
                    count += 1

            # Create a Habit
            elif choice == "2":
                name = input("Enter name: ")
                period = input("Enter period (daily/weekly): ")
                habit = createHabit(name, period)
                print(f"\nHabit '{name}' created")


            # Complete a Habit
            elif choice == "3":
                name = input("Enter name: ")
                date = input("Enter date (YYYY/MM/DD): ")
                datetime.strptime(date, '%Y/%m/%d')
                completeHabit(name, date)
                print(f"\nHabit '{name}' completed")


            # Delete Habit
            elif choice == "4":
                name = input("Enter name: ")
                deleteHabit(name)
                print(f"\nHabit '{name}' deleted")


            # List Habits by Period
            elif choice == "5":
                period = input("Enter period (daily/weekly): ")
                query = Analytics()
                habbitList = query.getHabitListByPeriod(period)
                print(f"\n'{period}' habits:\n")

                count = 0
                for h in habbitList:
                    print(f"{count}) {h.name} ({h.period})")
                    count += 1


            # Show longest streak for Habit
            elif choice == "6":
                name = input("Enter name: ")
                query = Analytics()
                habit = query.getHabitByName(name)
                if habit is None:
                    raise Exception(f"Habit '{name}' does not exist")
                
                streak = query.getLongestStreakForHabit(name)
                print(f"Longest streak for '{name}' is {streak[1]} days starting from {streak[0]}")


            # Show longest streak for all Habits
            elif choice == "7":
                period = input("Enter period (daily/weekly): ")
                query = Analytics()
                longest_period, longest_name = query.getLongestStreakForAllHabits(period)
                print(f"Longest {period} streak is for '{longest_name}' which is {longest_period[1]} days starting from {longest_period[0]}")

            # Exit
            elif choice == "8":
                break
       
            else:
                print('Invalid choice')

        except Exception as e:
            print("\nError: ", e)
        
        input('\nPress enter to continue ...')

if __name__ == "__main__":
    main()