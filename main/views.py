from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from main.forms import SignupForm
from main.models import Downtown


class HomeView(TemplateView):
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        downtowns = Downtown.objects.all()
        following = self.request.user.following
        context['downtown_info'] = map(
            lambda downtown: (downtown, len(following.filter(attending__id__exact=downtown.id))),
            downtowns)
        return context


class SignupView(FormView):
    template_name = 'main/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)