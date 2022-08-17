from django import forms
from .models import HabitModel

class HabitForm(forms.ModelForm):
    # Creation of the form
    class Meta:
        model = HabitModel
        fields = ('name','duration','start_date','finish_date')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.Select(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'finish_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
            }