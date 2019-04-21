from django.shortcuts import render

from main.models import Downtown


def homepage(request):
    downtowns = Downtown.objects.all()
    return render(request, 'home.html', {'downtowns' : downtowns})
