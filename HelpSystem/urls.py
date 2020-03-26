from django.urls import path
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls import static


urlpatterns = [
    path("", views.MainView.as_view()),
    path("articles/", views.ArticlesList.as_view()),
    path("<slug:slug>/", views.ArticleDetail.as_view()),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
    path("email/new", views.AddEmail.as_view(), name="add_email"),
    path("phone/new", views.AddNumber.as_view(), name="add_phone"),
    path("about/", views.AboutDetail.as_view()),

    #path("<slug:slug>/", views.MovieDetailView.as_view(), name="movie_detail"),
   # path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
    ##Не точно
]

