from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.views.generic import ListView

from .models import Followers, Following, Posts, Profile, User

class PostsList(ListView):
    paginate_by = 2
    model = Posts

def Pagination(request, post_list):
    paginator = Paginator(post_list, 1)
    page_number = request.GET.get("page")
    posts_page = paginator.get_page(page_number)
    return posts_page

def index(request):
    return render(request, "network/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            Profile.objects.create(user = user, followers = 0, following = 0)
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

@login_required(login_url='login')
def create_posts(request):
    if request.method == "POST":
        Posts.objects.create(user = request.user, content = request.POST["posts"], likes = 0)
        return HttpResponseRedirect(reverse("all_posts"))
    
    return render(request, "network/create_posts.html")

@login_required(login_url='login')
def all_posts(request):
    posts_page = Pagination(request, Posts.objects.order_by("-timestamp").all())
    return render(request, "network/all_posts.html", {
        "posts":posts_page
    })

@login_required(login_url='login')
def profile(request, user_id):
    x = Posts.objects.get(pk = user_id).user
    user_profile = Profile.objects.get(user = x)
    exists = Followers.objects.filter(follower = request.user, user = x).exists()
    user_posts = Pagination(request, Posts.objects.filter(user = x).order_by("-timestamp"))
    return render(request, "network/profiles.html", {
        "user_profile":user_profile, "user_posts":user_posts, "accessing_user":request.user, "exists":exists
    })

@login_required(login_url='login')
def user_profile(request, user_id):
    user_profile = Profile.objects.get(user = user_id)
    user_posts = Pagination(request, Posts.objects.filter(user = user_id).order_by("-timestamp"))
    return render(request, "network/profiles.html", {
        "user_profile":user_profile, "user_posts":user_posts, "accessing_user":request.user
    })

@csrf_exempt
@login_required(login_url='login')
def follow(request, id):
    if request.method == "PUT":
        profile = Profile.objects.get(user = id)
        profile.followers = profile.followers + 1
        profile.save()
        accessor = Profile.objects.get(user = request.user)
        accessor.following = accessor.following + 1
        accessor.save()
        Followers.objects.create(user = profile.user, follower = accessor.user)
        Following.objects.create(user = accessor.user, following = profile.user)
        return HttpResponse(status = 204)

@csrf_exempt
@login_required(login_url='login')
def unfollow(request, id):
        profile = Profile.objects.get(user = id)
        profile.followers = profile.followers - 1
        profile.save()
        accessor = Profile.objects.get(user = request.user)
        accessor.following = accessor.following - 1
        accessor.save()
        Followers.objects.get(user = profile.user, follower = accessor.user).delete()
        Following.objects.get(user = accessor.user, following = profile.user).delete()

@login_required(login_url='login')
def following(request):
    following_users_objects = Following.objects.filter(user = request.user)
    following_users = []
    for following_users_object in following_users_objects:
        following_users.append(following_users_object.following)
    posts = []
    for following_user in following_users:
        posts.extend(Posts.objects.filter(user = following_user))
    posts.sort(key=lambda x:x.timestamp, reverse=True)
    posts_page = Pagination(request, posts)
    return render(request, "network/all_posts.html", {
        "posts":posts_page
    })