from django.urls import path
from . import views
from . import util


encyclopedia_list = util.list_entries()

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<title>/".lower(), views.encyclopedia, name='entry_title'),
    path('search', views.search, name='search_processing'),
    path('create', views.create, name='create')
]



