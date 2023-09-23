from django.urls import path
from . import views

urlpatterns = [
    # Главная страница(Продукт)
    path('', views.index),
    # Страница Уроков
    path('lesson/', views.lesson_list),
    # Отдельная страница с информацией о уроках
    path('View_lesson/<str:slug>/', views.View_lesson_detail),
]