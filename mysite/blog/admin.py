from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'modify_date',)
    list_filter = ('modify_date',)
    search_fields = ('title', 'content',)
    prepopuplated_fields = {'slug':('title', )}
    


# Register your models here.
