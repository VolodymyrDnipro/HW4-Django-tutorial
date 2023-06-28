from django.shortcuts import render, get_object_or_404, redirect
import math
from .forms import TriangleForm, PersonForm
from .models import Person


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


def create_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('polls:create_person')
    else:
        form = PersonForm()
    return render(request, 'polls/create_person.html', {'form': form})


def edit_person(request, id):
    person = get_object_or_404(Person, pk=id)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('polls:create_person')
    else:
        form = PersonForm(instance=person)
    return render(request, 'polls/edit_person.html', {'form': form})
