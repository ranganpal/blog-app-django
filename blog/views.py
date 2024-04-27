from django.shortcuts import render, redirect
from .models import *
import os

# Create your views here.

def signup(request):
    return render(request, 'blog/signup.html', {
        'msg': None
    })

def signedup(request):
    if request.method == 'POST':
        email = request.POST['email']

        if User.objects.filter(email=email):
            return render(request, 'blog/signup.html', {
                'msg': "User Already Exists !!!"
            })
        else:
            user = User()
            user.name = request.POST.get('name')
            user.email = request.POST.get('email')
            user.password = request.POST.get('password')
            user.active = False
            user.save()
            return redirect('/signin/')

def signin(request):
    return render(request, 'blog/signin.html', {
        'msg': None
    })

def signedin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email=email, password=password):
            user = User.objects.get(email=email, password=password)
            user.active = True
            user.save()
            return render(request, 'blog/welcome.html', {
                'user': user
            })
        else:
            return render(request, 'blog/signin.html', {
                'msg': "User Doesn't Exist !!!"
            })

def no_account(request):
    return render(request, 'blog/no_account.html')

def home(request, user_id):
    user = User.objects.get(pk=user_id)
    if user and user.active:
        posts = Post.objects.all()
        return render(request, 'blog/home.html', {
            'user': user,
            'posts': posts,
        })
    elif user and not user.active:
        return render(request, 'blog/no_account.html')
    else:
        return redirect('/signup/')

def account(request, user_id):
    user = User.objects.get(pk=user_id)
    if user and user.active:
        return render(request, 'blog/account.html', {
            'user': user
        })
    elif user and not user.active:
        return render(request, 'blog/no_account.html')
    else:
        return redirect('/signup/')

def delete(request, user_id):
    user = User.objects.get(pk=user_id)
    if user and user.active:
        user.delete()
        return redirect('/')
    elif user and not user.active:
        return render(request, 'blog/no_account.html')
    else:
        return redirect('/signup/')

def update(request, user_id):
    user = User.objects.get(pk=user_id)
    if user and user.active:
        user.name = request.POST.get('name')
        user.email = request.POST.get('email')
        user.password = request.POST.get('password')
        user.active = False
        user.save()
        return redirect('/signin/')
    elif user and not user.active:
        return render(request, 'blog/no_account.html')
    else:
        return redirect('/signup/')

def logout(request, user_id):
    user = User.objects.get(pk=user_id)
    if user and user.active:
        user.active = False
        user.save()
        return redirect('/signin/')
    elif user and not user.active:
        return render(request, 'blog/no_account.html')
    else:
        return redirect('/signup/')

def my_posts(request, user_id):
    user = User.objects.get(pk=user_id)
    if user and user.active:
        posts = Post.objects.filter(user=user)
        return render(request, 'blog/my_posts.html', {
            'user': user,
            'posts': posts,
        })
    elif user and not user.active:
        return render(request, 'blog/no_account.html')
    else:
        return redirect('/signup/')

def add_post(request, user_id):
    user = User.objects.get(pk=user_id)
    if user and user.active:
        return render(request, 'blog/add_post.html', {
            'user': user
        })
    elif user and not user.active:
        return render(request, 'blog/no_account.html')
    else:
        return redirect('/signup/')

def create_post(request, user_id):
    user = User.objects.get(pk=user_id)
    if user and user.active:
        if request.method == 'POST':
            handle_uploaded_file(
                request.FILES.get('image'),
                str(request.FILES.get('image'))
            )
            post = Post()
            post.title = request.POST.get('title')
            post.content = request.POST.get('content')
            post.image = str(request.FILES.get('image'))
            post.user = user
            post.save()
            return redirect(f'/my-posts/{user_id}')
    elif user and not user.active:
        return render(request, 'blog/no_account.html')
    else:
        return redirect('/signup/')

def read_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    user = post.user
    if user and user.active:
        return render(request, 'blog/read_post.html', {
            'user': user,
            'post': post,
        })
    elif user and not user.active:
        return render(request, 'blog/no_account.html')
    else:
        return redirect('/signup/')

def read_my_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    user = post.user
    if user and user.active:
        return render(request, 'blog/read_my_post.html', {
            'user': user,
            'post': post,
        })
    elif user and not user.active:
        return render(request, 'blog/no_account.html')
    else:
        return redirect('/signup/')

def edit_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    user = post.user
    if user and user.active:
        return render(request, 'blog/edit_post.html', {
            'user': user,
            'post': post,
        })
    elif user and not user.active:
        return render(request, 'blog/no_account.html')
    else:
        return redirect('/signup/')

def delete_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    user = post.user
    if user and user.active:
        post.delete()
        return redirect(f'/my-posts/{user.id}')
    elif user and not user.active:
        return render(request, 'blog/no_account.html')
    else:
        return redirect('/signup/')

def update_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    user = post.user
    if user and user.active:
        if request.method == 'POST':
            handle_uploaded_file(
                request.FILES.get('image'),
                str(request.FILES.get('image'))
            )
            post.title = request.POST.get('title')
            post.content = request.POST.get('content')
            post.image = str(request.FILES.get('image'))
            post.save()
            return redirect(f'/my-posts/{user.id}')
    elif user and not user.active:
        return render(request, 'blog/no_account.html')
    else:
        return redirect('/signup/')

def handle_uploaded_file(file, filename):
    if not os.path.exists('blog/media/post/'):
        os.mkdir('blog/media/post/')

    with open('blog/media/post/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
