from django.shortcuts import render
from .models import News_post

# Create your views here.

def home(request):
    news = News_post.objects.all()
    return render(request, 'news_time/news_time.html', {'news': news})



