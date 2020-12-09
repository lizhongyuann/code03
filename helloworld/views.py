from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse

class First(View):
    def get(self, request):

        return HttpResponse('<h1>hellow world<h1/>')

    def post(self, request):
        pass

