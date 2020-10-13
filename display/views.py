from django.views.generic import TemplateView
from .models import Page

'''  目次表示 '''
class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        index = Page.objects.all()
        context['index'] = index
        return context

'''  記事表示 '''
class ArticleView(TemplateView):
    template_name = 'article.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_no'] = self.kwargs.get('url_no')
        return context

index = IndexView.as_view()
article = ArticleView.as_view()