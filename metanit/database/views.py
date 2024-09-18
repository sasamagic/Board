# views.py
from django.shortcuts import render, get_object_or_404
from database.models import Modules


def status(request):
    # Получаем все записи из модели Modules
    products = Modules.objects.all()

    # Добавляем отладочный вывод
    print(f"Retrieved products: {products}")

    if 'serial_number' in request.GET:
        serial_number = request.GET['serial_number']
        try:
            product = Modules.objects.get(serial_number=serial_number)
            products = [product]  # Показываем только один продукт, соответствующий серийному номеру
        except Modules.DoesNotExist:
            products = []  # Если продукт не найден, передаем пустой список

    context = {
        'products': products
    }
    return render(request, 'main/status.html', context)
