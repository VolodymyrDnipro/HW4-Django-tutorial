from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('triangle', views.triangle, name='triangle'),
    path('person/', views.create_person, name='create_person'),
    path('person/<int:id>', views.edit_person, name='edit_person'),
]
