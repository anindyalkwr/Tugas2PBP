from django import forms
from todolist.models import TaskItem

class TaskItemForm(forms.ModelForm):
    class Meta:
        model = TaskItem
        fields = {'title', 'description'}