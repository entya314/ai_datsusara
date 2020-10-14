from django.views.generic import TemplateView
from .models import Article

'''  目次表示 '''
class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        index = Article.objects.all().order_by('post_id')
        context['index'] = index
        return context

'''  記事表示 '''
class ArticleView(TemplateView):
    template_name = 'article.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_no = self.kwargs.get('url_no')
        article_data = Article.objects.filter(url=url_no).first()
        context['article_data'] = article_data
        print(article_data)
        return context

index = IndexView.as_view()
article = ArticleView.as_view()