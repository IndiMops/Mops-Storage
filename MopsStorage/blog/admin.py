from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("post_id", "title", "content", "create_at")
    list_display_links = ("title", )