import pathlib
from tinydb import TinyDB, Query

class Database:
    
    # Initialize database
    def __init__(self, databasePath):
        self.db = TinyDB(databasePath)
        self.habitTable = self.db.table('Habits')
        self.eventTable = self.db.table('Events')
    
    # Write Habit to database
    def writeHabit(self, name, period):
        self.habitTable.insert({'name': name, 'period': period})

    # Read Habit from database
    def readHabit(self, name):
        query = Query()
        return self.habitTable.get(query.name == name)

    # Get the list of all Habits in the database
    def readHabitTable(self):
        query = Query()
        return self.habitTable.all()

    # Write event to database
    def writeEvent(self, habit, date):
        self.eventTable.insert({'habit': habit, 'date': date})

    # Get events for habit from from database
    def readEvent(self, habit):
        query = Query()
        return self.eventTable.search(query.habit.all([habit]))