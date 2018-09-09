from django.contrib import admin
from .models import Album, Photo

class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 2


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    list_display = ('name', 'description')


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date')
