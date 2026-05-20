from django.contrib import admin
from .models import Driver

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email', 'phone')
    list_editable = ('age',)
    search_fields = ('name', 'phone', 'email')
    fields = ('name', 'age', 'email', 'phone')

    def get_readonly_fields(self, request, obj=None):
        if obj:  
            return ('email',)
        return ()  
