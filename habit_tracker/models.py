from django.db import models
from model_utils import Choices

# Creation of Database

class HabitModel(models.Model):
    # Creation of the Habit table
    class Meta:
        db_table = "habit"
    
    name = models.CharField(max_length=100)
    duration = models.CharField(max_length=100, choices=Choices('DAILY','WEEKLY'), default=Choices('DAILY'))
    completed = models.BooleanField(default=False)
    start_date = models.DateField()
    finish_date = models.DateField()

    def __str__(self):
        return self.name

class TaskModel(models.Model):
    # Creation of the Task Table
    class Meta:
        db_table = "task"
    
    completed = models.BooleanField(default=False)
    task_date = models.DateField()
    habit_id = models.ForeignKey(HabitModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.habit_id.name


