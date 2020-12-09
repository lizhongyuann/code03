from django.shortcuts import render, redirect
from django.views import View
from users.models import Users
from django.http import HttpResponse, JsonResponse



class Register(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = Users.objects.create(username=username, passworld=password)
        return redirect('/login/')


class Login(View):
    def get(self, request):
        # username = request.COOKIES.get('username')
        # return render(request, 'login.html', {'username': username})
        id = request.session.get('id')
        if id:
            return JsonResponse({'message': 'already login'})
        else:
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
            request.session['password'] = user.passworld
            if remember != 'true':
                request.session.set_expiry(0)
            return response


