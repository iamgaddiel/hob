import os
from random import randrange
from typing import Any, Dict
from django import urls
from django.forms.models import ModelForm
from django.http.response import HttpResponse, FileResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, View, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.conf import settings


from core.forms import EventCreationForm, LoginForm, PlayerCreationForm
from core.models import CustomUser, Player, Events


class Index(TemplateView):
    template_name = 'core/index.html'


class Login(LoginView):
    template_name = 'core/login.html'
    form_class = LoginForm


class Dispatcher(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return redirect('admin_dashboard')
        # todo: redirect to player dashboard by default
        return redirect('index')

class DownloadPublicityContract(View):
    def get(self, request, *args, **kwargs):
        CONTRACT_PATH = os.path.join(settings.MEDIA_ROOT, 'HOBS Clients Agreement For Clubs, Academies, Agencies.pdf')
        filename = "HOB3_Publicity_Contract.pdf"
        content_type = "application/pdf"
        return FileResponse(open(CONTRACT_PATH, 'rb'), filename=filename, content_type=content_type, as_attachment=True)

class DownloadBookingFormContract(View):
    def get(self, request, *args, **kwargs):
        CONTRACT_PATH = os.path.join(settings.MEDIA_ROOT, 'Speakers Booking Form.doc')
        filename = "HSpeakers_Booking_Form.doc.pdf"
        content_type = "application/pdf"
        return FileResponse(open(CONTRACT_PATH, 'rb'), filename=filename, content_type=content_type, as_attachment=True)

# =======================================[ Admmin ] ===================================

class AdminDashboard(TemplateView):
    template_name = "core/admin_dashboard.html"


# ===================== [ Admmin Player ]=======================
class CreatePlayer(CreateView):
    template_name = 'core/forms.html'
    queryset = Player.objects.all()
    success_url = reverse_lazy('admin_list_player')
    form_class = PlayerCreationForm

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form_title'] = "Add Player"
        return context

    def form_valid(self, form) -> HttpResponse:
        letters = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"
        password = ""
        count = 0
        while count < 15:
            password += letters[randrange(0, len(letters))]
            count += 1

        user = CustomUser.objects.create(
            username=form.instance.fullname,
            password=password
        )
        form.instance.user = user
        form.save()
        return super().form_valid(form)


class ListPlayers(ListView):
    queryset = Player.objects.all()
    template_name = 'core/list.html'
    ordering = ['-id']

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['dashboard_title'] = 'Players'
        context['list_type'] = "player"
        return context

class GetPlayer(DetailView):
    queryset = Player.objects.all()
    template_name = 'core/get_player.html'
    context_object_name = 'player'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['dashboard_title'] = 'Player Profile'
        return context

class SearchPlayers(View):
    def get(self, request, *args, **kwargs):
        pass

class PlayerDashboard():
    pass


class Payment(TemplateView):
    pass


# ===================== [ Admmin Events ]=======================
class AdminListEvents(ListView):
    model = Events
    template_name = "core/list.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['list_type'] = "events"
        context['dashboard_title'] = 'Events'
        return context

class EventsCreaton(CreateView):
    success_url = reverse_lazy('admin_events_list')
    template_name = 'core/forms.html'
    form_class = EventCreationForm

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Events'
        return context    

class AdminGetEvent(DetailView):
    model = Events
    template_name = "core/event_detail.html"
    context_object_name = "event"


# ============================== [ Events ] ========================================

    
class EventsList(ListView):
    model = Events
    template_name = "core/events.html"

class EventDetail(DetailView):
    template_name = 'services/event_detail.html'
    model = Events
    context_object_name = "event"

