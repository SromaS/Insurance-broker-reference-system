from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.base import View
from django.views.generic.edit import FormView

from .forms import ReviewForm, EmailForm, ReviewAnswerForm, CallsForm, RegistrationForm, LikeForm
from .models import Article, Views, Likes, Reviews, InsurancePrograms


class MainView(View):
    """Главная страница"""

    def get(self, request):
        quantity = 2
        articles = Article.objects.all()
        articles = articles[len(articles) - quantity::]
        for i in range(quantity):
            articles[i].viewsCount = len(Views.objects.filter(article_id=articles[i].id))
            articles[i].likesCount = len(Likes.objects.filter(article_id=articles[i].id))
        template_name = "HelpSystem/main.html"
        return render(request, template_name, {"latest_articles_list": articles})


class ArticlesList(View):
    """Список статей"""

    def get(self, request):
        search_query = request.GET.get('search', '')
        if search_query:
            articles = Article.objects.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))
        else:
            articles = Article.objects.all()

        for i in range(len(articles)):
            articles[i].viewsCount = len(Views.objects.filter(article_id=articles[i].id))
            articles[i].likesCount = len(Likes.objects.filter(article_id=articles[i].id))
        template_name = "HelpSystem/articlesList.html"
        if search_query:
            return render(request, template_name, {"articles_list": articles, "search_contain": search_query})
        else:
            return render(request, template_name, {"articles_list": articles})


class ArticleDetail(View):
    """Просмотр статьи"""

    def get(self, request, slug):
        article = Article.objects.get(url=slug)
        Views.objects.create(article=article)
        ArticleLikesQuery = Likes.objects.filter(article_id=article.id)
        article.viewsCount = len(Views.objects.filter(article_id=article.id))
        article.likesCount = len(ArticleLikesQuery)
        template_name = "HelpSystem/article_detail.html"
        currentUser = request.user
        if currentUser.is_authenticated:
            if Likes.objects.filter(article_id=article.id, user_id=currentUser.id):
                liked = True
            else:
                liked = False
            return render(request, template_name, {"article": article, "liked": liked})
        else:
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
                form.article = article
                form.save()
            return redirect("/" + article.url)
        article = Article.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.article = article
            form.save()
        return redirect("/" + article.url)


class AddEmail(View):
    """Подписка на рассылку"""

    def post(self, request):
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")


class AddNumber(View):
    """Запись по телефону"""

    def post(self, request):
        form = CallsForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class AboutDetail(ListView):
    """Страница О нас"""
    model = Article
    template_name = "HelpSystem/about.html"


class ProgramDetail(View):
    """Страница программы страхования"""

    def get(self, request, slug):
        slug = slug.rpartition("/")[2]
        insuranceProgram = InsurancePrograms.objects.get(url=slug)
        template_name = "HelpSystem/insurance_programs.html"
        return render(request, template_name, {"insuranceProgram": insuranceProgram, })


class RegisterFormView(FormView):
    """Регистрация пользвателя"""
    form_class = RegistrationForm
    success_url = "../accounts/login/"
    template_name = "registration/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)


class AddLike(View):
    """Поставить Лайк"""

    def post(self, request, pk):
        form = LikeForm(request.POST)
        article = Article.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.article = article
            form.save()
        return redirect("/" + article.url)


class DelLike(View):
    """Удалить Лайк"""

    def post(self, request, pk):
        article = Article.objects.get(id=pk)
        currentUser = request.user
        Likes.objects.filter(article_id=article.id, user_id=currentUser.id).delete()
        return redirect("/" + article.url)
