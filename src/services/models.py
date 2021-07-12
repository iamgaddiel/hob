from django.db import models
from django.utils import timezone


class AcademyPulicity(models.Model):

    PUBLICITY_CATEGORY = [
        ('player', 'player'),
        ('academy', 'academy')
    ]

    DURATION = [
        ('3 months', '3-months'),
        ('6 months', '6-months'),
        ('1 year', '1-year'),
    ]

    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True, blank=True)
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
    duration = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now=timezone.now)

    def __str__(self) -> str:
        return "{0}".format(self.name)

class PublicityPayment(models.Model):

    DURATION = [
        ('3 months', '3-months'),
        ('6 months', '6-months'),
        ('1 year', '1-year'),
    ]

    academy = models.ForeignKey(AcademyPulicity, on_delete=models.CASCADE)
    amount = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    ref = models.CharField(max_length=20)
    transaction = models.CharField(max_length=20, unique=True)
    txref = models.CharField(max_length=20, unique=True, blank=True)
    status = models.CharField(max_length=10)
    duration = duration = models.CharField(max_length=10, choices=DURATION)
    timestamp = models.DateTimeField(auto_now=timezone.now)

    def __str__(self) -> str:
        return "{0} | package: {1}| status: {2} | time: {3}".format(
            self.academy,
            self.package,
            self.status,
            self.timestamp
        )

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

    duration = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    position_of_play = models.CharField(max_length=2, choices=POSITION)
    footbal_level = models.CharField(max_length=12, choices=FOOTBALL_LEVEL)

    def __str__(self) -> str:
        return super().__str__()

