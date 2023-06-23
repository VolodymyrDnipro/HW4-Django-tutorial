from django.shortcuts import render
import math
from .forms import TriangleForm


def index(request):
    return render(request, 'polls/index.html')


def triangle(request):
    if request.method == 'POST':
        triangle_form = TriangleForm(request.POST)

        if triangle_form.is_valid():
            leg_a = triangle_form.cleaned_data['tri_a']
            print(leg_a)
            leg_b = triangle_form.cleaned_data['tri_b']
            hyp = math.sqrt(leg_a ** 2 + leg_b ** 2)
            content = {'triangle_form': triangle_form, 'hyp': hyp}
            return render(request, 'polls/triangle.html', content)
    else:
        triangle_form = TriangleForm()

    return render(request, 'polls/triangle.html', {'triangle_form': triangle_form})
