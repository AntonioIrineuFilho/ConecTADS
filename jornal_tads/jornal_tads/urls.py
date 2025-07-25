from django.contrib import admin
from django.views.generic.base import RedirectView
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(url='/index/', permanent=True)),
    path("", include("jornal.urls"))
]
