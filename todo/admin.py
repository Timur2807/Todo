from django.contrib import admin
from .models import ToDO
# Register your models here.


class ToDoController(admin.ModelAdmin):
    readonly_fields = 'created',
    list_display = 'title', 'memo'
    ordering = "-title", "pk"
    search_fields = "title", "memo"


admin.site.register(ToDO, ToDoController)
