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
        
        object_list = PoliticData.objects.filter(
            Q(분류 = query)
        )
        
        return object_list

class visualizedView(ListView):
    template_name = 'visualized.html'

    def get_queryset(self):
        query = self.request.path.split('/')[2]

        object_list = ArticleData.objects.filter(
            Q(정책_index = query)
        )
        
        return object_list