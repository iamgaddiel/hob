from typing import Any, Dict
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render, resolve_url
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, FormView, TemplateView, View, CreateView
from django.conf import settings
from django.db import IntegrityError
from core.utils import get_coupon_code

from services.forms import MentorshipForm, AcademyPulicityForm
from services.models import AcademyPulicity, PlayerMentorship, PublicityPayment, MentorshipPayment

import json




class DownloadPublicityContract():
    pass


class Mentorship(FormView):
    template_name = "services/mentorship.html"
    form_class = MentorshipForm

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['duration'] = self.kwargs.get('duration')
        return context
    
    def form_valid(self, form) -> HttpResponse:
        # store form detail to session
        form_data = self.request.POST

        self.request.session["FULL_DETAILS"] = form_data
        self.request.session["PRICE"] = form_data.get("price")
        self.request.session["NAME"] = f"{form_data.get('first_name')} {form_data.get('last_name')}"
        self.request.session["PACKAGE"] = form_data.get('duration')
        self.request.session["EMAIL"] = form_data.get('email')
        return redirect('mentorship_confirm')

class MentorshipConfirmPayment(View):
    def get(self, request, *args, **kwargs):
        template_name = "services/checkout.html"
        context = {
            "PRICE": self.request.session.get("PRICE"),
            "NAME": self.request.session.get('NAME'),
            "PACKAGE": self.request.session.get('PACKAGE'),
            "PAYSTACK_PUBLIC_KEY": settings.PAYSTACK_PUBLIC_KEY,
            "EMAIL": self.request.session.get('EMAIL'),
            "CALLBACK_ENDPOINT": resolve_url("mentorship_confirm"),
            "SUCCESS_URL": resolve_url("payment_done")
        }
        return render(request, template_name, context)

    def post(self, request, *args, **kwargs):
        payment_response = json.loads(request.body.decode('utf-8'))
        mentorship_data = request.session.get("FULL_DETAILS")
        player = PlayerMentorship.objects.create(
            duration = mentorship_data.get("duration"),
            first_name =  mentorship_data.get("first_name"),
            middle_name =  mentorship_data.get("middle_name"),
            last_name =  mentorship_data.get("last_name"),
            email =  mentorship_data.get("email"),
            position_of_play =  mentorship_data.get("position_of_play"),
            footbal_level = mentorship_data.get("footbal_level")
        )
        MentorshipPayment.objects.create(
            player=player,
            unique_code = get_coupon_code(20),
            amount=payment_response.get('amount'), 
            email=payment_response.get('email'),
            ref=payment_response.get('ref'),
            transaction=payment_response.get('transaction'),
            txref=payment_response.get('trxref'),
            status=payment_response.get('status'),
            duration=payment_response.get('duration')
        )
        return JsonResponse({"data": "success"})


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
        form_data_images = self.request.FILES

        academy = AcademyPulicity.objects.create(
            name = form_data.get('name'),
            profile_image = form_data.get('profile_image'),
            facility_image_1 = form_data_images.get('facility_image_1'),
            facility_image_2 = form_data_images.get('facility_image_2'),
            facility_image_3 = form_data_images.get('facility_image_3'),
            facility_image_4 = form_data_images.get('facility_image_4'),
            facility_image_5 = form_data_images.get('facility_image_5'),
        )
        self.request.session['OBJECT_ID'] = academy.pk
        self.request.session["FULL_DETAILS"] = form_data
        self.request.session["PRICE"] = form_data.get("price")
        self.request.session["NAME"] = form_data.get('name')
        self.request.session["PACKAGE"] = form_data.get('package')
        self.request.session["EMAIL"] = form_data.get('email')

        return redirect("confirm_payment")

class ConfirmPublicityPayment(View):
    def get(self, request, *args,**kwargs):
        template_name = "services/checkout.html"
        context = {
            "PRICE": self.request.session.get("PRICE"),
            "NAME": self.request.session.get('NAME'),
            "PACKAGE": self.request.session.get('PACKAGE'),
            "PAYSTACK_PUBLIC_KEY": settings.PAYSTACK_PUBLIC_KEY,
            "EMAIL": self.request.session.get('EMAIL'),
            "CALLBACK_ENDPOINT": resolve_url("confirm_payment"),
            "SUCCESS_URL": resolve_url("payment_done")
        }
        return render(request, template_name, context)
    
    def post(self, request, *args, **kwargs):
        payment_response = json.loads(request.body.decode('utf-8'))
        academy_data = request.session.get("FULL_DETAILS")

        academy = AcademyPulicity.objects.get(pk=request.session['OBJECT_ID'])
        academy.email = academy_data.get('email')
        academy.video_link = academy_data.get('video_link')
        academy.tournaments = academy_data.get('tournaments')
        academy.benefited_players = academy_data.get('benefited_players')
        academy.video_link_for_players = academy_data.get('video_link_for_players')
        academy.duration = request.session.get("PACKAGE")
        academy.save()

        PublicityPayment.objects.create(
            academy=academy,
            amount=payment_response.get('amount'), 
            email=payment_response.get('email'),
            ref=payment_response.get('ref'),
            transaction=payment_response.get('transaction'),
            txref=payment_response.get('trxref'),
            status=payment_response.get('status'),
            duration=payment_response.get('duration')
        )
        return JsonResponse({"data": "success"})

class PaymentDone(TemplateView):
    template_name = "services/payment_done.html"
