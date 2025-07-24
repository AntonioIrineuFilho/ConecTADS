from . import views
from django.urls import path

app_name = "jornal"

urlpatterns = [
    path("index/", views.IndexView.as_view(), name="index"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("edition/create", views.EditionView.as_view(), name="create-edition"),
    path("edition/view/<int:edition_id>", views.EditionView.as_view(), name="view-edition"),
    path("edition/<int:edition_id>/news/create", views.NewsView.as_view(), name="create-news"),
    path("edition/<int:edition_id>/news/view/<int:news_id>/", views.NewsView.as_view(), name="view-news"),
    path("edition/<int:edition_id>/news/view/<int:news_id>/comment/", views.CommentView.as_view(), name="create-comment")
]