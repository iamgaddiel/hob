from typing import Any, Dict
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render, resolve_url
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, FormView, TemplateView, View, CreateView
from django.conf import settings

from services.forms import MentorshipForm, AcademyPulicityForm
from services.models import AcademyPulicity, PlayerMentorship, PublicityPayment

import json


# Create your views here.
class Publicity(FormView):
    form_class = AcademyPulicityForm
    template_name = "services/publicity.html"
    # success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['package'] = self.kwargs.get("package")
        context['price'] = self.kwargs.get("price")
        return context

    def form_valid(self, form) -> HttpResponse:
        # store form detail to session
        form_data = self.request.POST

        self.request.session["ACADEMY_PUBLICITY_DETAILS"] = form_data
        self.request.session["PACKAGE_PRICE"] = form_data.get("price")
        self.request.session["PUBLICITY_NAME"] = form_data.get('name')
        self.request.session["PUBLICITY_PACKAGE"] = form_data.get('package')

        # print(self.kwargs.get('publicity_category'), self.kwargs.get("package"))
        return redirect("confirm_payment", package=self.kwargs.get("package"))
        # return super().form_valid(form)


class DownloadPublicityContract():
    pass


class Mentorship(CreateView):
    template_name = "services/mentorship.html"
    form_class = MentorshipForm
    success_url = reverse_lazy('index')  # TODO: redirect to payment page

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['package'] = self.kwargs.get('package')
        return context

class ConfirmPayment(View):
    def get(self, request, *args,**kwargs):
        template_name = "services/checkout.html"
        context = {
            "PACKAGE_PRICE": self.request.session.get("PACKAGE_PRICE"),
            "PUBLICITY_NAME": self.request.session.get('PUBLICITY_NAME'),
            "PUBLICITY_PACKAGE": self.request.session.get('PUBLICITY_PACKAGE'),
            "PAYSTACK_PUBLIC_KEY": settings.PAYSTACK_PUBLIC_KEY,
        }
        return render(request, template_name, context)

class PaymentCallback(View):
    def post(self, request, *args, **kwargs):
        payment_response = json.loads(request.body.decode('utf-8'))
        academy_data = request.session.get("ACADEMY_PUBLICITY_DETAILS")
        academy = AcademyPulicity(
            name = academy_data.get('name'),
            email = academy_data.get('email'),
            profile_image = academy_data.get('profile_image'),
            video_link = academy_data.get('video_link'),
            facility_image_1 = academy_data.get('facility_image_1'),
            facility_image_2 = academy_data.get('facility_image_2'),
            facility_image_3 = academy_data.get('facility_image_3'),
            facility_image_4 = academy_data.get('facility_image_4'),
            facility_image_5 = academy_data.get('facility_image_5'),
            tournaments = academy_data.get('tournaments'),
            benefited_players = academy_data.get('benefited_players'),
            video_link_for_players = academy_data.get('video_link_for_players'),
            duration = request.session.get("PUBLICITY_PACKAGE")
        )
        # academy.save()
        # publicity = PublicityPayment(**payment_response)
        # publicity.academy = academy
        # publicity.save()
        return JsonResponse({"data": "success"})

