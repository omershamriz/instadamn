from django.urls import path
from post import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newpost/', views.NewPost, name='newpost'),
    path('<uuid:post_id>/', views.PostDetail, name='post-details'),
    path('tag/<slug:tag_slug>/', views.tags, name='tags'),
    path('<uuid:post_id>/like', views.like, name='like'),
    path('<uuid:post_id>/favorite', views.favorite, name='post-favorite')
]