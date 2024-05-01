from database import *
from analytics import *

class Event:
    def __init__(self, habit, date):
        self.db = Database('habit.db')
        self.habit = habit.name
        self.date = date

    def sync(self):
        """ Sync Event to databse """
        self.db.writeEvent(self.habit, self.date)
    
    def existsInDB(self):
        """ Check if Event already exists in DB """
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

    def sync(self):
        """ Sync Habit object to databse """
        self.db.writeHabit(self.name, self.period)
    
    def existsInDB(self):
        """ Check if Habit already exists in DB """
        record = self.db.readHabit(self.name)
        return False if record is None else True

    def completeHabit(self, date):
        """ Create a completion event for habit """
        event = Event(self, date)
        if not event.existsInDB():
            event.sync()

    def getCompletionEvents(self):
        """ Get list of completion events for Habit """
        events = self.db.readEvents(self.name)
        eventList = []
        for evt in events:
            eventList.append(Event(self, evt['date']))
        return eventList
    
    def deleteHabit(self):
        """ Remove Habit from database"""
        self.db.deleteEvents(self.name)
        self.db.deleteHabit(self.name)


def createHabit(name, period):
    """ Create and return a Habit object """
    habit = Habit(name, period)
    if habit.existsInDB():
        raise Exception(f"Habit {name} already exists")

    if period not in ['daily', 'weekly']:
        raise Exception(f"Invalid period {period}")

    habit.sync()
    return habit


def completeHabit(name, date):
    """ Complete specified Habit """
    query = Analytics()
    habit = query.getHabitByName(name)
    if habit is None:
        raise Exception(f"Habit '{name}' does not exist")
    
    habit.completeHabit(date)


def deleteHabit(name):
    """ Delete sepcified Habit """
    query = Analytics()
    habit = query.getHabitByName(name)
    if habit is None:
        raise Exception(f"Habit '{name}' does not exist")

    habit.deleteHabit()