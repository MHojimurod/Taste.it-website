from django import forms
from sqlparse import format

from .models import Booking,User, Subscribe, Commentary



class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class EmailForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = '__all__'