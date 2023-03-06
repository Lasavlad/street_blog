from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from .models import Post, Comment, Category
from .forms import Comment_form

class HomePageView(TemplateView):
    template_name = 'home_view.html'

    def get_context_data(self,*args, **kwargs):
        context = super(HomePageView, self).get_context_data(*args,**kwargs)
        context['posts'] = Post.objects.all()
        return context  

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail_view.html'
    context_object_name = 'post'
    slug_url_kwarg = 'slug'


def art_category(request):
    category= Category.objects.get(name='Art').id
    posts = Post.objects.filter(category=category)

    context = {
        'posts':posts
    }

    return render(request, 'blog/art_category.html', context)

def fashion_category(request):
    category= Category.objects.get(name='Fashion').id
    posts = Post.objects.filter(category=category)

    context = {
        'posts':posts
    }

    return render(request, 'blog/fashion_category.html', context)

def brand_category(request):
    category= Category.objects.get(name='Brand').id
    posts = Post.objects.filter(category=category)

    context = {
        'posts':posts
    }

    return render(request, 'blog/brand_category.html', context)

def music_category(request):
    category= Category.objects.get(name='Music').id
    posts = Post.objects.filter(category=category)

    context = {
        'posts':posts
    }

    return render(request, 'blog/music_category.html', context)


