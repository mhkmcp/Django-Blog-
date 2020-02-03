from django.urls import path
from blog import views as v

app_name = 'blog'

urlpatterns = [
    path('', v.PostListView.as_view(), name='home'),
    path('post/<str:username>', v.UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>', v.PostDetailView.as_view(), name='post-detail'),
    path('post/new', v.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', v.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', v.PostDeleteView.as_view(), name='post-delete'),
    path('about', v.about, name='about'),
]
