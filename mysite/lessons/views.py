from django.http import HttpResponse
from django.shortcuts import render

#Сущность Продукт
def index(request):
    template = 'lessons/index.html'
    return render(request, template)
    #return HttpResponse('Главная страница')

def product(request):
    template = 'lessons/product.html'
    return render(request, template)

#Сущность Урок
def lesson_list(request):
    template = 'lessons/lesson_list.html'
    return HttpResponse('Список Уроков')


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def View_lesson_detail(request, slug):
    template_name = 'lessons/lesson_detail.html'
    return HttpResponse(f'<h1>Урок номер</h1> {slug}')
# Create your views here.
