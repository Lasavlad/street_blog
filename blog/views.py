from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, DetailView

from .models import Post, Comment, Category
from .forms import Comment_form

class HomePageView(TemplateView):
    template_name = 'home_view.html'

    def get_context_data(self,*args, **kwargs):
        context = super(HomePageView, self).get_context_data(*args,**kwargs)
        context['posts'] = Post.objects.all()
        return context  

@login_required
def post_detail_view(request, slug):
    #post detail
    post = get_object_or_404(Post, slug=slug)
    user = request.user

    #comments
    comments = post.comments.all()


    if request.method == 'POST':
        comment_form = Comment_form(request.POST)
        if comment_form.is_valid():
            form = comment_form.save(commit=False)
            form.posted_by = request.user
            form.post = post
            form.save()
            return redirect('post-detail-view', slug=post.slug)
    else:
        comment_form = Comment_form()

            
    context = {
        'user':user,
        'comment_form':comment_form,
        'post':post, 
        'comments':comments,
    }
    return render(request, 'blog/post_detail_view.html', context)

    

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail_view.html'
    context_object_name = 'post'
    slug_url_kwarg = 'slug'

    def add_comment(self):
        post = self.get_object()
        if self.request.method == 'POST':
            comment_form = Comment_form(self.request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.posted_by = self.request.user
                comment.save()
            else:
                comment_form = Comment_form()
        context = {
            'post':post,
            'comment_form':comment_form,
        }
        return render(self.request, self.template_name, context)

def art_category(request):
    category= Category.objects.get(name='Art').id
    posts = Post.objects.filter(category=category)[1:4]
    latest_post = posts[0]

    context = {
        'posts':posts,
        'latest_post':latest_post
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


