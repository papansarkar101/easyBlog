# from . import views
from .views import LikeView, HomeView, ArticleView, AddPostView, UpdateArticleView, DeleteArticleView, AddCategoryView, CategoryView
from django.urls import path

urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleView.as_view(), name="article"),
    path('addpost/', AddPostView.as_view(), name='addpost'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>/', UpdateArticleView.as_view(), name='updatepost'),
    path('article/<int:pk>/remove', DeleteArticleView.as_view(), name='deletepost'),
    path('category/<str:ctgs>/', CategoryView, name='category'),
    path('like/<int:pk>', LikeView, name="like_post")
]
