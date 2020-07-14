from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.db import models
from datetime import datetime
from django.urls import reverse


class EmailMailing(models.Model):
    """Email Рассылка"""
    email = models.EmailField("Email", unique=True)
    date = models.DateField("Дата отправки", null=True)

    def save(self, *args, **kwargs):
        self.date = datetime.now()
        super(EmailMailing, self).save(*args, **kwargs)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Запись Email"
        verbose_name_plural = "Email Рассылка"


class CallingMailing(models.Model):
    """Запись для консультации по телефону"""
    phoneNumber = models.CharField("Номер телефона", max_length=25, unique=True)
    date = models.DateField("Дата отправки", null=True)
    name = models.CharField("ФИО", max_length=220, default='Иван Иванов Иванович')

    def save(self, *args, **kwargs):
        self.date = datetime.now()
        super(CallingMailing, self).save(*args, **kwargs)

    def __str__(self):
        return self.phoneNumber

    class Meta:
        verbose_name = "Запись телефона"
        verbose_name_plural = "Список записей на консультацию по телефону"


class Employee(models.Model):
    """Сотрудник"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField("Должность", max_length=160)
    phone = models.CharField("Номер телефона", max_length=25)
    schedule = models.TextField("Время работы", max_length=160)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"


class Article(models.Model):
    """Статья"""
    title = models.CharField("Заголовок", max_length=150)
    content = RichTextField(blank=True, default='')
    url = models.SlugField(max_length=160, unique=True, null=True)
    author = models.ForeignKey(Employee, verbose_name="Автор", on_delete=models.SET_NULL, null=True)
    image = models.ImageField("Изображение", upload_to="articles/", null=True)
    viewsCount = models.IntegerField("Количество просмотров", null=True)
    likesCount = models.IntegerField("Количество лайков", null=True)
    shortDescription = models.TextField("Краткое описание", max_length=455, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class Views(models.Model):
    """Просмотры"""
    article = models.ForeignKey(Article, verbose_name="Статья", on_delete=models.CASCADE)

    def __str__(self):
        return f"Просмотр {self.article}"

    class Meta:
        verbose_name = "Просмотр"
        verbose_name_plural = "Просмотры"


class Likes(models.Model):
    """Лайк"""
    article = models.ForeignKey(Article, verbose_name="Статья", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="Юзер", on_delete=models.CASCADE)

    def __str__(self):
        return f"Лайк {self.user} - {self.article}"

    class Meta:
        verbose_name = "Лайк"
        verbose_name_plural = "Лайки"


class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField("Email")
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    article = models.ForeignKey(Article, verbose_name="Статья", on_delete=models.CASCADE, )

    def __str__(self):
        return f"{self.name} - {self.article}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class ReviewAnswer(models.Model):
    """Ответ на отзыв"""
    review = models.ForeignKey(Reviews, verbose_name="Отзыв", on_delete=models.CASCADE, )
    email = models.EmailField("Email")
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)

    def __str__(self):
        return f"{self.name} - {self.review}"

    class Meta:
        verbose_name = "Ответ на отзыв"
        verbose_name_plural = "Ответы на отзывы"


class InsurancePrograms(models.Model):
    """Программы страхования"""
    title = models.CharField("Заголовок", max_length=150)
    content = RichTextField(blank=True, default='')
    url = models.SlugField(max_length=160, unique=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Программа страхования"
        verbose_name_plural = "Программы страхования"
