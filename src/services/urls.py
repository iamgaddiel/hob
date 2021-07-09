from django.urls import path
from .views import Mentorship, Publicity


urlpatterns = [
    path('mentorship/<str:package>/', Mentorship.as_view(), name='mentorship'),
    path('academy/publicity/<str:publicity_category>/<str:package>/', Publicity.as_view(), name='academy_publicity'),
]