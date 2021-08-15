from django.urls import path
from .views import (

    ArticleDetailView,
    ArticleListView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView

)


app_name = 'blog'
urlpatterns = [

    path('create/', ArticleCreateView.as_view(), name='article_create'),
    path('', ArticleListView.as_view(), name='article_list'),
    path('detail/<int:id>/', ArticleDetailView.as_view(), name='article_detail'),
    path('update/<int:id>/', ArticleUpdateView.as_view(), name='article_update'),
    path('delete/<int:id>/', ArticleDeleteView.as_view(), name='article_delete'),
    # path('create/', product_create_view, name='create'),   
]
