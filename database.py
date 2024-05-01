import pathlib
from tinydb import TinyDB, Query

class Database:
    
    def __init__(self, databasePath):
        """ Initialize database """
        self.databasePath = databasePath
    
    def writeHabit(self, name, period):
        """ Write Habit to database """
        db = TinyDB(self.databasePath)
        habitTable = db.table('Habits')
        habitTable.insert({'name': name, 'period': period})
        db.close()

    def readHabit(self, name):
        """ Read Habit from database """
        db = TinyDB(self.databasePath)
        habitTable = db.table('Habits')
        query = Query()
        res = habitTable.get(query.name == name)
        db.close()
        return res

    def readHabitTable(self):
        """ Get the list of all Habits in the database """
        db = TinyDB(self.databasePath)
        habitTable = db.table('Habits')
        res = habitTable.all()
        db.close()
        return res

    def deleteHabit(self, name):
        """ Delete Habit from database """
        db = TinyDB(self.databasePath)
        habitTable = db.table('Habits')
        query = Query()
        habitTable.remove(query.name == name)
        db.close()

    def writeEvent(self, habit, date):
        """ Write event to database """
        db = TinyDB(self.databasePath)
        eventTable = db.table('Events')
        eventTable.insert({'habit': habit, 'date': date})
        db.close()

    def readEvents(self, habit):
        """ Get events for habit from from database """
        db = TinyDB(self.databasePath)
        eventTable = db.table('Events')
        query = Query()
        res = eventTable.search(query.habit.all([habit]))
        db.close()
        return res
    
    def deleteEvents(self, habit):
        """ Delete Events for Habit from database """
        db = TinyDB(self.databasePath)
        eventTable = db.table('Events')
        query = Query()
        eventTable.remove(query.habit == habit)
        db.close()