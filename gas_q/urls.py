from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("json", views.json, name="json"),
    path("export_data", views.export_data, name="export_data"),
    path("excel", views.excel, name="excel"),
]

