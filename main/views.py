from django.views.generic import TemplateView

from main.models import Downtown


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['downtowns'] = Downtown.objects.all()
        return context
