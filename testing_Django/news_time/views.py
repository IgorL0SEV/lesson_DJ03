from django.shortcuts import render
from .models import News_post
from .forms import News_postForm

# Create your views here.

def home(request):
    news = News_post.objects.all()
    return render(request, 'news_time/news_time.html', {'news': news})

def create_news(request):
    form = News_postForm()
    return render(request, 'news_time/add_new_post.html', {'form': form})


