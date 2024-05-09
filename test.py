from datetime import datetime
from habit import *
from analytics import *

import unittest

class TestHabitTracker(unittest.TestCase):
    """ Unit tests for Habit Tracker """

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
        habit.completeHabit("2024/04/28")
        self.assertEqual(len(habit.events) , 1)
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
        habit.completeHabit("2024/05/1")
        habit.completeHabit("2024/05/2")
        habit.completeHabit("2024/05/3")
        habit.completeHabit("2024/05/5")
        query = Analytics()
        streak = query.getLongestStreakForHabit("habit1")
        self.assertEqual(streak[0], "2024/05/1")
        self.assertEqual(streak[1], 3)
        deleteHabit("habit1")

    def testLongestStreakForAllHabits(self):
        """ Test longestStreakForAllHabits """

        habit1 = createHabit("habit1", "daily")
        habit1.completeHabit("2024/05/1")
        habit1.completeHabit("2024/05/2")
        habit1.completeHabit("2024/05/3")

        habit2 = createHabit("habit2", "weekly")
        habit2.completeHabit("2024/05/4")
        habit2.completeHabit("2024/05/11")
        habit2.completeHabit("2024/05/18")

        query = Analytics()
        streak, name = query.getLongestStreakForAllHabits()
        self.assertEqual(streak[0], "2024/05/4")
        self.assertEqual(streak[1], 15)
        self.assertEqual(name, "habit2")
        deleteHabit("habit1")
        deleteHabit("habit2")


if __name__ == '__main__':
    unittest.main()
