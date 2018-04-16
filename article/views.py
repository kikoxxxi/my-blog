from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from article.models import Article
from datetime import datetime

# Create your views here.


def home(request):
    template = get_template('index.html')
    post_list = Article.objects.all()
    html = template.render(locals())
    return HttpResponse(html)


def detail(response, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    template = get_template('post.html')
    html = template.render(locals())
    return HttpResponse(html)
