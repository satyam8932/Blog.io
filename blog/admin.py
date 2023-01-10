from django.contrib import admin
from .models import Category , Posts
# Register your models here.

# for configuration of Category Admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('imageTag','Title','Description',"url",'Date')
    search_fields = ('Title',)
    
# for configuration of Post Admin
class PostAdmin(admin.ModelAdmin):
    list_display = ('imageTag','Title',"url") 
    search_fields = ('Title',)
    list_filter = ('Category',)
    list_per_page = 10
    
    
    # for tinymce integration
    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/6/tinymce.min.js','js/script.js',)
        # css = ('css/style.css',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Posts , PostAdmin)
