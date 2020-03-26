from django import forms
from .models import Reviews, ReviewAnswer, EmailMailing, CallingMailing


class ReviewForm(forms.ModelForm):
    """Форма отзыва"""
    class Meta:
        model = Reviews
        fields = ("name", "email", "text",)


class EmailForm(forms.ModelForm):
    """Форма emaila"""
    class Meta:
        model = EmailMailing
        fields = ("email",)


class CallsForm(forms.ModelForm):
    """Форма emaila"""
    class Meta:
        model = CallingMailing
        fields = ("phoneNumber",)


class ReviewAnswerForm(forms.ModelForm):
    """Форма ответа отзыва"""
    class Meta:
        model = ReviewAnswer
        fields = ("name", "email", "text",)