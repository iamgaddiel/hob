from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.utils import timezone
import uuid



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
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    profile_image = models.ImageField(upload_to="player_profile_image", default="player_profile.png")
    age = models.PositiveIntegerField(default=1)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    nationality = models.CharField(max_length=30, blank=True)
    player_position = models.CharField(max_length=40, blank=True)
    preferred_foot = models.CharField(max_length=12, choices=FOOTS, default=FOOTS[1], blank=True)
    previous_club = models.CharField(max_length=500, blank=True)
    previous_club_start = models.DateField(blank=True, null=True)
    previous_club_finish = models.DateField(blank=True, null=True)
    current_club = models.CharField(max_length=500, help_text="current club name", default='N/A', blank=True)
    current_club_start_date = models.DateField(blank=True, null=True)
    awards = models.TextField(help_text="Enter new award on a new line", blank=True)
    hobbies = models.CharField(max_length=600, help_text="seporate hobbies with a comma", blank=True)
    educational_qualification = models.CharField(max_length=30, choices=QUALIFICATIONS, blank=True)
    referees = models.TextField(help_text="format: name - phone, each referee should be on a new line", blank=True)
    video_clip_link = models.CharField(max_length=100, unique=True, blank=True)
    timestamp = models.DateTimeField(auto_now=timezone.now)

    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

class Events(models.Model):
    title = models.CharField(max_length=400, unique=True)
    poster = models.ImageField(upload_to="event_image", default="image_image.png")
    kickoff_date = models.DateField()
    detail = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=timezone.now)

    
    def ___str__(self):
        pass
