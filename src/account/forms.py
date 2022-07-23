from .models import Account
from django.forms import ModelForm


class ProfileForm(ModelForm):

    class Meta:
        model = Account
        fields = '__all__'
        exclude = ['password', 'is_admin', 'is_active','is_staff', 'is_superuser','hide_email']
