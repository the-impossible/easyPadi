from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

# Create your views here.

class LandingPage(TemplateView):
    template_name = "index.html"

class AboutPage(TemplateView):
    template_name = "about.html"

class ContactPage(TemplateView):
    template_name = "contacts.html"

class PolicyPage(TemplateView):
    template_name = "policy.html"

class ErrorPage(TemplateView):
    template_name = "404.html"
