from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from django.core.mail import send_mail

from hipestory import settings

from users.forms import AddAvatarForm, CropAvatarForm, UserRegisterForm, UserLoginForm, NewStoryForm


@login_required
def profile(request):
    return render(request, 'users/profile.html')


@login_required
def change_avatar(request):
    context = {'form': AddAvatarForm()}
    return render(request, 'users/change_avatar.html', context)


@login_required
def crop_avatar(request):
    if request.method == 'POST':
        form = CropAvatarForm(request.POST)
        print(request.POST, request.FILES)
        # user = request.user
        # user.avatar = form.cleaned_data.get('hidden')
        # user.save()
        # return redirect('users:profile')
    else:
        form = CropAvatarForm()
    context = {
        'form': form,
    }
    return render(request, 'users/crop_avatar.html', context)


@login_required
def add_avatar(request):
    form = AddAvatarForm(request.POST, files=request.FILES)
    if form.is_valid():
        avatar = form.files.get('avatar', '')
        if avatar:
            user = request.user
            avatar.name = f'{user.username}.png'
            user.avatar = avatar
            user.save()
            messages.success(request, 'Аватарка успешно изменена!')
            return redirect('users:profile')
        return redirect('users:change_avatar')
    return redirect('users:change_avatar')


@login_required
def delete_avatar(request):
    user = request.user
    user.avatar = ''
    user.save()
    messages.success(request, 'Аватарка успешно удалена!')
    return redirect('users:profile')


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    next_page = reverse_lazy('users:profile')


class UserRegisterView(SuccessMessageMixin, CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'
    success_message = 'Вы успешно зарегистрировались!'


class UserLogoutView(LogoutView):
    # next_page = reverse_lazy('users:logout')
    template_name = 'users/logout.html'


@login_required
def logout_user(request):
    logout(request.user)
    return render(request, 'users/logout.html')


@login_required
def new_story(request):
    if request.method == 'POST':
        form = NewStoryForm(request.POST)
        if form.is_valid():
            user = request.user
            send_mail('Предложение истории | Администрация HipeStory',
                      f'Пользователь с ником {user.username} пердлагает следующую историю:\n\n'
                      f'Заголовок: {form.cleaned_data.get("title")}\n\n'
                      f'Содержимое: {form.cleaned_data.get("body")}',
                      settings.DEFAULT_EMAIL_NAME, settings.ADMINISTRATION_EMAILS)
            messages.success(request,
                             'История успешно отправлена, '
                             'вскоре вы получите ответ на почту, '
                             'которую указали при регистрации.')
            return redirect('main:index')
    else:
        form = NewStoryForm()
    context = {
        'form': form
    }
    return render(request, 'users/new_story.html', context)
