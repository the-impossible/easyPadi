from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

# Create your views here.

class LandingPage(TemplateView):
    template_name = "index.html"
