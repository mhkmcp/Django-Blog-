from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.views.generic import (
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
    ListView
)

from blog.models import Post
# from blog.forms import CommentForm


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context=context)


class PostListView(ListView):
    model = Post
    # by default django expect 'blog/post_list.html'
    template_name = 'blog/home.html'
    # by default django provide 'object_list' for posts
    # form_class = CommentForm
    context_object_name = 'posts'

    # query
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    # by default django expect 'blog/post_list.html'
    template_name = 'blog/user_posts.html'
    # by default django provide 'object_list' for posts
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    # def get_object(self):
    #     return Post.objects.get(id=id)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # fields with my view
    fields = ['title', 'content']

    def form_valid(self, form):
        # author for the post
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    # fields with my view
    fields = ['title', 'content']

    def form_valid(self, form):
        # author for the post
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        # check if the user trying to update the post is the author of the post
        post = self.get_object()
        # return True if self.request.user == post.author else False
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # 'blog:home' takes to 'post/pk/home'
    success_url = '/'

    def test_func(self):
        # check if the user trying to delete the post is the author of the post
        post = self.get_object()
        return True if self.request.user == post.author else False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
