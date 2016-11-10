"""URLPatterns for registration app."""
from django.conf.urls import url
from django.contrib.auth import views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from .views import UserDetailView

urlpatterns = (url(r'^login/$', views.login,
                   {'template_name': 'registration/login.haml'},
                   name='login'),
               url('^signup/', CreateView.as_view(
                   template_name='registration/signup.haml',
                   form_class=UserCreationForm,
                   success_url='/'),
                   name='signup'),
               url(r'^logout/$', views.logout,
                   {'template_name': 'registration/logout.haml'},
                   name='logout'),
               url(r'^password_change/$', views.password_change,
                   {'template_name': 'registration/password_change.haml'},
                   name='password_change'),
               url(r'^password_change/done/$', views.password_change_done,
                   {'template_name': 'registration/password_change_done.haml'},
                   name='password_change_done'),
               url(r'^password_reset/$', views.password_reset,
                   {'template_name': 'registration/password_reset.haml'},
                   name='password_reset'),
               url(r'^password_reset/done/$', views.password_reset_done,
                   {'template_name': 'registration/password_reset_done.haml'},
                   name='password_reset_done'),
               url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/'
                   r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
                   views.password_reset_confirm,
                   {'template_name':
                    'registration/password_reset_confirm.haml'},
                   name='password_reset_confirm'),
               url(r'^reset/done/$', views.password_reset_complete,
                   {'template_name':
                    'registration/password_reset_complete.haml'},
                   name='password_reset_complete'),
               url(r'^profile/$', UserDetailView.as_view(), name='profile'))
