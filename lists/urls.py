from django.urls import path
from lists.views import ListsListView

urlpatterns = [
    path("lists/", ListsListView.as_view(), name="lists_list"),
]
