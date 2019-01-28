from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Comments
from blog.forms import CommentForm

def blog_list(request):
    posts = Post.objects.all()
    return render(request, "posts/posts_list.html", {"posts": posts})

# def make_pagination_html(current_page, total_pages):
#
#     pagination_string = ""
#
#     if float(current_page) > 1:
#
#         pagination_string += '<a href="?page=%s">previous</a>' % (current_page -1)
#
#     pagination_string += '<span class="current"> Page %s of %s </span>' %(current_page, total_pages)
#
#     if float(current_page) < total_pages:
#
#         pagination_string += '<a href="?page=%s">next</a>' % (current_page + 1)
#
#     return pagination_string
#
# def listing(request):
#
#     current_page = request.GET.get('page' ,'1')
#
#     limit = 3 * int(current_page)
#
#     offset = limit - 3
#
#     comments_list = Comments.objects.all()[offset:limit]  # limiting contacts based on current_page
#
#     total_comments = Comments.objects.all().count()
#
#     total_pages = total_comments / 3
#
#     if total_comments % 3 != 0:
#
#         total_pages += 1 # adding one more page if the last page will contains less contacts
#
#         pagination = make_pagination_html(current_page, total_pages)
#
#     return {'pagination':pagination, 'comments_list':comments_list}

def post_single(request, pk):
    post = get_object_or_404(Post, id=pk)
    comment = Comments.objects.filter(post_id=pk, moderation=True)
    if request.method == "POST":
        print(request.POST)
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.post = post
            form.save()
            return redirect(post_single, pk)
    else:
        form = CommentForm()

    return render(request, "posts/post_single.html",
                  {"post": post,
                   "comments": comment,
                   "form": form,
                   # "pagination": listing(request)['pagination'],
                   # "comments_list": listing(request)["comments_list"]
                   })

