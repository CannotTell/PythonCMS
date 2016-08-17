from django.shortcuts import render

from .forms import LoginForm
from .models import Article


# Create your views here.
def index(request):
    latest_article_list = Article.objects.query_by_time()
    loginform = LoginForm()
    context = {'latest_article_list': latest_article_list, 'loginform':loginform}
    return render(request, 'index.html', context)