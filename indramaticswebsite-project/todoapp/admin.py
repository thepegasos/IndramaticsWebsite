from django.contrib import admin
from .models import Todo


# to display the read only fields. Without following, created field will not be displayed
class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


# Register your models here.
admin.site.register(Todo, TodoAdmin)
