from django.urls import path
from webpage import views

urlpatterns = [
    path('contact', views.contact, name = 'contact'),
    path('', views.index, name = 'index'),
    path('services', views.services, name = 'services'),
    path('projects', views.projects, name = 'projects'),
    path('blog/',views.PostListView.as_view(),name='post_list'),
    path('blog/<int:pk>/',views.PostDetailView.as_view(),name='post_detail'),
    path('blog/new/',views.CreatePost.as_view(),name='post_create'),
    path('blog/update/<int:pk>',views.UpdatePost.as_view(),name='post_update'),
    path('blog/delete/<int:pk>',views.DeletePost.as_view(),name='post_delete'),
    path('blog/category/<str:cats>/',views.CategoryView,name='category'),
    path('blog/<int:pk>/comment/',views.CommentView.as_view(),name='post_comment'),
    path('blog/comment/<int:pk>/remove/',views.comment_remove,name='comment_remove'),
]
