from habit import *
from query import *

def createHabit(name, period):
    habit = Habit(name, period)
    if habit.existsInDB():
        raise Exception("Habit already exists")

    habit.sync()
    return habit

def checkoffHabit(habit, date):
    event = Event(habit, date)
    if not event.existsInDB():
        event.sync()

habit1 = createHabit("habit1", 'daily')
checkoffHabit(habit1, 'yesterday')
checkoffHabit(habit1, 'today')

habit1 = createHabit("habit 2", 'weekly')

query = Query()
habbitList = query.getHabitList()

for h in habbitList:
    print(h.name, h.period)