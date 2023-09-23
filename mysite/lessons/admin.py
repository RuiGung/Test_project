from django.contrib import admin
from .models import Product, Lesson ,LessonView
# Register your models here.

#настройки отображения модели в интерфейсе админки
class ProductAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk', 'name', 'owner',) 
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('name',)
    # Это свойство сработает для всех колонок: где пусто — там будет эта строка 
    empty_value_display = '-пусто-'  

class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'video_link', 'duration_seconds',)
    search_fields = ('name',)

class LessonViewAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson', 'viewed_time_seconds', 'is_viewed',)
    search_fields = ('user',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(LessonView, LessonViewAdmin)