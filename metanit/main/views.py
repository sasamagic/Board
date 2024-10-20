from django.contrib.auth import logout as auth_logout
from database.models import Modules
from .forms import regForm
from .forms import info_modulesForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
def new_info_modules (request):
    error = ''  # Инициализирует пустую строку для хранения сообщения об ошибке.
    if request.method == 'POST':    # Проверяет, был ли запрос методом POST (обычно используется для отправки формы)
        form = info_modulesForm(request.POST)    # Создает экземпляр формы regForm, передавая данные, полученные из POST-запроса.
        if form.is_valid():     # Проверяет, является ли форма валидной (все обязательные поля заполнены и данные корректны).
            form.save()     # Сохраняет данные формы в базу данных.
            return redirect('status')   # Перенаправляет пользователя на страницу с именем 'status' после успешного сохранения.
        else:
            error = 'ахтунг ошибка'     # Устанавливает сообщение об ошибке.
    else:       # Если метод запроса не POST, выполняется этот блок.
        form = info_modulesForm()  # Создает пустую форму для GET-запросов (когда пользователь просто загружает страницу).

    context = {     # Начинает создание словаря context, который будет передан в шаблон.
        'form': form,       # Добавляет объект формы в словарь context.
        'error': error      # Добавляет сообщение об ошибке в словарь context.
    }
    return render(request,'main/new_info_modules.html',context)
def modules (request):
    error = ''  # Инициализирует пустую строку для хранения сообщения об ошибке.
    if request.method == 'POST':    # Проверяет, был ли запрос методом POST (обычно используется для отправки формы)
        form = regForm(request.POST)    # Создает экземпляр формы regForm, передавая данные, полученные из POST-запроса.
        if form.is_valid():     # Проверяет, является ли форма валидной (все обязательные поля заполнены и данные корректны).
            form.save()     # Сохраняет данные формы в базу данных.
            return redirect('status')   # Перенаправляет пользователя на страницу с именем 'status' после успешного сохранения.
        else:
            error = 'ахтунг ошибка'     # Устанавливает сообщение об ошибке.
    else:       # Если метод запроса не POST, выполняется этот блок.
        form = regForm()  # Создает пустую форму для GET-запросов (когда пользователь просто загружает страницу).

    context = {     # Начинает создание словаря context, который будет передан в шаблон.
        'form': form,       # Добавляет объект формы в словарь context.
        'error': error      # Добавляет сообщение об ошибке в словарь context.
    }
    return render(request,'main/modules.html',context) # Возвращает ответ с отрисованным шаблоном 'main/modules.html', используя созданный контекст.

# для регистрации несуществующего изделия

def index(request):
    return render(request,'main/index.html')

def status (request):
    serial_number = request.GET.get('serial_number')
    tasks = []

    if serial_number:
        # Фильтруем по серийному номеру
        tasks = Modules.objects.filter(serial_number=serial_number)
    else:
        print(tasks)
    return render(request,'main/status.html',{'title': 'Статус модуля','tasks':tasks})

def logout_view(request):
    auth_logout(request)
    return redirect('home')

# Модель для формы регистрации пользователя
def registration (request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) # Создается экземпляр формы UserRegisterForm, и в него передаются данные, полученные из request.POST
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') # Извлекается имя пользователя (username) из очищенных данных формы
            messages.success(request, f'Создан аккаунт {username}!') # Генерируется сообщение об успешном создании аккаунта
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'main/registration.html', {'form': form})

# Модель для формы входа в аккаунт пользователя
def user(request):
    if request.method == 'POST':
        username_or_email = request.POST['auth_login']
        password = request.POST['auth_pass']

        # Попробуйте аутентифицировать пользователя по имени пользователя
        user = authenticate(request, username=username_or_email, password=password)

        if user is None:
            # Попробуйте найти пользователя по email
            try:
                user = User.objects.get(email=username_or_email)
                if user.check_password(password):
                    login(request, user)
                    return redirect('home')  # Перенаправление на главную страницу
                else:
                    messages.error(request, "Неверный пароль")
            except User.DoesNotExist:
                messages.error(request, "Пользователь не найден")
        else:
            # Успешная аутентификация
            login(request, user)
            return redirect('home')  # Перенаправление на главную страницу

    return render(request, 'main/user.html')  # Отображение формы входа
