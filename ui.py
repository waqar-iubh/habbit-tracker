import traceback
from datetime import datetime

from habit import *
from query import *

def createHabit(name, period):
    habit = Habit(name, period)
    if habit.existsInDB():
        raise Exception(f"Habit {name} already exists")

    habit.sync()
    return habit

def listHabits():
    query = Query()
    habbitList = query.getHabitList()
    for h in habbitList:
        print(f" {h.name} ({h.period})")

def main():
    try:
        habit1 = createHabit("habit1", 'daily')
        habit2 = createHabit("habit2", 'weekly')
        listHabits()
        
        date = datetime(2024, 4, 23)
        habit1.completeHabit(date.strftime('%Y/%m/%d'))
        
        date = datetime(2024, 4, 21)
        habit1.completeHabit(date.strftime('%Y/%m/%d'))

        date = datetime(2024, 4, 20)
        habit1.completeHabit(date.strftime('%Y/%m/%d'))

        date = datetime(2024, 4, 17)
        habit1.completeHabit(date.strftime('%Y/%m/%d'))

        date = datetime(2024, 4, 16)
        habit1.completeHabit(date.strftime('%Y/%m/%d'))

        date = datetime(2024, 4, 10)
        habit1.completeHabit(date.strftime('%Y/%m/%d'))

        query = Query()
        longest = query.getLongestStreakForHabit('habit1')
        print (longest)


        date = datetime(2024, 4, 1)
        habit2.completeHabit(date.strftime('%Y/%m/%d'))

        date = datetime(2024, 4, 7)
        habit2.completeHabit(date.strftime('%Y/%m/%d'))

        date = datetime(2024, 4, 14)
        habit2.completeHabit(date.strftime('%Y/%m/%d'))

        date = datetime(2024, 4, 22)
        habit2.completeHabit(date.strftime('%Y/%m/%d'))

        date = datetime(2024, 4, 29)
        habit2.completeHabit(date.strftime('%Y/%m/%d'))

        date = datetime(2024, 5, 7)
        habit2.completeHabit(date.strftime('%Y/%m/%d'))

        query = Query()
        longest = query.getLongestStreakForHabit('habit2')
        print(longest)

    except Exception as e: 
        print(e, traceback.format_exc())

if __name__ == "__main__":
    main()