from django.contrib import admin
from django.utils.html import format_html
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('display_image', 'blog_title', 'blog_des')  # Removed 'blog_icon'

    def display_image(self, obj):
        if obj.blog_image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit:cover;"/>', obj.blog_image.url)
        return "No Image"
    
    display_image.short_description = "Blog Image"  # Column name in Django Admin

admin.site.register(Blog, BlogAdmin)
