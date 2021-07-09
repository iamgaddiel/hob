from django import forms
from django.db.models import fields
from django.forms import widgets

from .models import PlayerMentorship, AcademyPulicity


class MentorshipForm(forms.ModelForm):
    class Meta:
        model = PlayerMentorship
        exclude = ['duration']
        widgets = {
            'first_name': widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name '
            }),
            'middle_name': widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Middle Name '
            }),
            'last_name': widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name'
            }),
            'email': widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'position_of_play': widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Position of Play'
            }),
            'footbal_level': widgets.Select(attrs={
                'class': 'form-control',
                'type': 'select'
            }),
        }


class AcademyPulicityForm(forms.ModelForm):
    class Meta:
        model = AcademyPulicity
        exclude = ['timestamp', 'publicity_academy']
        widgets = {
            'name': widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Full Name '
            }),
            'profile_image': widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'profile_image ',
                'type': 'file'
            }),
            'video_link': widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'video_link'
            }),
            'facility_image_1': widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'facility_image_1',
                'type': 'file'
            }),
            'facility_image_2': widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'facility_image_2',
                'type': 'file'
            }),
            'facility_image_3': widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'facility_image_3',
                'type': 'file'
            }),
            'facility_image_4': widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'facility_image_4',
                'type': 'file'
            }),
            'facility_image_5': widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'facility_image_5',
                'type': 'file'
            }),
            'tournaments': widgets.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'tournaments',
                'rows': '25',
                'style': "height:170px;"
            }),
            'awards': widgets.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'awards',
                'rows': '25',
                'style': "height:170px;"
            }),
            'benefited_players': widgets.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'benefited_players',
                'rows': '25',
                'style': "height:170px;"
            }),
            'video_link_for_players': widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'video_link_for_players'
            }),

        } 

