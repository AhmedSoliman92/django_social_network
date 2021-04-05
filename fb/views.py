from django.shortcuts import render
from .models import Post
posts = [
    {
        'title': 'The peace and war',
        'author': 'Ahmed',
        'date': '1.Sep. 1992',
        'content': 'the peace is very important issue.'
    },
    {
        'title': 'the honey girl',
        'author': 'medo ',
        'date': '1.Sep. 2021',
        'content': 'She is pretty girl.'
    }
]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'fb/home.html', context)


def about(request):
    return render(request, 'fb/about.html', {'title': 'About Page'})
