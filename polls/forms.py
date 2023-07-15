from django import forms
from .models import Person
from django.utils import timezone


class TriangleForm(forms.Form):
    tri_a = forms.IntegerField(label='Triangle_a')
    tri_b = forms.IntegerField(label='Triangle_b')


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']


class ReminderForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    datetime = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        help_text='Please select a future date and time'
    )

    def clean_datetime(self):
        datetime = self.cleaned_data.get('datetime')

        if datetime and datetime <= timezone.now():
            raise forms.ValidationError('Please select a future date and time')

        return datetime
