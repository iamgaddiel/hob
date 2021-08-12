from django.db import models
from django.db.models.fields import CharField
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

    name = models.CharField(max_length=100,)
    email = models.EmailField(default="")
    profile_image = models.ImageField(default="academy.png", upload_to="academy_profile_image%Y%m%d")
    video_link = models.CharField(max_length=50, default="")
    facility_image_1 = models.ImageField(default="facility.png", upload_to="academy_facilities%Y%m%d")
    facility_image_2 = models.ImageField(default="facility.png", upload_to="academy_facilities%Y%m%d")
    facility_image_3 = models.ImageField(default="facility.png", upload_to="academy_facilities%Y%m%d")
    facility_image_4 = models.ImageField(default="facility.png", upload_to="academy_facilities%Y%m%d")
    facility_image_5 = models.ImageField(default="facility.png", upload_to="academy_facilities%Y%m%d")
    tournaments = models.TextField(blank=True, help_text="tournaments attended by this academy", default="")
    awards = models.TextField(help_text="Enter each award on a new line", default="")
    benefited_players = models.TextField(blank=True, help_text="players who got contracts from this academy", default="")
    video_link_for_players = models.CharField(max_length=200, default="")
    duration = models.CharField(max_length=10, default="")
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
        return "{0} | status: {1} | time: {2}".format(
            self.academy,
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
    football_level = models.CharField(max_length=12, choices=FOOTBALL_LEVEL)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

class MentorshipPayment(models.Model):

    DURATION = [
        ('3 months', '3-months'),
        ('6 months', '6-months'),
        ('1 year', '1-year'),
    ]

    player = models.ForeignKey(PlayerMentorship, on_delete=models.CASCADE)
    unique_code = models.CharField(max_length=20, unique=True, editable=False)
    amount = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    ref = models.CharField(max_length=20)
    transaction = models.CharField(max_length=20, unique=True)
    txref = models.CharField(max_length=20, unique=True, blank=True)
    status = models.CharField(max_length=10)
    duration = duration = models.CharField(max_length=10, choices=DURATION)
    timestamp = models.DateTimeField(auto_now=timezone.now)

    def __str__(self) -> str:
        return "{0} | status: {1} | time: {2}".format(
            self.player.first_name,
            self.status,
            self.timestamp
        )


class EducationPayments(models.Model):
    phone_number = CharField(max_length=15, unique=True)
    registration_date = models.DateField(auto_now=True)
    expiration_date = models.DateField(auto_now=True, blank=True)

    def __str__(self) -> str:
        return super().__str__()

    #TODO : create a method that checks for expiration date
    # def check_expiration(self):
    #     return False