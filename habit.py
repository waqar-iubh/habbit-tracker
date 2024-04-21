
from database import *

class Event:
    def __init__(self, habit, date):
        self.db = Database('habit.db')
        self.habit = habit.name
        self.date = date

    # Sync to databse
    def sync(self):
        self.db.writeEvent(self.habit, self.date)
    
    # Check if already exists in DB
    def existsInDB(self):
        events = self.db.readEvent(self.habit)
        for ev in events:
            if ev['date'] == self.date:
                return True
        return False 

class Habit:
    def __init__(self, name, period):
        self.db = Database('habit.db')
        self.name = name
        self.period = period

    # Sync to databse
    def sync(self):
        self.db.writeHabit(self.name, self.period)
    
    # Check if already exists in DB
    def existsInDB(self):
        record = self.db.readHabit(self.name)
        return False if record is None else True

    # Complete habit
    def completeHabit(self, date):
        event = Event(self, date)
        if not event.existsInDB():
            event.sync()