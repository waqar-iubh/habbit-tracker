import pathlib
from tinydb import TinyDB, Query

class Database:
    
    # Initialize database
    def __init__(self, databasePath):
        self.databasePath = databasePath
    
    # Write Habit to database
    def writeHabit(self, name, period):
        db = TinyDB(self.databasePath)
        habitTable = db.table('Habits')
        habitTable.insert({'name': name, 'period': period})
        db.close()

    # Read Habit from database
    def readHabit(self, name):
        db = TinyDB(self.databasePath)
        habitTable = db.table('Habits')
        query = Query()
        res = habitTable.get(query.name == name)
        db.close()
        return res

    # Get the list of all Habits in the database
    def readHabitTable(self):
        db = TinyDB(self.databasePath)
        habitTable = db.table('Habits')
        res = habitTable.all()
        db.close()
        return res

    # Delete Habit from database
    def deleteHabit(self, name):
        db = TinyDB(self.databasePath)
        habitTable = db.table('Habits')
        query = Query()
        habitTable.remove(query.name == name)
        db.close()

    # Write event to database
    def writeEvent(self, habit, date):
        db = TinyDB(self.databasePath)
        eventTable = db.table('Events')
        eventTable.insert({'habit': habit, 'date': date})
        db.close()

    # Get events for habit from from database
    def readEvents(self, habit):
        db = TinyDB(self.databasePath)
        eventTable = db.table('Events')
        query = Query()
        res = eventTable.search(query.habit.all([habit]))
        db.close()
        return res
    
    # Delete Events for Habit from database
    def deleteEvents(self, habit):
        db = TinyDB(self.databasePath)
        eventTable = db.table('Events')
        query = Query()
        eventTable.remove(query.habit == habit)
        db.close()