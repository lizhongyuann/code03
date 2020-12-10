from django.shortcuts import render, redirect
from django.views import View
from users.models import Users
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator

# def is_login(request):
#     username = request.session.get('username')
#     if username:
#         return HttpResponse(f'<h1>{username}用户已经登录, 这就是登录页面<h1/>')

def is_login(view_func):
    def wepper(request):
        username = request.session.get('username')
        if username:
            return HttpResponse(f'<h1>{username:}已登录,这个是登录后的页面<h1/>')
        return view_func(request)
    return wepper

class Is_login(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view_func = super().as_view(**initkwargs)
        return is_login(view_func)

class Register(View):


    def get(self, request):
        return render(request, 'register.html')


    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = Users.objects.create(username=username, passworld=password)
        return redirect('/login/')


class Login(Is_login, View):


    def get(self, request):
        # username = request.COOKIES.get('username')
        # return render(request, 'login.html', {'username': username})

        return render(request, 'login.html')


    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')
        try:
            user = Users.objects.get(username=username, passworld=password)
        except Users.DoesNotExist as error:
            return JsonResponse({'message': 'login faile'})
        else:

            response = JsonResponse({'message': 'login sucuss'})
            request.session['id'] = user.id
            request.session['username'] = user.username
            if remember != 'true':
                request.session.set_expiry(0)
            return response


