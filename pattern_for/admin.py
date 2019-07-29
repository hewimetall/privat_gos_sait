from django.contrib import admin
from django.contrib.auth.models import Group, User

from .models import pattern_for #,categoy
from markdownx.admin import MarkdownxModelAdmin
from markdownx.widgets import AdminMarkdownxWidget
#
# class CatAdmin(admin.ModelAdmin):
#     list_display=['name','slug']
#     prepopulated_fields={'slug':('name',)}
@admin.register(pattern_for)
class Prod_Admin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'categoy', 'image', 'text', 'price']
    prepopulated_fields = {'slug': ('name',)}

    formfield_overrides = {
        pattern_for.text: {'widget': AdminMarkdownxWidget},
    }
# admin.site.register(categoy,CatAdmin)
