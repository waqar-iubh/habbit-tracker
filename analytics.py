from datetime import datetime
from database import *

class Analytics:
    """ Class representing the Analytics module """

    def __init__(self):
        self.db = Database('habit.db')
    
    def getHabitList(self):
        """ Get list of all Habits """
        from habit import Habit
        habitList = self.db.readHabitTable()
        result = []
        for hbt in habitList:
            habit = Habit(hbt['name'], hbt['period'])
            habit.loadEvents()
            result.append(habit)

        return result
    
    def getHabitListByPeriod(self, period):
        """ Get habit list by period """
        from habit import Habit
        if period not in ['daily', 'weekly']:
            raise Exception(f"Invalid period {period}")

        habitList = self.db.readHabitTable()
        result = []
        for hbt in habitList:
            if hbt['period'] == period:
                habit = Habit(hbt['name'], hbt['period'])
                habit.loadEvents()
                result.append(habit)

        return result

    def getHabitByName(self, name):
        """ Get habit by name """
        from habit import Habit
        habit = None
        entry = self.db.readHabit(name)
        if entry is not None:
            habit = Habit(entry['name'], entry['period'])
            habit.loadEvents()

        return habit

    def getLongestStreakForHabit(self, name):
        """ Get the longest streak for specified habit """
        habit = self.getHabitByName(name)
        #events = self.getEventsList(habit)
        sorted_events = sorted(habit.events, key=lambda e: datetime.strptime(e.date, '%Y/%m/%d'))

        longest = ('', 0)
        current = ('', 0)
        if len(sorted_events) > 0:
            current = (sorted_events[0].date, 1)

        for i in range(0, len(sorted_events) - 1):
            delta = self.dateFromString(sorted_events[i+1].date) - self.dateFromString(sorted_events[i].date)

            if habit.period == 'daily' and delta.days == 1:
                current = (current[0], current[1] + 1)
            elif habit.period == 'weekly' and delta.days <= 7:
                current = (current[0], current[1] + delta.days)
            else:
                if current[1] >= longest[1]:
                    longest = current
                current = (sorted_events[i+1].date, 1)

        return current if current[1] >= longest[1] else longest

    def getLongestStreakForAllHabits(self):
        """ Get the longest streak for all habits """
        query = Analytics()
        habbitList = query.getHabitList()
        longest_period = ('', 0)
        longest_name = ''

        for h in habbitList:
            streak = query.getLongestStreakForHabit(h.name)
            if streak[1] >= longest_period[1]:
                longest_period = streak
                longest_name = h.name
        
        return longest_period, longest_name
    
    def dateFromString(self, datestr):
        """ Convert string to datetime object """
        return datetime.strptime(datestr, '%Y/%m/%d')

    def dateToString(self, date):
        """ Conver datetime object to string """
        return date.strftime('%Y/%m/%d')
