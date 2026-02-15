from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import CommentForm
from .models import Post

# Create your views here.


def posts(request):
    """
    Render the index page of the blog.
    """
    posts = Post.objects.all()
    return render(request, 'blog/posts.html', {'posts': posts})


def post_details(request, post_id):
    """
    Render the detail page of a specific blog post.
    """
    post = Post.objects.get(id=post_id)
    form = CommentForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        form = CommentForm()  # Reset the form after saving
        return HttpResponseRedirect(reverse("blog:post_details", args=(post.id,)))
    comments = post.comments.all()
    return render(request, 'blog/post_details.html', {'post': post, 'form': form, 'comments': comments})


def comment_delete(request, post_id, comment_id):
    """
    Delete a comment from a blog post.
    """
    post = Post.objects.get(id=post_id)
    comment = post.comments.get(id=comment_id)
    comment.delete()
    return HttpResponseRedirect(reverse("blog:post_details", args=(post.id,)))


def comment_edit(request, post_id, comment_id):
    """
    Edit a comment on a blog post.
    """
    post = Post.objects.get(id=post_id)
    comment = post.comments.get(id=comment_id)
    form = CommentForm(request.POST or None, instance=comment)
    
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("blog:post_details", args=(post.id,)))
    
    return render(request, 'blog/comment_edit.html', {'form': form, 'post': post, 'comment': comment})