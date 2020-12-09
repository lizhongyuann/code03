from django.urls import re_path
from helloworld.views import First

urlpatterns = [
    re_path(r'hello-world/$', First.as_view()),
]