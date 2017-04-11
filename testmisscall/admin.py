from django.contrib import admin

from .models import Call

class CallAdmin(admin.ModelAdmin):
    """
        List display for Charts in Django Admin
    """
    model = Call
    list_display = ['data']

admin.site.register(Call, CallAdmin)
