from django.conf.urls import url
from . import views
from django.contrib.auth.views import password_reset, password_reset_done

from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'dashboard/$', views.dashboard, name="dashboard"),
    url(r'login/$', views.user_login, name="login"),
    url(r'logout/$', views.user_logout, name="logout"),
    url(r'register/$', views.user_register, name='register'),
    url(r'pass_change/$', views.chage_password, name='change'),
    url(r'user_list/$', views.user_list, name='user_list'),
    url(r'signup/$', views.signup, name='user_signup'),
    url(r'^reset/$',
        auth_views.PasswordResetView.as_view(
            template_name='password_reset.html',
            email_template_name='password_reset_email.html',
            subject_template_name='password_reset_subject.txt'
        ),
        name='password_reset'),
    url(r'^reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),
]


