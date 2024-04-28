from datetime import datetime
from database import *

class Analytics:
    def __init__(self):
        self.db = Database('habit.db')
    
    def getHabitList(self):
        from habit import Habit
        habitList = self.db.readHabitTable()
        result = []
        for hbt in habitList:
            result.append(Habit(hbt['name'], hbt['period']))

        return result
    
    def getHabitListByPeriod(self, period):
        from habit import Habit
        if period not in ['daily', 'weekly']:
            raise Exception(f"Invalid period {period}")

        habitList = self.db.readHabitTable()
        result = []
        for hbt in habitList:
            if hbt.period == period:
                result.append(Habit(hbt['name'], hbt['period']))

        return result

    def getHabitByName(self, name):
        from habit import Habit
        habit = None
        entry = self.db.readHabit(name)
        if entry is not None:
            habit = Habit(entry['name'], entry['period'])

        return habit
    
    def getEventsList(self, habit):
        from habit import Event
        eventsList = self.db.readEvents(habit.name)
        result = []
        for evt in eventsList:
            result.append(Event(habit, evt['date']))
        
        return result

    def getLongestStreakForHabit(self, name):
        habit = self.getHabitByName(name)
        events = self.getEventsList(habit)
        sorted_events = sorted(events, key=lambda e: datetime.strptime(e.date, '%Y/%m/%d'))

        longest = ('', 0)
        current = ('', 0)
        if len(sorted_events) > 0:
            current = (sorted_events[0].date, 1)

        for i in range(0, len(sorted_events) - 1):
            delta = self.dateFromString(sorted_events[i+1].date) - self.dateFromString(sorted_events[i].date)

            if habit.period == 'daily' and delta.days == 1:
                current = (current[0], current[1] + 1)
            if habit.period == 'weekly' and delta.days <= 7:
                current = (current[0], current[1] + delta.days)
            else:
                if current[1] >= longest[1]:
                    longest = current
                current = (sorted_events[i+1].date, 1)

        return current if current[1] >= longest[1] else longest
    
    def dateFromString(self, datestr):
        return datetime.strptime(datestr, '%Y/%m/%d')

    def dateToString(self, date):
        return date.strftime('%Y/%m/%d')
