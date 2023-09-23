from django.shortcuts import render
from django.http import HttpResponse

#Сущность Продукт
def index(request):
    return HttpResponse('Главная страница')

#Сущность Урок
def lesson_list(request):
    return HttpResponse('Список Уроков')


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def View_lesson_detail(request, slug):
    return HttpResponse(f'Урок номер {slug}')
# Create your views here.
