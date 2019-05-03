from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from main.forms import SignupForm
from main.models import Downtown


@method_decorator(login_required, 'post')
class FollowView(View):
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username',  '')
        following = get_object_or_404(get_user_model(), username=username)
        request.user.following.add(following)
        return HttpResponse('Success')


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


class ProfileView(TemplateView):
    template_name = 'main/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        uname = kwargs['username']
        prof_user = get_user_model().objects.filter(username=uname).first()

        follow_state = 0
        user = self.request.user

        if user.is_authenticated:
            if user.following.filter(id=prof_user.id).exists():
                follow_state = 1
            else:
                follow_state = 2

        context['follow_state'] = follow_state
        context['profile_user'] = prof_user

        return context
