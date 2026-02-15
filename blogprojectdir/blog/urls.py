from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path('posts/', views.posts, name='posts'),
    path('post/<int:post_id>/', views.post_details, name='post_details'),
    path('post/<int:post_id>/comment/<int:comment_id>/delete', views.comment_delete, name='comment_delete'),
    path('post/<int:post_id>/comment/<int:comment_id>/edit', views.comment_edit, name='comment_edit'),
]
