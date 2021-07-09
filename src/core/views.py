from typing import Any, Dict
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, View, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from core.forms import LoginForm, PlayerCreationForm
from core.models import Player


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


class AdminDashboard(LoginRequiredMixin, TemplateView):
    template_name = "core/admin_dashboard.html"


class CreatePlayer(CreateView):
    template_name = 'core/forms.html'
    queryset = Player.objects.all()
    success_url = reverse_lazy('admin_list_player')
    form_class = PlayerCreationForm

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form_title'] = "Add Player"
        return context


class ListPlayers(ListView):
    queryset = Player.objects.all()
    template_name = 'core/list.html'
    ordering = ['-id']

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['dashboard_title'] = 'Players'
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
