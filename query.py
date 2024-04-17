from database import *
from habit import *

class Query:
    def __init__(self):
        self.db = Database('habit.db')
    
    def getHabitList(self):
        habitList = self.db.readHabitTable()
        result = []
        for hbt in habitList:
            result.append(Habit(hbt['name'], hbt['period']))

        return result

    def getHabitByName(self, name):
        habit = None
        entry = self.db.readHabit(name)
        if entry is not None:
            habit = Habit(entry['name'], entry['period'])

        return habit
        