from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterUserForm


def index(request):
    return render(request, 'main/index.html')

class WPLoginView(LoginView):
    template_name = 'main/login.html'

@login_required
def profile(request):
    return render(request, 'main/profile.html')

class WPLogoutView(LoginRequiredMixin, LogoutView):
   template_name = 'main/logout.html'

class WPRegisterViews(CreateView):
    template_name = 'main/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('webportal:login')