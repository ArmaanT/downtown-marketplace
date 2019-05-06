from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, TemplateView
from django.views.generic.edit import FormView

from main.forms import SignupForm
from main.models import Downtown, Ticket


@method_decorator(login_required, 'post')
class FollowView(View):
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username',  '')
        following = get_object_or_404(get_user_model(), username=username)
        request.user.following.add(following)
        return HttpResponse('Success')


@method_decorator(login_required, 'post')
class CloseTicketView(View):
    def post(self, request, *args, **kwargs):
        ticket_id = request.POST.get('ticket',  '')
        ticket = get_object_or_404(Ticket, id=ticket_id)
        if ticket.seller == self.request.user:
            print("found")
            ticket.sold = not ticket.sold
        ticket.save()
        return HttpResponse('Success')


@method_decorator(login_required, 'post')
class AttendView(View):
    def post(self, request, *args, **kwargs):
        downtown_id = request.POST.get('downtown',  '')
        downtown = get_object_or_404(Downtown, id=downtown_id)
        user = self.request.user
        user.attending.add(downtown)
        user.save()
        return HttpResponse('Success')


@method_decorator(login_required, 'post')
class UnattendView(View):
    def post(self, request, *args, **kwargs):
        downtown_id = request.POST.get('downtown',  '')
        downtown = get_object_or_404(Downtown, id=downtown_id)
        user = self.request.user
        user.attending.remove(downtown)
        user.save()
        return HttpResponse('Success')


class HomeView(TemplateView):
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('query', '')
        downtowns = Downtown.objects.filter(name__icontains=query)
        users = get_user_model().objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(username__icontains=query)
        )
        if self.request.user.is_authenticated:
            following = self.request.user.following
            downtown_info = map(
                lambda downtown: (downtown, len(following.filter(attending__id__exact=downtown.id))),
                downtowns
            )
            user_info = map(
                lambda user: (user, len(following.all() & user.following.all())),
                users
            )
            downtown_info = sorted(downtown_info, key=lambda d: d[1], reverse=True)
            user_info = sorted(user_info, key=lambda u: u[1], reverse=True)
            context['user_info'] = user_info
            context['downtown_info'] = downtown_info
        else:
            context['downtown_info'] = map(
                lambda downtown: (downtown, 0),
                downtowns)
            context['user_info'] = map(
                lambda user: (user, 0),
                users
            )

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

        attending_state = 0
        user = self.request.user
        if user.is_authenticated:
            if user.attending.filter(id=downtown.id).exists():
                attending_state = 1
            else:
                attending_state = 2

        context['attending_state'] = attending_state
        context['downtown'] = downtown
        context['tickets'] = downtown.ticket_set.filter(sold=False)
        return context


class SellView(CreateView):
    template_name = 'main/sell.html'
    model = Ticket
    fields = ['price', 'downtown', 'bio']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.seller = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProfileView(TemplateView):
    template_name = 'main/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        uname = kwargs['username']
        prof_user = get_object_or_404(get_user_model(), username=uname)

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


@method_decorator(login_required, 'post')
class UnfollowView(View):
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username',  '')
        following = get_object_or_404(get_user_model(), username=username)
        request.user.following.remove(following)
        return HttpResponse('Success')
