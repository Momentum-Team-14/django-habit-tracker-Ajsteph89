from django import forms
from .models import Habit, DailyRecord



class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ('habit_name', 'goal_amount', 'unit')

class RecordForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = DailyRecord
        fields = ('date', 'amount_completed')