from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Reviews, ReviewAnswer, EmailMailing, CallingMailing, Likes


class ReviewForm(forms.ModelForm):
    """Форма отзыва"""

    class Meta:
        model = Reviews
        fields = ("name", "email", "text",)


class LikeForm(forms.ModelForm):
    """Форма отправки Like"""

    class Meta:
        model = Likes
        fields = ("article", "user")


class EmailForm(forms.ModelForm):
    """Форма emaila"""

    class Meta:
        model = EmailMailing
        fields = ("email",)


class CallsForm(forms.ModelForm):
    """Форма консультаций"""

    class Meta:
        model = CallingMailing
        fields = ("phoneNumber", "name")


class ReviewAnswerForm(forms.ModelForm):
    """Форма ответа отзыва"""

    class Meta:
        model = ReviewAnswer
        fields = ("name", "email", "text",)


class RegistrationForm(UserCreationForm):
    """Форма регистрации пользвателя"""
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
