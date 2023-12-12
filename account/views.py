from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages


from .forms import SignUpForm, UserUpdateForm


User = get_user_model()

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if not user:
            messages.error(request, "User not found")
            return render(request, 'account/login.html')
        login(request, user)
        messages.info(request, 'Login successfull!')
        return redirect('blog:home')
    return render(request, 'account/login.html')


def logout_view(request):
    logout(request)
    messages.info(request, 'Logout successfull')
    return redirect('account:login')


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # subject = 'Test project'
            # message = f'Hi {user.username}, thank you for registering in blog web sayt.'
            # email_from = settings.EMAIL_HOST_USER
            # recipient_list = [user.email, ]
            # send_mail(subject, message, email_from, recipient_list)
            messages.success(request, 'Siz ruyxatdan o`tdingiz')
            return redirect('account:login')
        messages.warning(request, 'qayta urinib kuring')

    form = SignUpForm()

    context = {
        'form': form,
    }

    return render(request, 'account/register.html', context)


@login_required()
def user_profile(request):
    print(request.user)
    user = User.objects.filter(username=request.user).first()

    context = {
        'user': user
    }
    return render(request, 'account/profile.html', context)


@login_required()
def user_profile_edit(request):
    user = User.objects.filter(username=request.user.username).first()
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('account:user_profile')
    form = UserUpdateForm(instance=user)
    context = {
        'form': form
    }
    return render(request, 'account/user_profile_edit.html', context)


@login_required()
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('account:user_profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)

    context = {
        'form': form
    }
    return render(request, 'account/change_password.html', context)
