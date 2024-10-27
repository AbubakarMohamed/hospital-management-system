from django.urls import path
from sigin.views import auth_view
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('auth', auth_view),
]
