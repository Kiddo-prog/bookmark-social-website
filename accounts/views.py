import profile
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd["username"], password=cd["password"]
            )

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("accounts:dashboard")
                else:
                    return HttpResponse("Account not activated")
    else:
        form = LoginForm()
    return render(request, "registration/login.html", {"form": form})


@login_required
def dashboard(request):
    queryset = Profile.objects.all()
    return render(request, "accounts/dashboard.html", {'profile': queryset})


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data["password"])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, "accounts/register_done.html", {"form": form})
    else:
        form = UserRegistrationForm()
    return render(request, "accounts/register.html", {"form": form})


@login_required
def editProfile(request):
    if request.method == "POST":
        user_form = UserEditForm(request.POST, instance=request.user)
        profile_form = ProfileEditForm(
            request.POST, instance=request.user.profile, files=request.FILES
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile updated successfully")
            return redirect("accounts:dashboard")
        else:
            messages.error(request, "Error updating profile")

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(
        request,
        "accounts/edit.html",
        {"user_form": user_form, "profile_form": profile_form},
    )
