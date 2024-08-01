from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm,CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.all()

    context = {
        'articles' : articles,
    }

    return render(request, 'index.html', context)

def detail(request, id):
    article = Article.objects.get(id=id)
    form = CommentForm()

    comments = Comment.objects.filter(article_id=id)

    context = {
        'article' : article,
        'form' : form,
        'comments' : comments,
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

def comment_create(request, article_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            #커밋하지말고 일단 기다려라 라는 뜻
            comment = form.save(commit=False)

            # #1. 사용자 입력 정보가 아닌 객체를 저장하여 article_id 받기(?)
            # article = Article.objects.get(id=article_id)
            # comment.article = article
            # comment.save()
            # return redirect('articles:detail', id=article_id)

            #2. integer(숫자)를 저장하는 방법
            comment.article_id = article_id
            comment.save()
            return redirect('articles:detail', id=article_id)


    else:
        return redirect('articles:index')

def comment_delete(request, article_id, id):
    if request.method =='POST':
        comment = Comment.objects.get(id=id)
        comment.delete()
    # POST든 아니든 디테일 페이지로 돌아가도록 인덴트를 빼줌    
    return redirect('articles:detail', id=article_id)