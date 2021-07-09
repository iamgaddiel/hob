from typing import Any, Dict
from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, View, FormView, TemplateView
from django.views.generic.edit import CreateView

from services.forms import MentorshipForm, AcademyPulicityForm
from services.models import PlayerMentorship




# Create your views here.
class Publicity(CreateView):
    form_class = AcademyPulicityForm
    template_name = "services/publicity.html"
    success_url = reverse_lazy("index") # TODO: redirect to payment page

    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['package'] = self.kwargs.get("package")
        context['publicity_category'] = self.kwargs.get("publicity_category")
        return context

    def form_valid(self, form) -> HttpResponse:
        form.instance.publicity_academy = self.request.POST.get('publicity_academy')
        form.instance.duration = self.request.POST.get('duration')
        return super().form_valid(form)

class DownloadPublicityContract():
    pass


class Mentorship(CreateView):
    template_name = "services/mentorship.html"
    form_class = MentorshipForm
    success_url = reverse_lazy('index') # TODO: redirect to payment page

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['package'] = self.kwargs.get('package')
        return context

def ConfirmPayment(View):
    def get(self, request, *args, **kwargs):
        pass
