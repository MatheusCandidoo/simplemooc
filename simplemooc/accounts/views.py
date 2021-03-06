from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth import get_user_model
from simplemooc.accounts.models import PasswordReset
from .forms import RegisterForm, EditAccountForm, PasswordResetForm
from simplemooc.courses.models import Enrollment

User = get_user_model()


@login_required
def dashboard(request):
    template_name = 'accounts/dashboard.html'
    context ={}
    context['enrollments'] = Enrollment.objects.filter(user=request.user)
    return render(request, template_name, context)


def register(request):
    template_name = 'accounts/register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        print('entrou')
        form = RegisterForm()
    context = {'form': form}
    return render(request, template_name, context)


@login_required
def edit(request):
    context = {}
    template_name = 'accounts/edit.html'
    if request.method == 'POST':
        form = EditAccountForm(request.POST or None, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditAccountForm(instance=request.user)
            context['success'] = True
    else:
        form = EditAccountForm(instance=request.user)
    form = EditAccountForm()
    context['form'] = form
    return render(request, template_name, context)


@login_required
def edit_password(request):
    template_name = 'accounts/edit_password.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            context['success'] = True
    else:
        form = PasswordChangeForm(user=request.user)
    context['form'] = form
    return render(request, template_name, context)


def password_reset(request):
    context = {}
    template_name = 'accounts/password_reset.html'
    form = PasswordResetForm(request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True

    context['form'] = form
    return render(request, template_name, context)


def password_reset_confirm(request, key):
    template_name = 'accounts/password_reset_confirm.html'
    context = {}
    reset = get_object_or_404(PasswordReset, key=key)
    form = SetPasswordForm(user=reset.user, data=request.POST or None)
    if form.is_valid():
        form.save()
        print('passou')
        context['success'] = True


    context['form'] = form
    return render(request, template_name, context)
