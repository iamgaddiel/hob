from django.urls import path
from .views import Mentorship, Publicity, ConfirmPayment, PaymentCallback


urlpatterns = [
    path('mentorship/<str:package>/', Mentorship.as_view(), name='mentorship'),
    path('publicity/academy/<str:package>/<int:price>/', Publicity.as_view(), name='academy_publicity'),
    path('confirm/academy/<str:package>/', ConfirmPayment.as_view(), name='confirm_payment'),
    path('confirm/payment/<str:txref>/', PaymentCallback.as_view(), name='payment_response'),
]