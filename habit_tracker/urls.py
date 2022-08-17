from django.urls import path
from . import views
# Setting URLs
urlpatterns = [
    path('',views.Add_Habit_View.as_view(),name='add-habit'),
    path('habits/',views.All_Habits_View.as_view(),name='habits'),
    path('daily/',views.daily_habits,name='daily'),
    path('weekly/',views.weekly_habits,name='weekly'),
    path('habits/delete/<pk>',views.Delete_Habit.as_view(),name='delete'),
    path('habits/update/<pk>', views.Update_Habit.as_view(),name='update'),
    path('tasks/<pk>',views.TasksView.as_view(),name='tasks'),
    path('update_task/<pk>',views.UpdateTaskView.as_view(),name='update_task'),
    path('streak/<pk>', views.StreakView.as_view(), name='streak'),
    path('streaks/', views.StreaksView.as_view(), name='streaks')
]