from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from main.forms import SignupForm
from main.models import Downtown, Ticket


class HomeView(TemplateView):
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        downtowns = Downtown.objects.all()
        if self.request.user.is_authenticated:
            following = self.request.user.following
            context['downtown_info'] = map(
                lambda downtown: (downtown, len(following.filter(attending__id__exact=downtown.id))),
                downtowns)
        else:
            context['downtown_info'] = map(
                lambda downtown: (downtown, 0),
                downtowns)

        return context

class SignupView(FormView):
    template_name = 'main/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class DowntownView(TemplateView):
    template_name = 'main/downtown.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        downtown = Downtown.objects.filter(id=kwargs['dtname']).first()
        context['downtown'] = downtown
        context['tickets'] = downtown.ticket_set.all()
        return context
