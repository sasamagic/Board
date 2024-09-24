from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout as auth_logout
from database.models import Modules
from .forms import regForm

# Create your views here.

def index(request):
    return render(request,'main/index.html')
def user (request):
    return render(request,'main/user.html')
# def modules (request):
#     error = ''
#     if request.method == 'POST':
#         form = regForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('status')
#         else:
#             error = 'ахтунг ошибка'
#     else:
#         form = regForm()  # Create an empty form for GET requests
#
#     context = {
#         'form': form,
#         'error': error
#     }
#     return render(request,'main/modules.html',context) # ОСТАВИЛА НА СЛУЧАЙ ПОЛОМКИ #


# ТУТ КАЖЕТСЯ ТУТ ВСЕ ОК

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
def registration (request):
    return render(request,'main/registration.html')