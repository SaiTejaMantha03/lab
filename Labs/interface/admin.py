from django.contrib import admin
from .models import User, Test

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address')
    list_filter = ('name',)
    search_fields = ('name', 'email', 'phone')
    ordering = ('name',)

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'test', 'test_status', 'created_at')
    list_filter = ('test_status', 'test', 'created_at')
    search_fields = ('name', 'email', 'test')
    ordering = ('-created_at',)
    list_editable = ('test_status',)
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related()