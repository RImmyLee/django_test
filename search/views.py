from django.views.generic import TemplateView, ListView
from .models import ArticleData, PoliticData
from django.db.models import Q
import requests

# Create your views here.
class homeView(TemplateView):
    template_name = 'index.html'

class searchView(ListView):
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        try:
            response = requests.get(
                url = 'https://transformers-pipeline.ai-api.datadriven.kr/',
                params = {
                    'model_name': 'popo-classifier',
                    'gitlab_model_path': 'popo-classifier',
                    'text': query,
                    'pipeline_type': 'text-classification',
                }, 
            )

            json_list = response.json()
            
            object_list = PoliticData.objects.filter(
                Q(분류 = json_list[0]['label'])
            )
            
            return object_list
        except requests.exceptions.RequestException:
            print('HTTP Request failed')

class visualizedView(ListView):
    template_name = 'visualized.html'

    def get_queryset(self):
        query = self.request.path.split('/')[2]

        object_list = ArticleData.objects.filter(
            Q(정책_index = query)
        )
        
        return object_list