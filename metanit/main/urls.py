
from django.urls import path, include #подключили новый метод
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('user', views.user, name='user'),
    path('modules', views.modules, name='modules'), # пока работаю с этой фигней#
    path('status', views.status, name='status'),
    path('logout/', views.logout_view, name='logout'),
    path('registration', views.registration, name='registration'),
    path('registration', views.registration, name='main'),
]