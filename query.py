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