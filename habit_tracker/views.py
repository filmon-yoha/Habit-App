from django.shortcuts import render,redirect
from django import views
from .forms import HabitForm
from .models import HabitModel, TaskModel
import datetime
from django.views.generic.edit import DeleteView , UpdateView
from itertools import groupby

class Add_Habit_View(views.View):
    def get(self,request):
        # Return the same page if the required inputs are not given
        form = HabitForm()
        return render(request,'add_habit.html',{'form':form})
    def post(self,request):
        # Store data from user in the Habit and Task tables
        data = request.POST
        habit_exists = HabitModel.objects.filter( name = data.get('name')).exists()
        if habit_exists:
            return redirect('/')
        
        start_date = data.get('start_date')
        finish_date = data.get('finish_date')
        duration = data.get('duration')
        
        new_start_date = start_date.replace('-','/')
        new_finish_date = finish_date.replace('-','/')

        date_format = "%Y/%m/%d"

        d1 = datetime.datetime.strptime(new_start_date,date_format).date()
        d2 = datetime.datetime.strptime(new_finish_date,date_format).date()
        
        step = ''
        if duration == ('DAILY'):
            step = datetime.timedelta(days=1)
        elif duration == ('WEEKLY'):
            step = datetime.timedelta(days=7)
        
        habit_model = HabitForm(data)

        if habit_model.is_valid():
            habit = habit_model.save()
            
        saved_habit = HabitModel.objects.filter(name=habit)

        while d1 <= d2:
            date = d1.strftime(date_format)
            new_date = date.replace('/','-')
            task = TaskModel(completed=False, task_date=new_date , habit_id=saved_habit[0])
            task.save()
            d1 += step
        return redirect('/habits')
        
class All_Habits_View(views.View):
    def get(self,request):
        # Returns all habits user has created
        all_habits = HabitModel.objects.all()
        return render(request,'all_habits.html',{'habits':all_habits})

def daily_habits(request):
    # Returns habits with daily duration
    daily_habits = HabitModel.objects.filter(duration='DAILY')
    return render(request,'all_habits.html',{'habits':daily_habits})

def weekly_habits(request):
    #Returns habits with weekly duration
    weekly_habits = HabitModel.objects.filter(duration='WEEKLY')
    return render(request,'all_habits.html',{'habits':weekly_habits})

class Delete_Habit(DeleteView):
    # Enables the deleting of habits
    model = HabitModel
    success_url = '/habits'

class Update_Habit(UpdateView):
    # Enables the updating of habits
    model = HabitModel
    success_url = '/habits'
    template_name = 'update.html'
    fields = ['completed']

class TasksView(views.View):
    def get(self, request, pk):
        # Returns task dates
        tasks = TaskModel.objects.filter(habit_id=pk)
        return render(request, 'tasks.html', {'tasks': tasks})

class UpdateTaskView(UpdateView):
    # Enables user to update task dates
    model = TaskModel
    template_name = "TaskModel_form.html"
    fields = ["completed"]
    success_url = "/habits"

class StreakView(views.View):
    def number_formatted(self, tasks):
        # Will assign value of 1 if task is mark completed and 0 if not
        number_tasks = []
        for task in tasks:
            if task.completed:
                number_tasks.append(1)
            else:
                number_tasks.append(0)
        return number_tasks

    def len_iter(self, items):
        # Completes sum of task marked completed
        return sum(1 for _ in items)

    def get(self, request, pk):
        # Retrieves the streak for habit selected
        habit = HabitModel.objects.filter(id=pk)
        tasks = TaskModel.objects.filter(habit_id=habit[0])
        number_tasks = self.number_formatted(tasks)

        def consecutive_one(data) -> int:
            if number_tasks.__contains__(1):
                return max(self.len_iter(run) for val, run in groupby(data) if val)
            else:
                return 0

        longest_streak = consecutive_one(number_tasks)

        return render(request, 'streak.html', {'streak': longest_streak})

class StreaksView(views.View):
    def get(self, request):
        # Displays the streak for each habit
        habits = HabitModel.objects.all()
        habit_streaks = []
        for habit in habits:
            tasks = TaskModel.objects.filter(habit_id=habit)
            number_tasks = []
            for task in tasks:
                if task.completed:
                    number_tasks.append(1)
                else:
                    number_tasks.append(0)
            def len_iter(items):
                return sum(1 for _ in items)
            def consecutive_one(data) -> int:
                if number_tasks.__contains__(1):
                    return max(len_iter(run) for val, run in groupby(data) if val)
                else:
                    return 0
            longest_streak = consecutive_one(number_tasks)
            habit_streak = HabitStreaks()
            habit_streak.habit_id = habit.name
            habit_streak.streak = longest_streak
            habit_streaks.append(habit_streak)
            
        return render(request, 'streaks.html', {'habit_streaks': habit_streaks})

class HabitStreaks:
    def __int__(self, habit_id, streak):
        self.habit_id = habit_id
        self.streak = streak




        
