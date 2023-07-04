from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Post
from users.models import Profile
from datetime import datetime

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        context = {
            'posts' : Post.objects.all()[::-1],
        }
        return render(request, "home.html", context)
    else:
        return redirect('register')
    return render(request, "home.html", context)

def post_detail(request,logged_user,  post_id):
    post = Post.objects.get(pk = post_id)
    curr_user = post.author
    logged_user_id = logged_user
    print(logged_user_id)
    print(curr_user.id)
    return render(request, 'post_detail.html', {'user': curr_user, 'post':post,'logged_user_id': logged_user_id} )

def about(request):
    return HttpResponse("This is about page")

# def register(request):
#     return render(request, "register.html")

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            return render(request, "login.html")
        
    return render(request, "login.html")

def logout_user(request):
    logout(request)
    return redirect("login")

def profile(request):
    current_user = request.user
    id = current_user.id
    context = {
        'id' : id
    }
    return render(request, 'profile.html', context)

def profile_update(request):
    if request.method == 'POST':
        email = request.POST['email']
        facebook_link = request.POST['fb_link']
        github_link = request.POST['git_link']
        image = request.FILES['image']
        user = request.user
        Profile.objects.filter(user = user).update(email=email, facebook_link = facebook_link, github_link = github_link, image = image)
        return redirect("profile")


    return render(request, 'profile_update.html')

def add_blog(request):
    if request.method == "POST":
        curr_user = request.user
        print(curr_user)
        title = request.POST['title']
        content = request.POST['content']
        author = curr_user
        date_posted = datetime.now()
        post = Post(title=title, content = content , author = author, date_posted=date_posted)
        post.save()
        return redirect('home')

    return render(request, 'add_blog.html')

def update_blog(request, post_id):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        print(Post.objects.get(id = post_id))
        post = Post.objects.filter(id = post_id).update(title = title, content = content)
        print(post)
        return redirect('home')

    post = Post.objects.get(id = post_id)
    return render(request, 'update_blog.html', {'post':post})

