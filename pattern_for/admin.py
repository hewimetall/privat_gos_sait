from django.contrib import admin
from .models import pattern_for #,categoy
from markdownx.admin import MarkdownxModelAdmin
from markdownx.widgets import AdminMarkdownxWidget
#
# class CatAdmin(admin.ModelAdmin):
#     list_display=['name','slug']
#     prepopulated_fields={'slug':('name',)}

class Prod_Admin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'categoy', 'image', 'text', 'price']
    prepopulated_fields = {'slug': ('name',)}

    formfield_overrides = {
        pattern_for.text: {'widget': AdminMarkdownxWidget},
    }
# admin.site.register(categoy,CatAdmin)

admin.site.register(pattern_for,Prod_Admin)

