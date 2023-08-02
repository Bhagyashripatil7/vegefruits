from django.contrib import admin
from .models import Feedback
class FeedbackAdmin(admin.ModelAdmin):
    list_display=('name','email','subject','message')

admin.site.register(Feedback,FeedbackAdmin)
# Register your models here.


# Register your models here.
