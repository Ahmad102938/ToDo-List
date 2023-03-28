from django.contrib import admin
from todoapp.models import TodoListItem

class todoappAdmin(admin.ModelAdmin):
    list_display=['content']

admin.site.register(TodoListItem, todoappAdmin)

# Register your models here.
