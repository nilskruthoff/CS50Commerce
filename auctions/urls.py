from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("todo/<str:title>", views.todo, name="todo"),
    path("create", views.create_listing, name="create"),
    path("auction/<int:id>", views.listing, name="listing")
]
