from database import *
from analytics import *

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
        events = self.db.readEvents(self.habit)
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

    # Get list of completion events for Habit
    def getCompletionEvents(self):
        events = self.db.readEvents(self.name)
        eventList = []
        for evt in events:
            eventList.append(Event(self, evt['date']))
        return eventList
    
    # Remove Habit from database
    def deleteHabit(self):
        self.db.deleteEvents(self.name)
        self.db.deleteHabit(self.name)


def createHabit(name, period):
    habit = Habit(name, period)
    if habit.existsInDB():
        raise Exception(f"Habit {name} already exists")

    if period not in ['daily', 'weekly']:
        raise Exception(f"Invalid period {period}")

    habit.sync()
    return habit


def completeHabit(name, date):
    query = Analytics()
    habit = query.getHabitByName(name)
    if habit is None:
        raise Exception(f"Habit '{name}' does not exist")
    
    habit.completeHabit(date)


def deleteHabit(name):
    query = Analytics()
    habit = query.getHabitByName(name)
    if habit is None:
        raise Exception(f"Habit '{name}' does not exist")

    habit.deleteHabit()