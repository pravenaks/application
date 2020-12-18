from django.shortcuts import render, redirect
from blog.models import Post
from blog.form import PostForm


def home(request):
    post = Post.objects.all()
    data = {
        'posts': post
    }
    return render(request, template_name='blog/home.html', context=data)


def about(request):
    return render(request, template_name='blog/about.html')


def createPost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home-url")
    data = {
        'form': form
    }
    return render(request, template_name='blog/createPost.html', context=data)
