from django.shortcuts import render
from django.views.generic import TemplateView

from main.models import Downtown


class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        downtowns = Downtown.objects.all()
        return render(request, self.template_name, {'downtowns': downtowns})
