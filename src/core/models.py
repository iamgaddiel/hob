from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import uuid



class CustomUser(AbstractUser):
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4)

    def save(self, *args, **kwargs) -> None:
        self.username = "{0}_{1}".format(
            self.first_name,
            self.last_name,
        )
        return super().save(*args, **kwargs)

class Player(models.Model):
    FOOTS = [
        ('left_foot', 'Left Foot'),
        ('right_foot', 'Right Foot'),
    ]
    QUALIFICATIONS = [
        ('SSCE', 'SSCE'),
        ('Bsc', 'Bsc'),
        ('OND', 'OND'),
        ('HND', 'HND'),
        ('Phd', 'Phd'),
    ]
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    fullname = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to="player_profile_image", default="player_profile.png")
    age = models.PositiveIntegerField(default=1)
    height = models.FloatField(null=True)
    weight = models.FloatField(null=True)
    nationality = models.CharField(max_length=30)
    player_position = models.CharField(max_length=40)
    preferred_foot = models.CharField(max_length=12, choices=FOOTS, default=FOOTS[1])
    previous_club = models.CharField(max_length=500)
    previous_club_start = models.DateField(blank=True, null=True)
    previous_club_finish = models.DateField(blank=True, null=True)
    current_club = models.CharField(max_length=500, help_text="current club name", default='N/A')
    current_club_start_date = models.DateField(blank=True, null=True)
    awards = models.TextField(help_text="Enter new award on a new line")
    hobbies = models.CharField(max_length=600, help_text="seporate hobbies with a comma")
    educational_qualification = models.CharField(max_length=30, choices=QUALIFICATIONS)
    referees = models.TextField(help_text="format: name - phone, each referee should be on a new line")
    video_clip_link = models.CharField(max_length=100, unique=True)
    timestamp = models.DateTimeField(auto_now=timezone.now)

    
    def __str__(self) -> str:
        return r"{self.first_name} {self.last_name}"

