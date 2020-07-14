from django.urls import path
from . import views

urlpatterns = [
    path("", views.MainView.as_view(), name="main"),
    path("accounts/register", views.RegisterFormView.as_view(), name="register"),
    path("articles/", views.ArticlesList.as_view(), name="articles_list"),
    path("about/", views.AboutDetail.as_view(), name="about"),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
    path("addLike/<int:pk>/", views.AddLike.as_view(), name="add_like"),
    path("delLike/<int:pk>/", views.DelLike.as_view(), name="del_like"),
    path("email/new", views.AddEmail.as_view(), name="add_email"),
    path("phone/new", views.AddNumber.as_view(), name="add_phone"),
    path("programs/<slug:slug>", views.ProgramDetail.as_view(), name="program_detail"),
    path("<slug:slug>/", views.ArticleDetail.as_view(), name="article_detail"),
]
