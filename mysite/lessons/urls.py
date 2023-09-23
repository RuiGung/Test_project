from django.urls import path
from . import views

urlpatterns = [
    # Главная страница(Продукт)
    path('', views.index),
    #Продукт
    path('products/', views.product),
    # Страница Уроков
    path('lessons/', views.lesson_list),
    # Отдельная страница с информацией о уроках
    path('View_lesson/<str:slug>/', views.View_lesson_detail),
]