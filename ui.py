import traceback
import datetime

from habit import *
from query import *

def createHabit(name, period):
    habit = Habit(name, period)
    if habit.existsInDB():
        raise Exception(f"Habit {name} already exists")

    habit.sync()
    return habit

def completeHabit(name, date):
    query = Query()
    habit = query.getHabitByName(name)
    if habit is None:
        raise Exception(f"Habit {name} does not exist")

    event = Event(habit, date)
    if not event.existsInDB():
        event.sync()

def listHabits():
    query = Query()
    habbitList = query.getHabitList()
    for h in habbitList:
        print(f" {h.name} ({h.period})")

def main():
    try:
        habit1 = createHabit("habit1", 'daily')
        habit1 = createHabit("habit2", 'weekly')
        habit1 = createHabit("habit3", 'daily')
        habit1 = createHabit("habit4", 'weekly')
        listHabits()
        
        date = datetime.datetime(2024, 4, 16)
        completeHabit('habit1', date.strftime('%Y/%m/%d'))

        date = datetime.datetime(2024, 4, 17)
        completeHabit('habit1', date.strftime('%Y/%m/%d'))
        
    except Exception as e: 
        print(e, traceback.format_exc())

if __name__ == "__main__":
    main()