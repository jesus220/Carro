from django.shortcuts import render
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.http import HttpRequest
from django.http import HttpResponse
from django.db.models import Count
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

class Home (APIView):
    template_name="prueba.html"
    def get(self, request):
        return render(request,self.template_name)
    