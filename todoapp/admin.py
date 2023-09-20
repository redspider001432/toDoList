from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'due_date', 'status')
    list_filter = ('status', 'tags')
    search_fields = ('title', 'description', 'tags__name')
    readonly_fields = ('timestamp',) # Fields that are read-only

    fieldsets = (
        (None, {'fields': ('title', 'description', 'due_date')}),
        ('Status', {'fields': ('status',)}),
        ('Tags', {'fields': ('tags',)}),
    ) # Grouping fields into sections (fieldsets)

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if obj:
            return readonly_fields + ('timestamp',) # Making timestamp field read-only when editing an existing object
        return readonly_fields

admin.site.register(Task, TaskAdmin)
