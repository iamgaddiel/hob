from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.urls.conf import include

from .views import (
    Index,
    Login,
    AdminDashboard,
    CreatePlayer,
    ListPlayers,
    GetPlayer,
    EventsList,
    EventDetail,
    EventsCreaton,
    AdminListEvents,
    AdminGetEvent,
    DownloadPublicityContract,
    DownloadBookingFormContract,
)

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('download/contract/', DownloadPublicityContract.as_view(), name="download_publicity_contract"),
    path('download/booking/form/', DownloadBookingFormContract.as_view(), name="download_booking_form"),
    # ====================== [Events[ ==================================
    path('events/', EventsList.as_view(), name="events_list"),
    path('events/<int:pk>/', EventDetail.as_view(), name="events_detail"),
    path('root/admin/events/form/crate/', EventsCreaton.as_view(), name="admin_create_event"),
    path('root/admin/events/get/<int:pk>/', AdminGetEvent.as_view(), name="admin_get_event"),
    path('root/admin/events/list/', AdminListEvents.as_view(), name="admin_events_list"),
    # ====================== [Admin[ ==================================
    path('login/', Login.as_view(), name="login"),
    path('root/admin/dashboard/', AdminDashboard.as_view(), name="admin_dashboard"),
    path('root/create/player/', CreatePlayer.as_view(), name="admin_create_player"),
    path('root/list/player/', ListPlayers.as_view(), name="admin_list_player"),
    path('root/get/player/<pk>/', GetPlayer.as_view(), name="admin_get_player"),
    path('services/', include('services.urls')),
]
