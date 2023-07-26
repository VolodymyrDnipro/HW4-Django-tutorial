from django.shortcuts import render
from .tasks import scrape_quotes


def index(request):
    scrape_quotes.delay()
    return render(request, 'quotes/index.html')
