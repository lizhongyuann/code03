from django.urls import re_path
from users.views import Register, Login

urlpatterns = [
    re_path(r'^register/$', Register.as_view()),
    re_path(r'^login/$', Login.as_view()),
]