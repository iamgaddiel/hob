from django.contrib import admin

from .models import Player, Events

# admin.site.register(CustomUser)
admin.site.register(Player)
admin.site.register(Events)
