from datetime import datetime
from habit import *
from analytics import *

import unittest

class TestHabitTracker(unittest.TestCase):

    def testCreateHabit(self):
        """ Test createHabit """

        createHabit("habit1", "daily")
        query = Analytics()
        habit = query.getHabitByName("habit1")
        self.assertEqual(habit.name, "habit1")
        self.assertEqual(habit.period, "daily")
        deleteHabit("habit1")

    def testCompleteHabit(self):
        """ Test completeHabit """

        habit = createHabit("habit2", "daily")
        completeHabit("habit2", "2024/04/28")
        events = habit.getCompletionEvents()
        self.assertEqual(len(events) , 1)
        deleteHabit("habit2")

    def testDeleteHabit(self):
        """ Test deleteHabit """

        habit = createHabit("habit3", "daily")
        deleteHabit("habit3")
        query = Analytics()
        habit = query.getHabitByName("habit3")
        self.assertEqual(habit , None)

    def testLongestStreakForHabit(self):
        """ Test longestStreakForHabit """

        habit = createHabit("habit1", "daily")
        completeHabit("habit1", "2024/05/1")
        completeHabit("habit1", "2024/05/2")
        completeHabit("habit1", "2024/05/3")
        completeHabit("habit1", "2024/05/5")
        query = Analytics()
        streak = query.getLongestStreakForHabit("habit1")
        self.assertEqual(streak[0], "2024/05/1")
        self.assertEqual(streak[1], 3)
        deleteHabit("habit1")

    def testLongestStreakForAllHabits(self):
        """ Test longestStreakForAllHabits """

        habit1 = createHabit("habit1", "daily")
        completeHabit("habit1", "2024/05/1")
        completeHabit("habit1", "2024/05/2")
        completeHabit("habit1", "2024/05/3")

        habit2 = createHabit("habit2", "weekly")
        completeHabit("habit2", "2024/05/4")
        completeHabit("habit2", "2024/05/11")
        completeHabit("habit2", "2024/05/18")

        query = Analytics()
        streak, name = query.getLongestStreakForAllHabits()
        self.assertEqual(streak[0], "2024/05/4")
        self.assertEqual(streak[1], 15)
        self.assertEqual(name, "habit2")
        deleteHabit("habit1")
        deleteHabit("habit2")


if __name__ == '__main__':
    unittest.main()
