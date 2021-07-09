from django.contrib import admin

from .models import Player, CustomUser

admin.site.register(CustomUser)
admin.site.register(Player)
