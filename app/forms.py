from django import forms

class TodoForm(forms.Form):
    content = forms.CharField(max_length=100, label=False)