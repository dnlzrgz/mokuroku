from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from lists.models import List


class ListsListView(LoginRequiredMixin, ListView):
    model = List
    template_name = "lists/lists.html"
    context_object_name = "lists"

    def get_queryset(self):
        return List.objects.filter(user=self.request.user).prefetch_related("tasks")
