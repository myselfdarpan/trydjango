from django.shortcuts import render, get_object_or_404
from django.urls import reverse

# Create your views here.

from django.views.generic import(
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
    DetailView,

)

from .models import Article
from .forms import ArticleModelForm

class ArticleCreateView(CreateView):
    template_name = 'article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

class ArticleListView(ListView):
    template_name = 'article_list.html'
    queryset = Article.objects.all()

class ArticleDetailView(DetailView):
    template_name = 'article_details.html'
    # queryset = Article.objects.all()

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Article, id = id)


class ArticleUpdateView(UpdateView):
    template_name = 'article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Article, id = id)

class ArticleDeleteView(DeleteView):
    template_name = 'article_delete.html'
    # queryset = Article.objects.all()

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Article, id = id)

    def get_success_url(self):
        return reverse("blog:article_list")
    