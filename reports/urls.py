from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path('', view),
    path('generate/', generate),
    path('do_generate/', doGenerate),
    re_path(r'^change/(?P<id>\d+)/$', change),
    path('do_change/', doChange),
    re_path(r'^delete/(?P<id>\d+)/$', delete),
]
