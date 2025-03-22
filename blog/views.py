from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Blog

def blog(request):
    st = request.GET.get('blogname', '')  # Get the search query

    if st:
        blogsData = Blog.objects.filter(blog_title__icontains=st).order_by('-blog_title')
    else:
        blogsData = Blog.objects.all().order_by('-blog_title')

    # Apply pagination to the filtered results
    paginator = Paginator(blogsData, 2)  # 2 blogs per page
    page_number = request.GET.get('page')
    blogDatafinal = paginator.get_page(page_number)
    totalpage = blogDatafinal.paginator.num_pages

    data = {
        'blogsData': blogDatafinal,
        'lastpage': totalpage,
        'totalPagelist': [n + 1 for n in range(totalpage)],
        'title': 'Contact',
        'name': 'Nischal'
    }
    return render(request, "blog/blogs.html", data)
