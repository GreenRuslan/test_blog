from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Comments
from blog.forms import CommentForm
from datetime import datetime, timedelta


def blog_list(request):
    posts = Post.objects.all()
    return render(request, "posts/posts_list.html", {"posts": posts})

def post_single(request, pk):
    post = get_object_or_404(Post, id=pk)
    comment = Comments.objects.filter(new=pk, moderation=True)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.post = post
            return redirect(post_single, pk)
    else:
        form = CommentForm()
    return render(request, "posts/post_single.html",
                  {"post": post,
                   "comments": comment,
                   "form": form})

