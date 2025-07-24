from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from .modules.register import Register
from .modules.edition import Edition
from .modules.news import News
from .modules.comment import Comment

class IndexView(View):

    def get(self, request, *args, **kwargs):
        context = {"editions": Edition.getEditions()}
        return render(request, "jornal/index.html", context)
    
class RegisterView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "jornal/register.html")
    
    def post(self, request, *args, **kwargs):
        _first_name = request.POST.get("first_name")
        _last_name = request.POST.get("last_name")
        _username = request.POST.get("username")
        _email = request.POST.get("email")
        _password = request.POST.get("password")
        try:
            user = Register.registerUser(_first_name, _last_name, _username, _email, _password)
            login(request, user)
            context = {"success": True, "redirect": "/index"}
        except ValidationError as error:
            context = {"success": False, "errors": error.message_dict}
        return JsonResponse(context)

class LoginView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "jornal/login.html")
    
    def post(self, request, *args, **kwargs):
        _username = request.POST.get("username")
        _password = request.POST.get("password")
        user = authenticate(username=_username, password=_password)
        if (user):
            login(request, user)
            context = {"success": True, "redirect": "/index"}
        else:
            context = {"success": False, "error": "Username e/ou senha inválidos"}
        return JsonResponse(context)

class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("/index")

class EditionView(View):

    def get(self, request, *args, **kwargs):
        url_name = request.resolver_match.url_name
        if (url_name == "create-edition"):
            return redirect("/index")
        edition_id = self.kwargs["edition_id"]
        edition_object = Edition.getOne(edition_id)
        news = News.getNews(edition_id)
        context = {"edition": edition_object, "news": news}
        return render(request, "jornal/edition.html", context)
    
    def post(self, request, *args, **kwargs):
        _autor = request.user
        _data = request.POST.get("data")
        try:
            ed = Edition.createEdition(_autor, _data)
            return redirect(f"/edition/view/{ed.id}")
        except ValidationError as error:
            context = error.message_dict
            return render(request, "jornal/index.html", context)   

class NewsView(View):

    def get(self, request, *args, **kwargs):
        url_name = request.resolver_match.url_name
        if (url_name == "create-news"):
            return redirect("/index")
        edition_id = self.kwargs["edition_id"]
        news_id = self.kwargs["news_id"]
        news_object = News.getOne(news_id)
        comments = Comment.getComments(news_id)
        context = {"edition_id": edition_id, "news": news_object, "comments": comments}
        return render(request, "jornal/news.html", context)
    
    def post(self, request, *args, **kwargs):
        _titulo = request.POST.get("titulo")
        _conteudo = request.POST.get("conteudo")
        _autor = request.user.id
        _edicao = self.kwargs["edition_id"]
        try:
            news = News.createNews(_autor, _edicao, _titulo, _conteudo)
            return redirect(f"/edition/{_edicao}/news/view/{news.id}")
        except ValidationError as error:
            context = error.message_dict
            return render(request, "jornal/edition.html", context)

class CommentView(View):

    def post(self, request, *args, **kwargs):
        _autor_id = request.user.id
        _conteudo = request.POST.get("conteudo")
        news_id = self.kwargs["news_id"]
        try:
            comment = Comment.createComment(_autor_id, news_id, _conteudo)
            context = {"success": True, "comment": {"username": comment.autor.username, "conteudo": comment.conteudo }}
        except ValidationError as error:
            context = {"success": False, "error": error.message_dict}
        return JsonResponse(context)


            
