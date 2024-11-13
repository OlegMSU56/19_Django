from django.shortcuts import render
from .forms import UserRegister

# Create your views here.

# Из Модуля 18 task4/views
def platform(request):
    title = 'Главная страница'
    context = {
        'title': title
    }
    return render(request, 'platform.html', context)

def games(request):
    games = ['Atomic Heart', 'Cyberpunk 2077', 'GTA']
    return render(request, 'games.html', {'games': games})

def cart(request):
    title = 'Корзина'
    context = {
        'title': title
    }
    return render(request, 'cart.html', context)

# Из Модуля 18 task5/views

users = ['user1', 'user2', 'user3']

def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            users.append(username)
            info['message'] = f'Приветствуем, {username}!'
    return render(request, 'registration_page.html', info)

def django_sign_up(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                users.append(username)
                info['message'] = f'Приветствуем, {username}!'
    else:
        form = UserRegister()
    return render(request, 'registration_page.html', info)