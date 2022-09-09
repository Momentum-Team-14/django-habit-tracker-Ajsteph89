from django.shortcuts import render, redirect, get_object_or_404
from core.models import DailyRecord, Habit
from .forms import HabitForm, RecordForm
from django.contrib.auth.decorators import login_required
from django.db.models import F

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return redirect("list_habits")
    return render(request, "core/home.html")

@login_required
def list_habits(request):
    habits = Habit.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'core/list_habits.html', {'habits': habits})

@login_required
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

@login_required
def habit_detail(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    records = habit.records.all().order_by('-date')
    for record in records:
        percentage = 100 * (record.amount_completed / habit.goal_amount) 
    return render(request, "core/habit_detail.html", {'records':records,
        'habit':habit, 'percentage':percentage})

@login_required
def add_record(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == "POST":
        record_form = RecordForm(request.POST)
        if record_form.is_valid():
            record = record_form.save(commit=False)
            record.habit = habit
            record.save()
            return redirect('habit_detail', pk=pk)
    else:
        record_form = RecordForm()
    return render(request, 'core/add_record.html', {'record_form': record_form})

@login_required
def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == "POST":
        habit_form = HabitForm(request.POST, instance=habit)
        if habit_form.is_valid():
            habit = habit_form.save(commit=False)
            habit.save()
            return redirect('list_habits')
    else:
        habit_form = HabitForm(instance=habit)
    return render(request, 'core/edit_habit.html', {'habit_form': habit_form})

@login_required
def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    habit.delete()
    return redirect('list_habits')

@login_required
def edit_record(request, pk1, pk2):
    record = get_object_or_404(DailyRecord, pk=pk2)
    habit = get_object_or_404(Habit, pk=pk1)
    if request.method == "POST":
        record_form = RecordForm(request.POST, instance=record)
        if record_form.is_valid():
            record = record_form.save(commit=False)
            record.habit = habit
            record.user = request.user
            record.save()
            return redirect('habit_detail', pk=pk1)
    else:
        record_form = RecordForm(instance=record)
    return render(request, 'core/edit_record.html', {'record_form': record_form})

@login_required
def delete_record(request, pk1, pk2):
    record = get_object_or_404(DailyRecord, pk=pk2)
    record.delete()
    habit = get_object_or_404(Habit, pk=pk1)
    return redirect('habit_detail', pk=pk1)