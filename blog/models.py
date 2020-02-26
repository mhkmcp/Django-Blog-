from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# class PostManager(models.Manager):
#     def get_all_comments(self, **kwargs):
#         comments = Comment.objects.filter(post = se)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts_author")
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # provide redirect url after post is saved
        return reverse('blog:post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post        = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author      = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_author')
    content     = models.TextField()
    active      = models.BooleanField(default=True)
    updated_at  = models.DateTimeField(auto_now=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    # def get_absolute_url(self, *args, **kwargs):
    #     return reverse('blog:home', kwargs={'pk': self.pk})
