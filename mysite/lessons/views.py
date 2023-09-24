from django.http import HttpResponse
from django.shortcuts import render

#Сущность Продукт
def index(request):
    text = 'Главная страница'

    template = 'lessons/index.html'
    context = {
        'title': text,
    }
    return render(request, template, context)
    #return HttpResponse('Главная страница')

def product(request):
    template = 'lessons/product.html'
    return render(request, template)

#Сущность Урок
def lesson_list(request):
    template = 'lessons/lesson_list.html'
    return render(request, template)


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def View_lesson_detail(request):
    template_name = 'lessons/lesson_detail.html'
    context = {}
    return render(request, template_name)
# Create your views here.
