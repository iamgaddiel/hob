import os
from random import randrange, seed
from datetime import datetime
from typing import Any, Dict, Optional
from django.db.models import query
from django.http import request
from django.http.response import HttpResponse, FileResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, View, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


from core.forms import EventCreationForm, LoginForm, PlayerCreationForm
from core.models import Player, Events
from services.models import MentorshipPayment, PlayerMentorship


class Index(TemplateView):
    template_name = 'core/index.html'

class Login(LoginView):
    template_name = 'core/login.html'
    form_class = LoginForm


class Dispatcher(View):
    def get(self, request, *args, **kwargs):
        user = request.user

        if user.is_superuser and user.is_staff:
            return redirect('admin_dashboard')
        elif user.is_active:
            return redirect("player_dashboard", player=user.player.id)
        return redirect('index')

class DownloadPublicityContract(View):
    def get(self, request, *args, **kwargs):
        CONTRACT_PATH = os.path.join(settings.MEDIA_ROOT, 'HOBS Clients Agreement For Clubs, Academies, Agencies.pdf')
        filename = "HOB3_Publicity_Contract.pdf"
        content_type = "application/pdf"
        return FileResponse(open(CONTRACT_PATH, 'rb'), filename=filename, content_type=content_type, as_attachment=True)

class DownloadBookingFormContract(View):
    def get(self, request, *args, **kwargs):
        CONTRACT_PATH = os.path.join(settings.MEDIA_ROOT, 'Speakers Booking Form.pdf')
        filename = "HSpeakers_Booking_Form.pdf"
        content_type = "application/pdf"
        return FileResponse(open(CONTRACT_PATH, 'rb'), filename=filename, content_type=content_type, as_attachment=True)

class PlayerList(ListView):
    template_name = "core/players.html"
    model = Player

class PlayerDetail(DetailView):
    template_name = "core/player_details.html"
    model = Player


class PlayerDashboard(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = "core/player_dashboard.html"
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        queryset = Player.objects.get(id=self.kwargs.get('player'))
        if self.request.user == queryset.user:
            context["object"] = queryset
        return context

    def test_func(self) -> Optional[bool]:
        if self.request.user == Player.objects.get(id=self.kwargs.get("player")).user:
            return True
        return False

# =======================================[ Admmin ] ===================================

class AdminDashboard(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = "core/admin_dashboard.html"

    def test_func(self) -> Optional[bool]:
        if self.request.user.is_superuser:
            return True
        return super().test_func()


# ===================== [ Admmin Player ]=======================
class CreatePlayer(LoginRequiredMixin, CreateView):
    template_name = 'core/forms.html'
    queryset = Player.objects.all()
    success_url = reverse_lazy('admin_list_player')
    form_class = PlayerCreationForm

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form_title'] = "Add Player"
        return context

    def form_valid(self, form) -> HttpResponse:
        letters = "a#$w\cde546fgij@&*klmo^pqt7uyz12h3n8brs90!()xv"
        password = ""
        seed = datetime.now()
        count = 0
        while count < 15:
            password += letters[randrange(0, len(letters))]
            count += 1

        user = User.objects.create(
            username="{0}_{1}_{2}".format(
                form.instance.first_name,
                form.instance.last_name,
                password
            ),
            password=make_password(password=password),
            first_name = form.instance.first_name,
            last_name = form.instance.last_name
        )
        form.instance.user = user
        form.save()
        return super().form_valid(form)


class ListPlayers(LoginRequiredMixin, ListView):
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

class SearchPlayers(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
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


# ============================== [ Mentorship ] ========================================
class ListMentorships(ListView):
    template_name = "core/list.html"
    model = PlayerMentorship

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["list_type"] = "mentorship"
        context['dashboard_title'] = 'Mentorships'
        return context

class MentorshipDetails(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = PlayerMentorship
    template_name = "core/mentorship_detail.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        mentorship_detail = self.get_object()
        context = super().get_context_data(**kwargs)
        context["payment"] =  MentorshipPayment.objects.get(player=mentorship_detail)
        context['dashboard_title'] = f"{mentorship_detail.first_name} {mentorship_detail.last_name}"
        return context

    def test_func(self) -> Optional[bool]:
        if self.request.user.is_superuser:
            return True
        return False
