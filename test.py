from datetime import datetime
from habit import *
from analytics import *

import unittest

class TestHabitTracker(unittest.TestCase):

    def testCreateHabit(self):
        createHabit("habit1", "daily")
        query = Analytics()
        habit = query.getHabitByName("habit1")
        self.assertEqual(habit.name, "habit1")
        self.assertEqual(habit.period, "daily")
        deleteHabit("habit1")

    def testCompleteHabit(self):
        habit = createHabit("habit23", "daily")
        completeHabit("habit23", "2024/04/28")
        events = habit.getCompletionEvents()
        self.assertEqual(len(events) , 1)
        deleteHabit("habit23")

    def testDeleteHabit(self):
        habit = createHabit("habit3", "daily")
        deleteHabit("habit3")
        query = Analytics()
        habit = query.getHabitByName("habit3")
        self.assertEqual(habit , None)

if __name__ == '__main__':
    unittest.main()
