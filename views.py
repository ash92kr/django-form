from django.shortcuts import render, redirect, resolve_url
from .forms import PostForm, PostModelForm
from .models import Post

# Create your views here.
def list(request):
    posts = Post.objects.all()
    return render(request, 'post/list.html', {'posts': posts})
    
def create(request):
    if request.method == "POST":
        # 저장로직
        form = PostForm(request.POST)  # PostForm은 html로 바꿔주는 함수
        if form.is_valid():   # 유효성 검사(필수인데 공백으로 입력하거나 중복 금지 등, 형식을 안 맞는 컬럼을 거르는 경우)
            # title = form.cleaned_data['title']  # 검증 작업을 거친 데이터를 cleaned_data로 부름
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            Post.objects.create(title=title, content=content)
            return redirect(resolve_url('post:list'))  # post에 있는 list의 이름을 가져옴
    else: # GET 방식(사용자가 값을 입력하지 않은 경우)
        # 사용자가 입력할 수 있는 폼 리턴
        form = PostForm()
    return render(request, 'post/create.html', {'form': form})
    # 저장이 될 수 있는 폼을 생성해 post/create.html로 넘김

def detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post/detail.html', {'post':post})

def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect(resolve_url('post:list'))

def update(request, id):
    post = Post.objects.get(id=id)  # 기존 데이터를 넣은 공간
    if request.method == "POST":
        # 폼을 검증 후 수정, 저장하는 단계
        form = PostForm(request.POST)  # request를 통해 사용자가 입력한 정보를 담음
        if form.is_valid():  # 허용이 되는 값이 들어오면
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            # post.update(title=title, content=content)  # 기존의 post값을 수정함
            post.title = title
            post.content=content
            post.save()
            return redirect(resolve_url('post:detail', id))  # 전체 글이 아닌 개별 글을 보여주는 페이지
    else:  # get 방식
        # 기존의 데이터를 폼에 담아서 사용자에게 전달
        form = PostForm({'title':post.title, 'content':post.content})  # title과 content를 값으로 가짐
    return render(request, 'post/update.html', {'form':form, 'post':post})  # form을 담아주는 공간도 같이 넘겨야 한다
        

def model_create(request):
    if request.method == "POST":
        # 저장하는 로직    
        pass
    else:   # 폼을 보여주는 규칙
        form = PostModelForm()
    return render(request, 'post/model_create.html', {"form":form})

def model_update(request, id):
    pass