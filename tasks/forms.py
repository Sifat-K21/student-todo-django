from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'due_date']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'e.g. Complete Python assignment'}),
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Add a short note...'}),
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }
