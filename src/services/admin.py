from django.contrib import admin
from .models import AcademyPulicity, PublicityPayment, PlayerMentorship, MentorshipPayment


admin.site.register(AcademyPulicity)
admin.site.register(PublicityPayment)
admin.site.register(PlayerMentorship)
admin.site.register(MentorshipPayment)

