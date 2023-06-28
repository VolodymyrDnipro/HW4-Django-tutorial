from django import forms
from .models import Person


class TriangleForm(forms.Form):
    tri_a = forms.IntegerField(label='Triangle_a')
    tri_b = forms.IntegerField(label='Triangle_b')


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']
