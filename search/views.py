from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import TestData
from django.db.models import Q

# Create your views here.
class homeView(TemplateView):
    template_name = 'index.html'

class searchView(ListView):
    model = TestData
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = TestData.objects.filter(
            Q(의원명__icontains = query)
        )
        print(object_list)
        return object_list