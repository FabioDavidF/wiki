from django.urls import path
from . import views
from . import util


urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<title>/".lower(), views.encyclopedia, name='entry_title'),
    path("wiki/<title>/edit".lower(), views.edit, name='edit'),
    path("wiki/<title>/edit/processing".lower(), views.edit_file, name='edit_processing'),
    path('search', views.search, name='search_processing'),
    path('create', views.create, name='create'),
    path('create_file', views.create_file, name='create_file')
]



