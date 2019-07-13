from django.contrib import admin
from .models import Post
from markdownx.admin import MarkdownxModelAdmin
from markdownx.widgets import AdminMarkdownxWidget

class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        Post.content: {'widget': AdminMarkdownxWidget},
    }
admin.site.register(Post,MarkdownxModelAdmin)
