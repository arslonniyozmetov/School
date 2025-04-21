from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted', 'image_preview')
    list_filter = ('date_posted',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 50px; max-width: 50px;" />')
        return "-"

    image_preview.short_description = 'Rasm'