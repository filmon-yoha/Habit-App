import unittest
from django.test import TestCase
from .models import HabitModel,TaskModel
import datetime

class Model_Test(TestCase):
    def test_name_field(self):
        # Testing name field of Habit Model
        habit = HabitModel.objects.create(name='Run',start_date=datetime.datetime.now(),finish_date=datetime.datetime.now())
        self.assertEqual('Run',str(habit.name))
    def test_duration_field(self):
        # Testing duration field of Habit Model
        habit = HabitModel.objects.create(name='jump',start_date=datetime.datetime.now(),finish_date=datetime.datetime.now(),duration='DAILY')
        self.assertEqual('DAILY',habit.duration)
    def test_start_date_field(self):
        # Testing start date field of Habit Model
        habit = HabitModel.objects.create(name='swim',start_date=datetime.datetime.now(),finish_date=datetime.datetime.now())
        self.assertEqual(datetime.datetime.now(),habit.start_date)
    def test_finish_date_field(self):
        # Testing finish date of Habit Model
        habit = HabitModel.objects.create(name='jog',start_date=datetime.datetime.now(),finish_date=datetime.datetime.now())
        self.assertEqual(datetime.datetime.now(),habit.finish_date)
    def test_completed_field(self):
        # Testing completed field of Task Model
        habit = HabitModel.objects.create(name='swim',start_date=datetime.datetime.now(),finish_date=datetime.datetime.now())
        task = TaskModel.objects.create(completed=True,task_date=datetime.datetime.now(),habit_id=habit)
        self.assertEqual(True,task.completed)
    def test_task_date_field(self):
        # Testing task date of Task Model
        habit = HabitModel.objects.create(name='play',start_date=datetime.datetime.now(),finish_date=datetime.datetime.now())
        task = TaskModel.objects.create(completed=False,task_date=datetime.datetime.now(),habit_id=habit)
        self.assertEqual(datetime.datetime.now(),task.task_date)


    
    

