from django.shortcuts import render, redirect
from core.models import Habit
from .forms import HabitForm

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return redirect("list_habits")
    return render(request, "core/home.html")

def list_habits(request):
    habits = Habit.objects.filter(user=request.user)
    return render(request, 'core/list_habits.html', {'habits': habits})

def add_habit(request):
    if request.method == "POST":
        habit_form = HabitForm(request.POST)
        if habit_form.is_valid():
            habit = habit_form.save(commit=False)
            habit.user=request.user
            habit.save()
            return redirect('list_habits')
    else:
        habit_form = HabitForm()
    return render(request, 'core/add_habit.html', {'habit_form': habit_form})