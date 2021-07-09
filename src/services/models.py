from django.db import models
from django.utils import timezone


class AcademyPulicity(models.Model):
    name = models.CharField(max_length=100, unique=True)
    profile_image = models.ImageField(default="academy.png", upload_to="academy_profile_image%Y%m%d")
    video_link = models.CharField(max_length=50)
    facility_image_1 = models.ImageField(default="facility.png", upload_to="academy_facilities%Y%m%d", blank=True)
    facility_image_2 = models.ImageField(default="facility.png", upload_to="academy_facilities%Y%m%d", blank=True)
    facility_image_3 = models.ImageField(default="facility.png", upload_to="academy_facilities%Y%m%d", blank=True)
    facility_image_4 = models.ImageField(default="facility.png", upload_to="academy_facilities%Y%m%d", blank=True)
    facility_image_5 = models.ImageField(default="facility.png", upload_to="academy_facilities%Y%m%d", blank=True)
    tournaments = models.TextField(blank=True, help_text="tournaments attended by this academy")
    awards = models.TextField(help_text="Enter each award on a new line")
    benefited_players = models.TextField(blank=True, help_text="players who got contracts from this academy")
    video_link_for_players = models.CharField(max_length=200, unique=True)
    timestamp = models.DateTimeField(auto_now=timezone.now)

    def __str__(self) -> str:
        return "{0}".format(self.name)

class PlayerPublicity(models.Model):
    pass

class BenefitedPlayers(models.Model):
    pass

    def __str__(self) -> str:
        return super().__str__()

class PlayerMentorship(models.Model):
    DURATION = [
        ('3 months', '3-months'),
        ('6 months', '6-months'),
        ('1 year', '1-year'),
    ]

    POSITION = [
        ('GK', 'GK'),
        ('CB', 'CB'),
        ('MF', 'MF'),
        ('ST', 'ST'),
    ]

    FOOTBALL_LEVEL = [
        ('Amateur', 'Amateur'),
        ('Semi Pro', 'Semi Pro'),
        ('Professional', 'Professional'),
    ]

    PUBLICITY_CATEGORY = [
        ('player', 'player'),
        ('academy', 'academy')
    ]

    duration = models.CharField(max_length=10, choices=DURATION)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    position_of_play = models.CharField(max_length=2, choices=POSITION)
    footbal_level = models.CharField(max_length=12, choices=FOOTBALL_LEVEL)
    publicity_category = models.CharField(max_length=10, choices=PUBLICITY_CATEGORY)

    def __str__(self) -> str:
        return super().__str__()

