from django.shortcuts import render,redirect
from .models import Post,Like
from .forms import Add_Post
from django.http import JsonResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    posts = Post.objects.all().prefetch_related("post_likes", 'post_comments', 'post_comments__user').select_related("user")
    likes = Like.objects.filter(post__in=posts, user=request.user).values_list("post", flat=True)

    def is_liked_add(p):
        p.is_liked = p.id in likes
        return p

    posts = list(map(is_liked_add, posts))
    return render(request, "posts/home.html", {"posts": posts})
    
def log_out(request):
    logout(request)
    return redirect('/accounts/login/')
@login_required
def addPosts(request):
    if request.method == 'POST':
        form = Add_Post(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('/posts/home/')

    else:
        addpost = Add_Post()
        return render(request,'posts/addpost.html',{'form':addpost})

def add_likes(request, post_id):
    post = Post.objects.get(id=post_id)
    user = request.user
    response={}
    try:
        already_liked = Like.objects.get(post=post, user=user)
        already_liked.delete()
        response['status']='dislike'
    except Like.DoesNotExist:
        Like.objects.create(post=post, user=user)
        response['status']='like'
    response['count']=Like.objects.filter(post=post).count()
    return JsonResponse(response)

    