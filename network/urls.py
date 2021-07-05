
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_posts", views.create_posts, name = "create_posts"),
    path("all_posts", views.all_posts, name = "all_posts"),
    path("profile/<int:user_id>", views.profile, name="profile"),
    path("user_profile/<int:user_id>", views.user_profile, name="user_profile"),
    path("follow/<int:id>", views.follow, name = "follow"),
    path("unfollow/<int:id>", views.unfollow, name = "unfollow"),
    path("following", views.following, name = "following"),
    path("edit_page/<int:post_id>", views.edit_page, name = "edit_page"),
    path("edit_post/<int:post_id>", views.edit_post, name = "edit_post")
]
