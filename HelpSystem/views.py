from django.shortcuts import render, redirect
from .models import Article, Views, Likes, ReviewAnswer, Reviews
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .forms import ReviewForm, EmailForm, ReviewAnswerForm, CallsForm
import datetime


class MainView(View):
    """Главная страница"""

    def get(self, request):
        quantity = 2
        articles = Article.objects.all()
        articles = articles[len(articles) - quantity::]
        for i in range(quantity):
            articles[i].viewsCount = len(Views.objects.filter(article_id=articles[i].id))
            articles[i].likesCount = len(Likes.objects.filter(article_id=articles[i].id))
        template_name = "HelpSystem/index.html"
        return render(request, template_name, {"latest_articles_list": articles})


class ArticlesList(View):
    """Список статей"""

    def get(self, request):
        articles = Article.objects.all()
        for i in range(len(articles)):
            articles[i].viewsCount = len(Views.objects.filter(article_id=articles[i].id))
            articles[i].likesCount = len(Likes.objects.filter(article_id=articles[i].id))
        template_name = "HelpSystem/articlesList.html"
        return render(request, template_name, {"articles_list": articles})


class ArticleDetail(View):
    """Просмотр статьи"""
    def get(self, request, slug):
        article = Article.objects.get(url=slug)
        Views.objects.create(article=article)
        article.viewsCount = len(Views.objects.filter(article_id=article.id))
        article.likesCount = len(Likes.objects.filter(article_id=article.id))
        template_name = "HelpSystem/article_detail.html"
        return render(request, template_name, {"article": article})


class AddReview(View):
    """Отзыв"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        if request.POST.get("parent", None):
            form = ReviewAnswerForm(request.POST)
            ParentID = int(request.POST.get("parent"))
            review = Reviews.objects.get(id=ParentID)
            article = Article.objects.get(id=pk)
            if form.is_valid():
                form = form.save(commit=False)
                form.review = review
                form.save()
            return redirect("/" + article.url)
        article = Article.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.article = article
            form.save()
        return redirect("/"+article.url)


class AddEmail(View):
    """Подписка на рассылку"""
    def post(self, request):
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")


class AddNumber(View):
    """Подписка на рассылку"""
    def post(self, request):
        form = CallsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")


class AddAnswerReview(View):
    """Ответ на отзыв"""
    def post(self, request, pk):
        form = ReviewAnswerForm(request.POST)
        review = Reviews.objects.get(id=pk)
        article = Article.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.review = review
            form.save()
        return redirect("/"+article.url)


class AboutDetail(ListView):
    model = Article
    template_name = "HelpSystem/about.html"
