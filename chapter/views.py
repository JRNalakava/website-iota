from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from iota_web.decorators import user_is_authenticated
from . import forms, models


@login_required
@user_is_authenticated
# Create your views here.
def index(request):
    return render(request, 'chapter/index.html')


@login_required
def authenticate(request, reg_type):
    form = ''
    file_url = 'chapter/authentication/'
    if request.method == 'POST':
        if reg_type == 'active' or reg_type == 'pledge':
            form = forms.MemberForm(request.POST)
            file_url += 'member_register.html'
        elif reg_type == 'alumni':
            form = forms.AlumniUserForm(request.POST)
            file_url += 'alumni_register.html'
        else:
            return render(request, 'chapter/authentication/home_register.html')

        member = form.save(commit=False)
        if form.is_valid():
            member.user = request.user
            member.save()
            if reg_type == 'active':
                active = models.Active.objects.create(member=member)
                active.save()
            return HttpResponseRedirect(reverse('chapter_index'))
    else:
        if reg_type == 'active' or reg_type == 'pledge':
            form = forms.MemberForm()
            file_url += 'member_register.html'
        elif reg_type == 'alumni':
            form = forms.AlumniUserForm()
            file_url += 'alumni_register.html'
        else:
            return render(request, 'chapter/authentication/home_register.html')
    context = {
        'form': form,
    }
    return render(request, file_url, context)


@login_required
def authenticate_active(request):
    form = ''

    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.info(request, "Thanks for registering. You are now logged in.")
            login(request=request, user=user)

            return HttpResponseRedirect(reverse('custom_registration', args=['home']))
    else:
        form = forms.UserForm()

    context = {
        'form': form,
    }
    return render(request, 'open/register/user_register.html', context)
