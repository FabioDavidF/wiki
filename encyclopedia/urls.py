from django.urls import path
from . import views
from . import util


encyclopedia_list = util.list_entries()

urlpatterns = [
    path("", views.index, name="index"),
    path("entry/<title>/".lower(), views.encyclopedia, name='entry_title'),
]



