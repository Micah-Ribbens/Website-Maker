from django.shortcuts import render, redirect
from django.views.generic import TemplateView

class documentation_view(TemplateView):
    template_name = "documentation.html"
    def get(self, request, *args):
        return render(request, self.template_name, {})

class step1_view(TemplateView):
    template_name = "step1.html"

    def get(self, request, *args):
        return render(request, self.template_name, {})

class home_view(TemplateView):
    template_name = "home.html"
    
    def get(self, request, *args):
        return render(request, self.template_name, {})
