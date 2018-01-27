from django.shortcuts import render
from .models import Post
from django.views import generic


class InspirationView(generic.ListView):
    template_name = 'inspiration/index.html'

    def get_queryset(self):
        return Post.objects.all()


class DetailView(generic.DetailView):
    model = Post
    template_name = 'inspiration/detail.html'


