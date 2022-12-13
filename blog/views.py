from typing import Optional

from django.shortcuts import render, redirect

from .models import Post, PostForm


def index(request):
    data = Post.objects.all()
    ctx = {
        'title': 'Blog',
        'heading': 'Blog',
        'subheading': 'Postingan',
        'post': data
    }
    return render(request=request, template_name='blog/blog.html', context=ctx)


def form_post(request):
    if request.method == 'POST':
        data = PostForm(request.POST)

        if data.is_valid():
            in_data = Post(**data.cleaned_data)
            in_data.save()
            return redirect('blog:index')

    form = PostForm()

    return render(request, 'blog/form.html', {'form': form})
