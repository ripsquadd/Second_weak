from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterUserForm, CreateRequestForm
from .models import Request



def index(request):
    counter = Request.objects.filter(status="work").all().count()
    completed_requests = Request.objects.filter(status="completed").order_by('-creation_date')[:4]
    return render(request, 'main/index.html', {'completed_requests': completed_requests, 'counter': counter})


class WPLoginView(LoginView):
    template_name = 'main/login.html'


def profile_status_new(request):
    request_items = request.user.request_set.filter(status='new').order_by('-creation_date').all()
    return render(request, 'main/profile.html', context={'request_items': request_items, })



@login_required
def profile(request):
    request_items = request.user.request_set.order_by('-creation_date').all()
    return render(request, 'main/profile.html', context={'request_items': request_items, })


class WPLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'main/logout.html'


class WPRegisterViews(CreateView):
    template_name = 'main/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('webportal:login')


@login_required
def delete(request, pk):
    request = Request.objects.filter(user=request.user, pk=pk, status='new')
    if request:
        request.delete()
    return redirect('webportal:profile')


@login_required
def create(request):
    if request.method == 'POST':
        form = CreateRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user_id = request.user.pk
            form.save()
            messages.warning(request, 'Заявка создана')
            return redirect('webportal:profile')
    else:
        form = CreateRequestForm(initial={'author': request.user})
    context = {'form': form}
    return render(request, 'main/create.html', context)
