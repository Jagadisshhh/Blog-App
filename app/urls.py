from django.urls import path
from app import views
from users import views as views_user

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("register/", views_user.register, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("profile_update/", views.profile_update, name="profile_update"),
    path("add_blog/", views.add_blog, name="add_blog"),
    path("post/<int:logged_user>/<int:post_id>/", views.post_detail, name="post_detail"),
    path("update_blog/<int:post_id>/", views.update_blog, name="update_blog"),
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
