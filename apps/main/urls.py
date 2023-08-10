from django.urls import path
from .views import post_list, create_post, delete_post,  patch_post, put_post

urlpatterns = [
    path('', post_list),
    path('create/', create_post),
    path('delete/<int:id>/', delete_post),
    path('update/<int:pk>/', patch_post),
    path('put_post/<int:pk>/', put_post)
]