from typing import Any
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import fields
from django.forms import models, widgets
from core.models import Events, Player



class EventCreationForm(forms.ModelForm):
    class Meta:
        model = Events
        exclude = ['timestamp']
        widgets = {
            'title' : widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title'
            }),
            'poster' : widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title',
                'type': 'file'
            }),
            'kickoff_date' : widgets.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title',
                'type': 'date'
            }),
            'detail' : widgets.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Title',
                'rows': '25',
                'style': 'height: 200px;'
            }),
        }


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = [
            'first_name',
            'last_name',
            'age',
            'profile_image',
            'height',
            'weight',
            'nationality',
            'player_position',
            'preferred_foot',
            'previous_club',
            'previous_club_start',
            'previous_club_finish',
            'current_club',
            'current_club_start_date',
            'hobbies',
            'awards',
            'educational_qualification',
            'referees',
            'video_clip_link'
        ]
        widgets = {
            'previous_club_start': widgets.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'previous_club_finish': widgets.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'current_club_start_date': widgets.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'video_clip_link': widgets.URLInput(attrs={
                'class': 'form-control',
                # 'type': 'date'
            })
        }

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['age'].widget.attrs.update({
            'placeholder': 'age',
            'class': "form-control"
        })
        self.fields['first_name'].widget.attrs.update({
            'placeholder': 'fullname',
            'class': "form-control"
        })
        self.fields['last_name'].widget.attrs.update({
            'placeholder': 'fullname',
            'class': "form-control"
        })
        self.fields['profile_image'].widget.attrs.update({
            'placeholder': 'profile_image',
            'class': "form-control"
        })
        self.fields['height'].widget.attrs.update({
            'placeholder': 'height',
            'class': "form-control"
        })
        self.fields['weight'].widget.attrs.update({
            'placeholder': 'weight',
            'class': "form-control"
        })
        self.fields['nationality'].widget.attrs.update({
            'placeholder': 'nationality',
            'class': "form-control"
        })
        self.fields['player_position'].widget.attrs.update({
            'placeholder': 'Player Position',
            'class': "form-control"
        })
        self.fields['preferred_foot'].widget.attrs.update({
            'placeholder': 'Preferred Foot',
            'class': "form-control"
        })
        self.fields['previous_club'].widget.attrs.update({
            'placeholder': 'Previous Club',
            'class': "form-control"
        })
        self.fields['previous_club_finish'].widget.attrs.update({
            'placeholder': 'Previous Club Finish',
            'class': "form-control",
            'type': 'date'
        })
        self.fields['current_club'].widget.attrs.update({
            'placeholder': 'Current Club',
            'class': "form-control",
        })
        self.fields['hobbies'].widget.attrs.update({
            'placeholder': 'hobbies',
            'class': "form-control"
        })
        self.fields['awards'].widget.attrs.update({
            'placeholder': 'awards',
            'class': "form-control"
        })
        self.fields['educational_qualification'].widget.attrs.update({
            'placeholder': 'Educational Qualification',
            'class': "form-control"
        })
        self.fields['referees'].widget.attrs.update({
            'placeholder': 'referees',
            'class': "form-control"
        })


class LoginForm(AuthenticationForm):
    def __init__(self, request, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Username',
            'class': "form-control"
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Password',
            'class': "form-control"
        })
