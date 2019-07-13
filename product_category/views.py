from django.shortcuts import render
from django.shortcuts import render
from django.views.generic.list import ListView
from pattern_for.models import pattern_for as prod_list
# Create your views here.
from django.shortcuts import get_object_or_404
class ArticleListView(ListView):
    model = 'prod_list'
    paginate_by = 6  # if pagination is desired
    template_name = 'product_category/index.html'
    #queryset = prod_list.objects.filter(categoy=)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        for i in range(3):
            print (self.args[i])
