from django.contrib import admin
from django.contrib import admin
from .models import Statement
class StatementAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','address','items','total','modepayment')


admin.site.register(Statement,StatementAdmin)

# Register your models here.
