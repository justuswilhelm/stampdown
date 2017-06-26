"""URLPatterns for account app."""
from django.conf.urls import url
from django.contrib.auth import views
from django.urls import reverse_lazy

from .views import (
    SignupDoneView,
    SignupView,
    UserDetailView,
)


urlpatterns = (
    url(
        r'^login/$',
        views.LoginView.as_view(
            template_name='account/login.haml',
        ),
        name='login',
    ),
    url('^signup/', SignupView.as_view(), name='signup'),
    url('^signup_done/', SignupDoneView.as_view(), name='signup_done'),
    url(
        r'^logout/$',
        views.LogoutView.as_view(
            template_name='account/logout.haml',
        ),
        name='logout',
    ),
    url(
        r'^password_change/$',
        views.PasswordChangeView.as_view(
            template_name='account/password_change.haml',
            success_url=reverse_lazy('account:password_change_done'),
        ),
        name='password_change',
    ),
    url(
        r'^password_change/done/$',
        views.PasswordChangeDoneView.as_view(
            template_name='account/password_change_done.haml',
        ),
        name='password_change_done',
    ),
    url(
        r'^password_reset/$',
        views.PasswordResetView.as_view(
            template_name='account/password_reset.haml',
        ),
        name='password_reset',
    ),
    url(
        r'^password_reset/done/$',
        views.PasswordResetDoneView.as_view(
            template_name='account/password_reset_done.haml',
        ),
        name='password_reset_done',
    ),
    url(
        r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/'
        r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.PasswordResetConfirmView.as_view(
            template_name='account/password_reset_confirm.haml',
        ),
        name='password_reset_confirm',
    ),
    url(
        r'^reset/done/$',
        views.PasswordResetCompleteView.as_view(
            template_name='account/password_reset_complete.haml',
        ),
        name='password_reset_complete',
    ),
    url(
        r'^profile/$',
        UserDetailView.as_view(),
        name='user_detail',
    ),
)
