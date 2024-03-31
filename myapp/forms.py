from django import forms
from .model.task import Task

class TodoForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','complete']
        widgets = {
            'user':forms.Select(attrs={'class':'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
