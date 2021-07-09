from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.urls.conf import include

from .views import (
    Index,
    Login,
    AdminDashboard,
    CreatePlayer,
    ListPlayers,
    GetPlayer
)

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('login/', Login.as_view(), name="login"),
    path('root/admin/dashboard/', AdminDashboard.as_view(), name="admin_dashboard"),
    path('root/create/player/', CreatePlayer.as_view(), name="admin_create_player"),
    path('root/list/player/', ListPlayers.as_view(), name="admin_list_player"),
    path('root/get/player/<pk>/', GetPlayer.as_view(), name="admin_get_player"),
    path('services/', include('services.urls')),
]
