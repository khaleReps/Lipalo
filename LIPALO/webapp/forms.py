from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'first_name',
            'last_name',
            'email',
            'contact_number',
            'access_level',
            'role_based_permissions',
            'password_management',
            'two_factor_authentication',
            'security_questions',
            'email_notifications',
            'mobile_app_notifications',
            'time_zone',
            'language_preference',
        ]
