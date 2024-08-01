from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()

    context = {
        'articles' : articles,
    }

    return render(request, 'index.html', context)

def detail(request, id):
    article = Article.objects.get(id=id)

    context = {
        'article' : article
    }

    return render(request, 'detail.html', context)

def create(request):
    ##POST방식으로 들어왔을때
    if request.method =='POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', id=article.id)
        else:
            pass
    ##그렇지 않을때 (GET 방식으로 들어왔을때?)
    else:
        form = ArticleForm()

    # if문 바깥에 작성
    context = {
        'form' : form,
    }
    # 이름을 form.html로 한 이유 (두가지 기능 통합)
    return render(request, 'form.html', context)