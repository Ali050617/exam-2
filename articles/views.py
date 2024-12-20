from django.shortcuts import render, redirect, get_object_or_404
from .models import Articles


def home(request):
    articles = Articles.objects.all()
    ctx = {'articles': articles}
    return render(request,'index.html', ctx)



def article_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        short_content = request.POST.get('short_content')
        long_content = request.POST.get('long_content')
        category = request.POST.get('category')
        auther_name = request.POST.get('auther_name')
        if title and short_content and long_content and category and auther_name:
            Articles.objects.create(
                title=title,
                short_content=short_content,
                long_content=long_content,
                category=category,
                auther_name=auther_name
            )
            return redirect('home')
    return render(request, 'articles/add-post.html')




def articles_by_category(request, category):
    articles = Articles.objects.filter(category=category)
    ctx = {'articles': articles, 'category': category}
    return render(request, 'articles/articles-by-category.html', ctx)



def articles_detail(request, articles_id):
    articles = get_object_or_404(Articles, pk=articles_id)
    ctx = {'articles': articles}
    return render(request, 'articles/detail.html', ctx)