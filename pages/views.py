from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest
from pages.models import Post

# Create your views here.
def home(request):
    ctx = {"title": "Home", "features": ["Django", "Templates", "Static files"]}
    return render(request, "home.html", ctx)

def about(request):
    return render(request, "about.html", {"title": "About"})

def hello(request, name):
    return render(request, "hello.html", {"name": name})

def gallery(request):
    # Assume images placed in pages/static/img/
    images = ["img1.jpg", "img2.jpg", "img3.jpg"]
    return render(request, "gallery.html", {"images": images})

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def server_error_view(request):
    return render(request, '500.html', status=500)

def post_list(request):
    # Model.objects.all()
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'title': 'Posts',
    }
    return render(request, 'post_list.html', context)

def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        if not title or not body:
            return HttpResponseBadRequest('Title and body are required.')
        Post.objects.create(title=title, body=body)
        return redirect('post_list')
    return render(request, 'post_form.html')

def post_view(request, pk):
    # post = get_object_or_404(Post, pk=pk)
    post = Post.objects.get(pk=pk)
    return render(request, 'post_view.html', {'post': post})

def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.title = request.POST.get('title') or post.title
        post.body = request.POST.get('body') or post.body
        post.save()
        return redirect('post_view', pk=pk)
    return render(request, 'post_form.html', {'post': post})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'post_confirm_delete.html', {'post': post})