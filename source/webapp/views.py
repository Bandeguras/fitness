from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.


class ProjectIndex(ListView):
    model = get_user_model()
    template_name = 'project/index.html'
