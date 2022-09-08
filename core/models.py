from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.constraints import UniqueConstraint


class CustomUser(AbstractUser):
    def __str__(self):
        return self.username

class Habit(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name= 'habits')
    created_at = models.DateField(db_index=True, auto_now_add=True, null=True)
    habit_name = models.CharField(max_length=200)
    goal_amount = models.IntegerField(null=True)
    unit = models.CharField(max_length=200)
    
    def __str__(self):
        return self.habit_name

class DailyRecord(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name= 'habits')
    date = models.DateField(null=True)
    amount_completed = models.IntegerField(null=True)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['habit', 'date'], name='unique_constraint')
        ]

    def __str__(self):
        return str(self.date)