from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import ArticleData, PoliticData
from django.db.models import Q

# Create your views here.
class homeView(TemplateView):
    template_name = 'index.html'

class searchView(ListView):
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        
        temp_list = PoliticData.objects.filter(
            Q(분류__icontains = query)
        )

        object_list = ArticleData.objects.filter(
            Q(정책_index__in = temp_list.values_list('정책_index', flat = True))
        )
        
        return object_list