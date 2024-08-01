from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    # create 한 댓글을 생성? 관리하는 페이지
    path('<int:article_id>/coments/create/', views.comment_create, name='comment_create'),
]