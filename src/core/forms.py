from typing import Any
from django import forms
from django.db.models import fields
from django.forms import models

from core.models import Player


class PlayerCreationForm(forms.ModelForm):
    class Meta:
        models = Player
        fields = [
            'username',
            'first_name',
            'last_name',
            'age',
            'height',
            'weight',
            'nationality',
            'player_position',
            'preferred_foot',
            'abilities',
            'previous_club',
            'previous_club_start',
            'previous_club_finish',
            'current_club',
            'current_club_start_date',
            'hobbies',
            'awards',
            'educational_qualification',
            'referees',
            'video_clips_link'
        ]
