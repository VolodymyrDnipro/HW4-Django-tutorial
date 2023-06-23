from django import forms


class TriangleForm(forms.Form):
    tri_a = forms.IntegerField(label='Triangle_a')
    tri_b = forms.IntegerField(label='Triangle_b')
