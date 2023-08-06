from django.contrib import admin
from .models import Journal


# admin.site.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'emotion',"emotion_predications", 'created_at', 'updated_at')
    list_filter = ('author', 'emotion', 'emotion_predications', 'created_at', 'updated_at')
    search_fields = ('title', 'author', 'emotion', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)

admin.site.register(Journal, JournalAdmin)
