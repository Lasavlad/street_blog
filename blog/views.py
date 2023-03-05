from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from .models import Post, Comment
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



# Create your views here.
