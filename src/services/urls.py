from django.urls import path
from .views import (
    Mentorship, 
    Publicity, 
    ConfirmPublicityPayment, 
    # PublicityPaymentCallback,
    PaymentDone,
    MentorshipConfirmPayment,
)


urlpatterns = [
    path('mentorship/<str:duration>/', Mentorship.as_view(), name='mentorship'),
    path('confrim/mentorship/', MentorshipConfirmPayment.as_view(), name='mentorship_confirm'),
    path('publicity/academy/<str:package>/<int:price>/', Publicity.as_view(), name='academy_publicity'),
    path('confirm/academy/', ConfirmPublicityPayment.as_view(), name='confirm_payment'),
    # path('confirm/payment/', PublicityPaymentCallback.as_view(), name='publicity_payment_response'),
    path('payment/done/', PaymentDone.as_view(), name='payment_done'),
]