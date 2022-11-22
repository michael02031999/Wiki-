from django.urls import path

from . import views

urlpatterns = [
    path("wiki/random_page", views.random_page, name = "random_page"),
    path("wiki/edit_markdown", views.edit_markdown, name = "edit_markdown"),
    path("wiki/create_new_page", views.create_new_page, name = "create_new_page"),
    path("wiki/<str:entry>", views.entry, name="entry"),
    path("", views.index, name="index")
]
