from django.urls import path
from . import views


app_name = 'articles'

urlpatterns = [
    path('create/', views.article_create, name='create'),
    path('category/<str:category>/', views.articles_by_category, name='articles_category'),
    path('detail/<int:articles_id>/', views.articles_detail, name='detail')
]