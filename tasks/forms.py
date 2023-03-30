from django import forms 
from .models import Tasks

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'description', 'important']
        widgets={
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Type a Title'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Type a Description'}),
            'important': forms.CheckboxInput(attrs={'class':'form-check-input m-auto'}),
        }