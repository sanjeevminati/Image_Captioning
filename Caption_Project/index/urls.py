from django.contrib import admin
from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('register/',views.register,name="register"),
    path('login/',auth_views.LoginView.as_view(template_name="index/login.html"),name="login"),
    path('index/',views.index,name="index"),
    path('logout/',auth_views.LogoutView.as_view(template_name="index/login.html"),name="upload_image/logout"),
    path('upload/', views.upload,name="upload"),
    path('upload_save',views.upload_save,name="upload_save"),
    path('caption/',views.caption,name="caption"),
    path('success_upload/',views.success_upload,name="success_upload"),
    path('success_caption_upload/',views.success_caption_upload,name="success_caption_upload"),
    path('password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete')
]

