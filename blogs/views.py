from django.shortcuts import get_object_or_404, render
from .models import Blog

# Create your views here.
def blogs(request):
    # blogs = Blog.objects.all()
    # blogs = Blog.objects.order_by('created_at').reverse()
    # blogs = Blog.objects.order_by('-created_at')[:5]
    blogs = Blog.objects.order_by('-created_at')
    return render(request, 'blogs/blogs.html', {'blogs': blogs})

def blog(request, blog_id):
    # blog = Blog.objects.get(pk=blog_id)
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogs/blog.html', {'blog': blog})